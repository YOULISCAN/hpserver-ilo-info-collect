# -*- coding: utf-8 -*-
#对ilo表进行账号密码测试

import pymysql
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
            sql = "select IP from ilo_IP where flag is null and dba is null"
            cursor.execute(sql)
            a = cursor.fetchall()
    finally:
        connection.close()
    return a
def insert_flag(flag,ip):
    connection = pymysql.connect(host='10.172.108.131',
                                 port=3306,
                                 user='SM',
                                 passwd='SM-dpbg123.',
                                 db='hpilo',
                                 charset="utf8")
    try:
        with connection.cursor() as cursor:
            sql = "update `ilo_IP` set `flag`= '%d' where `IP` = '%s'" %(flag,ip)
            cursor.execute(sql)
        connection.commit()
    finally:
        connection.close()

"""
try/except面对三个账号报出的相同错误无能为力

"""
a = get_ilo()

for ip in a:
    flag = 0
    print(ip)
    ip = str(ip).lstrip("(").rstrip(")").rstrip(",").strip("/'").lstrip("u").lstrip("/'").strip()
    print(ip)
    if flag == 0:
        try:
            print(ip)
            print("---------------尝试账号(1)登录IP:%s----------------"%(ip))
            ilo = hpilo.Ilo(ip,login="admin",password="iL0!@#123")
            ilo.get_fw_version()
            insert_flag(flag, ip)
        except:
            print("----------该账号无法登陆-----------")
            flag = 2

    if flag == 2:
        try:
            print("---------------尝试账号(2)登录IP:%s----------------"%(ip))
            ilo = hpilo.Ilo(ip,login="Admin",password="iL0!@#123")
            ilo.get_fw_version()
            insert_flag(flag, ip)
        except:
            print("----------该账号无法登陆-----------")
            flag = 3

    if flag == 3:
        try:
            print("---------------尝试账号(3)登录IP:%s----------------"%(ip))
            ilo = hpilo.Ilo(ip, login="Administrator", password="dpbg123.")
            ilo.get_fw_version()
            insert_flag(flag, ip)
        except:
            print("----------该账号无法登陆-----------")
            flag = 4

    if flag == 4:
        try:
            print("---------------尝试账号(4)登录IP:%s----------------"%(ip))
            ilo = hpilo.Ilo(ip, login="Administrator", password="iL0!@#123")
            ilo.get_fw_version()
            insert_flag(flag, ip)
        except:
            print("----------该账号无法登陆-----------")
            flag = 5

    if flag == 5:
        try:
            print("---------------尝试账号(5)登录IP:%s----------------"%(ip))
            ilo = hpilo.Ilo(ip, login="adminstrator", password="dpbg123.")
            ilo.get_fw_version()
            insert_flag(flag, ip)
        except:
            print("----------该账号无法登陆-----------")
            flag = 6

    if flag == 6:
        try:
            print("---------------尝试账号(6)登录IP:%s----------------"%(ip))
            ilo = hpilo.Ilo(ip, login="scadmin", password="iL0!@#123")
            ilo.get_fw_version()
            insert_flag(flag, ip)
        except:
            print("----------该账号无法登陆-----------")
            flag = 7

    if flag == 7:
        try:
            print("---------------尝试账号(7)登录IP:%s----------------"%(ip))
            ilo = hpilo.Ilo(ip, login="scadmin", password="dpbg123.")
            ilo.get_fw_version()
            insert_flag(flag, ip)
        except:
            print("----------该账号无法登陆-----------")
            flag = 8

    if flag == 8:
        try:
            print("---------------尝试账号(8)登录IP:%s----------------" % (ip))
            ilo = hpilo.Ilo(ip, login="MonitorTools", password="ping.p.shen@foxconn.com")
            ilo.get_fw_version()
            insert_flag(flag, ip)
        except:
            print("----------该账号无法登陆-----------")
            flag = 9

    if flag == 9:
        try:
            print("---------------尝试账号(9)登录IP:%s----------------" % (ip))
            ilo = hpilo.Ilo(ip, login="admin", password="password")
            ilo.get_fw_version()
            insert_flag(flag, ip)
        except:
            print("----------该账号无法登陆-----------")
            flag = 10



