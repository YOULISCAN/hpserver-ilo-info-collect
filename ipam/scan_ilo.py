# -*- coding: utf-8 -*-
#网段扫描
import subprocess
import threading

import nmap
import cx_Oracle
import queue

num_threads = 10
num_threads1 = 5
q = queue.Queue()
p = queue.Queue()
addlock = threading.Lock()
strr1 = 'HP Integrated Lights-Out mpSSH'
strr2 = "AllegroSoft RomSShell sshd"
#class collect_IP():


def connect_oracle( IP,judge):

    if judge == 0:
        p.put(IP)
        connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
        try:
            status = 1
            param = {'IP': IP, 'status': status}
            with connection.cursor() as cursor:
#                sql = ""
                cursor.execute('insert into "ip_test" values(:IP,:status)' , param)
            connection.commit()
        finally:
            connection.close()
    else:

        connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
        try:
            status = 0
            param = {'IP': IP, 'status': status}
            with connection.cursor() as cursor:
            #    sql = "'insert into ip_test values(:IP,:status)' , param"
                cursor.execute('insert into "ip_test" values(:IP,:status)' , param)
            connection.commit()
        finally:
            connection.close()


#class judge_IP():
def Ping_all(self):
    while not q.empty():
        ip = q.get()
        q.task_done()
        res = subprocess.call('ping -n 2 -w 5 %s' % '{0}'.format(ip), stdout=subprocess.PIPE)
        with addlock:
            if res == 0:
                print(ip,"------>该IP使用中")
                connect_oracle(ip,res)
            else:
                print(ip,"------>该IP闲置中")
                connect_oracle(ip,res)

def judge_ilo(self):
    print("----------------开始扫描指定IP--------------------")
    while not p.empty():
        ip = p.get()
        nm = nmap.PortScanner()
        print("----------------扫描（%s:22）端口--------------------"%(ip))
        portinfo = nm.scan(ip, '22')
        portinfo = nm.csv()
        portinfo1 = portinfo.split(';')
        for i in portinfo1:
            if i == strr1 or i == strr2 :
                print(ip,'----->该IP已配置ilo插入数据库')
                connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
                try:
                    status = 1
                    param = {'IP_ILO': ip, 'IP_ILO_STATUS': status}
                    with connection.cursor() as cursor:
                      # sql = ""
                        cursor.execute('insert into ILO_INFO (IP_ILO,IP_ILO_STATUS)values(:IP_ILO,:IP_ILO_STATUS)',param)
                    connection.commit()
                finally:
                    connection.close()




if __name__ == '__main__':
    file = open("ipam\IP.txt", 'r', encoding='utf-8')
    for i in file:
        i = i.strip()
        q.put(i)
    size = q.qsize()
    threads = []
    for i in range(num_threads):
         thread = threading.Thread(target=Ping_all, args=(i,))
         thread.start()
         threads.append(thread)
    for thread in threads: thread.join()

    for j in range(num_threads1):
        threading.Thread(target=judge_ilo, args=(j,)).start()
    #judge_ilo()
