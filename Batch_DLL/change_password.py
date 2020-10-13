# -*- coding: utf-8 -*-


import hpilo


def IP_list():

    with open('change_password_IP', 'r') as f:
        for i in f.readlines():
            ip = i.strip()
            login_password(ip)

def login_password(ip):

    ilo = hpilo.Ilo(ip,login='Administrator',password='dpbg123.')
    try:
        ilo.add_user(user_login='admin',user_name='admin',password='iL0!@#123',admin_priv=True,reset_server_priv=True,virtual_media_priv=True)
    except  hpilo.IloError:
        ilo.mod_user(user_login='admin',user_name='admin',password='iL0!@#123',admin_priv=True,reset_server_priv=True,virtual_media_priv=True)
    finally:
        print("over")

IP_list()