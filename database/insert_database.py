# -*- coding: utf-8 -*-

import cx_Oracle



def update_fw_info(product_name=None, server_name=None, ilo_model=None, fw_version=None, fw_data=None,ip=None):  #修改ILO_INFO表信息
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'ASSETS_MODEL': product_name,'ASSETS_NAME': server_name ,'ILO_MODEL':ilo_model,'ILO_FW_VERSION':fw_version ,'ILO_FW_DATA':fw_data,'IP_ILO':ip}
    print(param)
    with connection.cursor() as cursor:
         cursor.execute('update ILO_INFO set ASSETS_MODEL=:ASSETS_MODEL,ASSETS_NAME=:ASSETS_NAME,ILO_MODEL=:ILO_MODEL,ILO_FW_VERSION=:ILO_FW_VERSION,ILO_FW_DATA=:ILO_FW_DATA where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_server_general_info(bios_hardware=None,fans=None,temperature=None,power_supplies=None,battery=None,processor=None,memory=None,network=None,storage=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'BIOS_HARDWARE': bios_hardware, 'FANS': fans, 'TEMPERATURE': temperature,
             'POWER_SUPPLIES': power_supplies, 'BATTERY': battery, 'PROCESSOR': processor,
             'MEMORY': memory, 'NETWORK':network,'STORAGE':storage,'IP_ILO':ip}
    print(param)
    with connection.cursor() as cursor:
        cursor.execute('update ILO_INFO set BIOS_HARDWARE=:BIOS_HARDWARE,FANS=:FANS,TEMPERATURE=:TEMPERATURE,POWER_SUPPLIES=:POWER_SUPPLIES,BATTERY=:BATTERY,PROCESSOR=:PROCESSOR,MEMORY=:MEMORY,NETWORK=:NETWORK,STORAGE=:STORAGE where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()