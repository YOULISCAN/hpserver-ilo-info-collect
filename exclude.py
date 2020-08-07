#有些ilo是dba的server涉及生产 暂做排除操作
'''
1.先对比刷出来的所有ilo是否包含了dba的全部设备
'''
import queue
import pymysql
q_dba = queue.Queue()
q_all = queue.Queue()

file = open("DBA_ilo.txt", 'r', encoding='utf-8')
for i in file:
    i = i.strip()
    q_dba.put(i)


connection = pymysql.connect(host='10.172.108.229',
                                 port=3306,
                                 user='SM',
                                 passwd='SM-dpbg123.',
                                 db='hpilo_info_collect',
                                 charset="utf8")
try:
    with connection.cursor() as cursor:
        sql = "select IP from ilo_IP"
        cursor.execute(sql)
        a = cursor.fetchall()
finally:
    connection.close()
all_ip = []
for ip in a:
    ip = str(ip).lstrip("(").rstrip(")").rstrip(",").strip("/'").strip()
    all_ip.append(ip)

diff = []

while True:
    item = q_dba.get()
    count = 0
    for i in all_ip:
        if item != i:
            count += 1
            if count == len(all_ip):
                diff.append(item)
        else:
            break

    if q_dba.qsize() == 0:
        break
print(diff)