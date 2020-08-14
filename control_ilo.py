#对ilo表进行账号密码测试

import  pymysql
import hpilo
import os


def get_ilo():
    connection = pymysql.connect(host='10.172.108.131',
                                 port=3306,
                                 user='SM',
                                 passwd='SM-dpbg123.',
                                 db='hpilo',
                                 charset="utf8")
    try:
        with connection.cursor() as cursor:
            sql = "select IP from ilo_IP"
            cursor.execute(sql)
            a = cursor.fetchall()
    finally:
        connection.close()

    for ip in a:
        ip = str(ip).lstrip("(").rstrip(")").rstrip(",").strip("/'").strip()
        print("---------------尝试账号登录IP:%s----------------"%(ip))
        ilo = hpilo.Ilo(ip,login="admin",password="iL0!@#123")
        print(ilo.get_fw_version())

get_ilo()
