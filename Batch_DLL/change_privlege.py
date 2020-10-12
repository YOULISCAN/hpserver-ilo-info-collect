# -*- coding: utf-8 -*-

import hpilo

ilo = hpilo.Ilo('10.172.100.137',login='Administrator',password='dpbg123.')

ilo.mod_user(user_login='admin',admin_priv=True,reset_server_priv=True,virtual_media_priv=True)