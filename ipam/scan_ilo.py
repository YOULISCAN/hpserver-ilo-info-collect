# -*- coding: utf-8 -*-
#网段扫描
import subprocess
import threading

import nmap
import cx_Oracle
import queue
import time
num_threads = 200
num_threads1 = 200
q = queue.Queue()
p = queue.Queue()
addlock = threading.Lock()
strr1 = 'HP Integrated Lights-Out mpSSH'
strr2 = "AllegroSoft RomSShell sshd"
#class collect_IP():


def connect_oracle(IP,judge):

    if judge == 0:
        p.put(IP)
        connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
        status = 1
        param = {'PING_IP': status ,'IP_ILO': IP}
        print(type(IP),status)
        with connection.cursor() as cursor:
            cursor.execute('update ILO_INFO set PING_IP=:PING_IP where IP_ILO=:IP_ILO', param)
        connection.commit()
        connection.close()
    else:
        connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
        status = 0
        param = {'PING_IP': status, 'IP_ILO': IP}
        with connection.cursor() as cursor:
            cursor.execute('update GL_SM.ILO_INFO set PING_IP=:PING_IP where IP_ILO=:IP_ILO', param)
        connection.commit()
        connection.close()


#class judge_IP():
def Ping_all():
    while not q.empty():
        ip = q.get()
        q.task_done()
        res = subprocess.call('ping -n 2 -w 5 %s' % '{0}'.format(ip), stdout=subprocess.PIPE)
        with addlock:
            if res == 0:
                print(ip,"------>该IP使用中")
                print(res)
                connect_oracle(ip,res)

            else:
                print(ip,"------>该IP闲置中")
                print(res)
                connect_oracle(ip,res)

def judge_ilo():
    print("----------------开始扫描指定IP--------------------")
    while not p.empty():
        ip = p.get()
        nm = nmap.PortScanner()
        print("----------------扫描（%s:22）端口--------------------"%(ip))
        portinfo = nm.scan(ip, '22')
        portinfo = nm.csv()
        portinfo1 = portinfo.split(';')
        for i in portinfo1:
            number = 0
            if i == strr1 or i == strr2 :
                print(ip,'----->该IP已配置ilo插入数据库')
                connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
                status = 1
                param = {'IP_ILO': ip, 'IP_ILO_STATUS': status}
                print(param)
                with connection.cursor() as cursor:
                    cursor.execute('UPDATE GL_SM.ILO_INFO SET IP_ILO_STATUS=:IP_ILO_STATUS WHERE IP_ILO=:IP_ILO',param)
                connection.commit()
                connection.close()
                continue
            else:
                number += 1
            if number == len(portinfo1):
                connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
                status = 0
                param = {'IP_ILO': ip, 'IP_ILO_STATUS': status}
                print(param)
                with connection.cursor() as cursor:
                    cursor.execute('UPDATE GL_SM.ILO_INFO SET IP_ILO_STATUS=:IP_ILO_STATUS WHERE IP_ILO=:IP_ILO', param)
                connection.commit()
                connection.close()

def update_info(ip,site):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {
        "IP_ILO":ip , "SITE": site
    }
    with connection.cursor() as cursor:
        try:
            cursor.execute('INSERT into ILO_INFO(IP_ILO,SITE) values (:IP_ILO,:SITE)',param)
        except:
            print('unique value')
    connection.commit()
    connection.close()



if __name__ == '__main__':

    #sql1 = 'SELECT IP_ILO FROM GL_SM.ILO_INFO where IP_ILO=:IP_ILO'
    sql = '''   select site_code_id,ip_ilo,count(ip_ilo) as num
                from itim_auto.ITIM_ASSETS@itim_auto_pitimdb where CATEGORY_ID='服務器'
                and ASSETS_STATUS_ID in ('正式','在用','備用','測試') and assets_model like 'HP%'
                group by site_code_id,ip_ilo having count(ip_ilo)=1      
          '''
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    with connection.cursor() as cursor:
       hah1 = cursor.execute(sql)
      # file = open("IP.txt", 'r')
       for i in hah1:
           ip = str(i[1]).lstrip('(').rstrip(")").strip(",")
           site = i[0]
           try:
               update_info(ip,site)
               print(ip,site)
           except:
               raise

           q.put(ip)
           print(ip)
    connection.commit()
    connection.close()
    size = q.qsize()
    print(size)
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=Ping_all, args=())
        thread.start()
        threads.append(thread)
    for thread in threads: thread.join()

    for j in range(num_threads1):
        threading.Thread(target=judge_ilo, args=()).start()
    judge_ilo()

