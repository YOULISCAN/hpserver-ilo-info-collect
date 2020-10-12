# -*- coding: utf-8 -*-

import hpilo,hpilo_fw



ilo = hpilo.Ilo('10.172.100.190',login='admin',password='iL0!@#123')
#hpilo_fw.config(mirror='hpserver-ilo-info-collect/Batch_DLL/')
ilo.update_rib_firmware(filename='ilo5_230.bin', progress='print_progress')
