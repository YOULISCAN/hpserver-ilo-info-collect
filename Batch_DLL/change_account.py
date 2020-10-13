# -*- coding: utf-8 -*-


import hpilo


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
def add_account(ip):
    ilo = hpilo.Ilo(ip,login='admin',password='iL0!@#123')
    try:
        ilo.add_user(user_login='MonitorTools',user_name='MonitorTools',password='ping.p.shen@foxconn.com')
    except hpilo.IloError:
        print("{}对应的账号已存在".format(ip))
    finally:
        pass
IP_list()