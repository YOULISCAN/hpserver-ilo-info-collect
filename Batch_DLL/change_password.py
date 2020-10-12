# -*- coding: utf-8 -*-


import hpilo

with open('change_password_IP','r') as f:
    ip = f.readline().strip()



# ilo = hpilo.Ilo('10.172.100.137',login='Administrator',password='dpbg123.')
#
# ilo.add_user(user_login='admin',user_name='admin',password='iL0!@#123')
