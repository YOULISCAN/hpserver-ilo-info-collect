#!/usr/bin/python
import hpilo
import multiprocessing
import os

def get_login_info(url):
    login_info = []
    with open(url,'r') as file:
        for info in file.readlines():
            login_info.append(tuple(info.rstrip('\n').split()))
    return login_info

def AddIloUser(args):
    ilo_ip, username, password = args
    ilo = hpilo.Ilo(ilo_ip, username, password)
    ilo.add_user(virtual_media_priv=False, reset_server_priv=False, config_ilo_priv=True,
                 user_login="elk", remote_cons_priv=False, admin_priv=False, password="passwd", user_name="username")


if __name__ == '__main__':
    url = os.getcwd() + '/ilo_login_info.txt'
    ilos_login_info = get_login_info(url)
    print ilos_login_info
    multiprocessing.Pool().map(AddIloUser, ilos_login_info)