# -*- coding: utf-8 -*-


import hpilo
import database.login_database as db

def IP_list():

    with open('change_password_IP', 'r') as f:
        for i in f.readlines():
            ip = i.strip()
            login_password(ip)

def login_password(ip):

    ilo = hpilo.Ilo(ip,login='admin',password='iL0!@#123')
    try:
        ilo.add_user(user_login='admin',user_name='admin',password='iL0!@#123',admin_priv=True,reset_server_priv=True,virtual_media_priv=True)
    except  hpilo.IloError:
        ilo.mod_user(user_login='admin',user_name='admin',password='iL0!@#123',admin_priv=True,reset_server_priv=True,virtual_media_priv=True)
    finally:
        print("over")
def add_account():
    sql = 'select IP_ILO from ILO_INFO'

    g = db.connection_database(sql)
    try:
        while True:
            ip = g.next().lstrip("'").rstrip("'")
            try:
                ilo = hpilo.Ilo(ip, login='admin', password='iL0!@#123')
                ilo.add_user(user_login='MonitorTools', user_name='MonitorTools', password='ping.p.shen@foxconn.com',
                             remote_cons_priv=False, config_ilo_priv=False)
            except hpilo.IloLoginFailed:
                print("该IP {} 为DBA设备".format(ip))
            except hpilo.IloError:
                print("该IP {} 账号已存在".format(ip))
            finally:
                pass
    except StopIteration:
        pass
    finally:
        pass

add_account()