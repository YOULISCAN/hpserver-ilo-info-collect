
#网段扫描
import hpilo
import subprocess
import os
import pymysql
import queue
import threading

num_threads = 10
q = queue.Queue()
addlock = threading.Lock()
class collect_IP():
    def connect_mysql( IP, judge):
        if judge == 1:
            connection = pymysql.connect(host='10.172.108.229',port=3306,user='SM',passwd='SM-dpbg123.',db='hpilo_info_collect',charset='utf8')
            try:
                with connection.cursor() as cursor:
                    sql = "insert into `using_IP` (`IP`) value (%s)"
                    cursor.execute(sql, (IP))
                connection.commit()
            finally:
                connection.close()
        else:
            connection = pymysql.connect(host='10.172.108.229', port=3306, user='SM', passwd='SM-dpbg123.', db='hpilo_info_collect',charset='utf8')
            try:
                with connection.cursor() as cursor:
                    sql = "insert into `dead_IP` (`IP`) value (%s)"
                    cursor.execute(sql, (IP))
                connection.commit()
            finally:
                connection.close()


class judge_IP():
    def Ping_all(self):
        while not q.empty():
            ip = q.get()
            res = subprocess.call('ping -n 2 -w 5 %s' % '{0}'.format(ip), stdout=subprocess.PIPE)
            with addlock:
                if res == 1:
                    print(ip,"------>该IP使用中")
                    collect_IP.connect_mysql(ip,res)
                else:
                    print(ip,"------>该IP闲置中")
                    collect_IP.connect_mysql(ip,res)
            q.task_done()



if __name__ == '__main__':
    file = open("IP.txt", 'r', encoding='utf-8')
    for i in file:
        i = i.strip()
        q.put(i)
    size = q.qsize()
    threads = []
    for i in range(num_threads):
        threading.Thread(target=judge_IP.Ping_all, args=(i,)).start()

 #   for thread in threads: thread.join()