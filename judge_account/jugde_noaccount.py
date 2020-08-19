# -*- coding: utf-8 -*-
import pymysql

connection = pymysql.connect(host='10.172.108.131',
                             port=3306,
                             user='SM',
                             passwd='SM-dpbg123.',
                             db='hpilo',
                             charset="utf8")
try:
    with connection.cursor() as cursor:
        sql = "select IP  from `ilo_IP` where `flag` is Null and `dba`is Null"
        cursor.execute(sql)
        data = cursor.fetchall()
finally:
    connection.close()
print(data)