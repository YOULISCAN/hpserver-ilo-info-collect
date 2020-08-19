# -*- coding: utf-8 -*-
'''
把DB排除
'''
import hpilo
import pymysql
import os
import database
import cx_Oracle
def connect_oracle():
    conn = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244:1521/db244d')
    try:
        with conn.cursor() as cursor:
            cursor.execute("select IP_ILO from itim_auto.ITIM_ASSETS where SERVER_TYPE='DB' and SITE_CODE_ID='GL'")
            data = cursor.fetchall()
    finally:
        conn.close()
    return data

def connection_mysql(ip):
    connection = pymysql.connect(host='10.172.108.131',
                                 port=3306,
                                 user='SM',
                                 passwd='SM-dpbg123.',
                                 db='hpilo',
                                 charset="utf8")
    try:
        with connection.cursor() as cursor:
            sql = "update `ilo_IP` set `dba`= 1 where `IP` = '%s'" % (ip)
            cursor.execute(sql)
        connection.commit()
    finally:
        connection.close()

a = connect_oracle()
all_dbip = []
for ip in a:
    ip = str(ip).lstrip("(").rstrip(")").rstrip(",").strip("/'").strip()
    all_dbip.append(ip)
for ip in all_dbip:
    connection_mysql(ip)


