# -*- coding: utf-8 -*-

import cx_Oracle
import hpilo
ilo = hpilo.Ilo('10.172.100.190',login='admin',password='iL0!@#123')
ilo.mod_network_settings(sntp_server1='10.172.113.1',sntp_server2='10.173.173.163',timezone='Asia/Taipei')