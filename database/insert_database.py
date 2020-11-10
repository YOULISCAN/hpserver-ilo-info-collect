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

def update_fan1_info(fan_status=None,fan_speed=None,fan_location=None,fan_label=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'FAN_STATUS': fan_status,'FAN_SPEED': fan_speed,'FAN_LOCATION': fan_location,'FAN_LABEL': fan_label,'IP_ILO': ip}
    print(param)
    with connection.cursor() as cursor:
        cursor.execute('update FANS_INFO set FAN1_STATUS=:FAN_STATUS,FAN1_SPEED=:FAN_SPEED,FAN1_LOCATION=:FAN_LOCATION,FAN1_LABEL=:FAN_LABEL where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()
#
def update_fan2_info(fan_status=None,fan_speed=None,fan_location=None,fan_label=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'FAN_STATUS': fan_status, 'FAN_SPEED': fan_speed ,'FAN_LOCATION': fan_location,'FAN_LABEL': fan_label,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute('update FANS_INFO set FAN2_STATUS=:FAN_STATUS,FAN2_SPEED=:FAN_SPEED,FAN2_LOCATION=:FAN_LOCATION,FAN2_LABEL=:FAN_LABEL where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_fan3_info(fan_status=None,fan_speed=None,fan_location=None,fan_label=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'FAN_STATUS': fan_status, 'FAN_SPEED': fan_speed ,'FAN_LOCATION': fan_location,'FAN_LABEL': fan_label,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute('update FANS_INFO set FAN3_STATUS=:FAN_STATUS,FAN3_SPEED=:FAN_SPEED,FAN3_LOCATION=:FAN_LOCATION,FAN3_LABEL=:FAN_LABEL where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_fan4_info(fan_status=None,fan_speed=None,fan_location=None,fan_label=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'FAN_STATUS': fan_status, 'FAN_SPEED': fan_speed ,'FAN_LOCATION': fan_location,'FAN_LABEL': fan_label,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute('update FANS_INFO set FAN4_STATUS=:FAN_STATUS,FAN4_SPEED=:FAN_SPEED,FAN4_LOCATION=:FAN_LOCATION,FAN4_LABEL=:FAN_LABEL where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_fan5_info(fan_status=None,fan_speed=None,fan_location=None,fan_label=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'FAN_STATUS': fan_status, 'FAN_SPEED': fan_speed ,'FAN_LOCATION': fan_location,'FAN_LABEL': fan_label,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute('update FANS_INFO set FAN5_STATUS=:FAN_STATUS,FAN5_SPEED=:FAN_SPEED,FAN5_LOCATION=:FAN_LOCATION,FAN5_LABEL=:FAN_LABEL where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_fan6_info(fan_status=None,fan_speed=None,fan_location=None,fan_label=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'FAN_STATUS': fan_status, 'FAN_SPEED': fan_speed ,'FAN_LOCATION': fan_location,'FAN_LABEL': fan_label,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute('update FANS_INFO set FAN6_STATUS=:FAN_STATUS,FAN6_SPEED=:FAN_SPEED,FAN6_LOCATION=:FAN_LOCATION,FAN6_LABEL=:FAN_LABEL where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_network1_info(network_name=None,network_status=None,network_ipaddr=None,network_macaddr=None,network_port=None, ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'NETWORK_NAME': network_name,'NETWORK_STATUS': network_status, 'NETWORK_IPADDR': network_ipaddr, 'NETWORK_MACADDR': network_macaddr,
             'NETWORK_PORT': network_port, 'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update NETWORK_INFO set NETWORK_1=:NETWORK_NAME,NETWORK_1_STATUS=:NETWORK_STATUS,NETWORK_1_IPADDR=:NETWORK_IPADDR,NETWORK_1_MACADDR=:network_macaddr,NETWORK_1_PORT=:network_port where IP_ILO=:IP_ILO',
            param)
    connection.commit()
    connection.close()

def update_network2_info(network_name=None,network_status=None,network_ipaddr=None,network_macaddr=None,network_port=None, ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'NETWORK_NAME': network_name, 'NETWORK_STATUS': network_status, 'NETWORK_IPADDR': network_ipaddr, 'NETWORK_MACADDR': network_macaddr,
             'NETWORK_PORT': network_port, 'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update NETWORK_INFO set NETWORK_2=:NETWORK_NAME,NETWORK_2_STATUS=:NETWORK_STATUS,NETWORK_2_IPADDR=:NETWORK_IPADDR,NETWORK_2_MACADDR=:network_macaddr,NETWORK_2_PORT=:network_port where IP_ILO=:IP_ILO',
            param)
    connection.commit()
    connection.close()

def update_network3_info(network_name=None,network_status=None,network_ipaddr=None,network_macaddr=None,network_port=None, ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'NETWORK_NAME': network_name, 'NETWORK_STATUS': network_status, 'NETWORK_IPADDR': network_ipaddr, 'NETWORK_MACADDR': network_macaddr,
             'NETWORK_PORT': network_port, 'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update NETWORK_INFO set NETWORK_3=:NETWORK_NAME,NETWORK_3_STATUS=:NETWORK_STATUS,NETWORK_3_IPADDR=:NETWORK_IPADDR,NETWORK_3_MACADDR=:network_macaddr,NETWORK_3_PORT=:network_port where IP_ILO=:IP_ILO',
            param)
    connection.commit()
    connection.close()

def update_network4_info(network_name=None,network_status=None,network_ipaddr=None,network_macaddr=None,network_port=None, ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'NETWORK_NAME': network_name, 'NETWORK_STATUS': network_status, 'NETWORK_IPADDR': network_ipaddr, 'NETWORK_MACADDR': network_macaddr,
             'NETWORK_PORT': network_port, 'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update NETWORK_INFO set NETWORK_4=:NETWORK_NAME,NETWORK_4_STATUS=:NETWORK_STATUS,NETWORK_4_IPADDR=:NETWORK_IPADDR,NETWORK_4_MACADDR=:network_macaddr,NETWORK_4_PORT=:network_port where IP_ILO=:IP_ILO',
            param)
    connection.commit()
    connection.close()

def update_network5_info(network_name=None,network_status=None,network_ipaddr=None,network_macaddr=None,network_port=None, ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'NETWORK_NAME': network_name, 'NETWORK_STATUS': network_status, 'NETWORK_IPADDR': network_ipaddr, 'NETWORK_MACADDR': network_macaddr,
             'NETWORK_PORT': network_port, 'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update NETWORK_INFO set NETWORK_5=:NETWORK_NAME,NETWORK_5_STATUS=:NETWORK_STATUS,NETWORK_5_IPADDR=:NETWORK_IPADDR,NETWORK_5_MACADDR=:network_macaddr,NETWORK_5_PORT=:network_port where IP_ILO=:IP_ILO',
            param)
    connection.commit()
    connection.close()

def update_network6_info(network_name=None,network_status=None,network_ipaddr=None,network_macaddr=None,network_port=None, ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'NETWORK_NAME': network_name, 'NETWORK_STATUS': network_status,'NETWORK_IPADDR': network_ipaddr, 'NETWORK_MACADDR': network_macaddr,
             'NETWORK_PORT': network_port, 'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update NETWORK_INFO set NETWORK_6=:NETWORK_NAME,NETWORK_6_STATUS=:NETWORK_STATUS,NETWORK_6_IPADDR=:NETWORK_IPADDR,NETWORK_6_MACADDR=:network_macaddr,NETWORK_6_PORT=:network_port where IP_ILO=:IP_ILO',
            param)
    connection.commit()
    connection.close()

def update_network7_info(network_name=None,network_status=None,network_ipaddr=None,network_macaddr=None,network_port=None, ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'NETWORK_NAME': network_name, 'NETWORK_STATUS': network_status,'NETWORK_IPADDR': network_ipaddr, 'NETWORK_MACADDR': network_macaddr,
             'NETWORK_PORT': network_port, 'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update NETWORK_INFO set NETWORK_7=:NETWORK_NAME,NETWORK_7_STATUS=:NETWORK_STATUS,NETWORK_7_IPADDR=:NETWORK_IPADDR,NETWORK_7_MACADDR=:network_macaddr,NETWORK_7_PORT=:network_port where IP_ILO=:IP_ILO',
            param)
    connection.commit()
    connection.close()

def update_network8_info(network_name=None,network_status=None,network_ipaddr=None,network_macaddr=None,network_port=None, ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'NETWORK_NAME': network_name, 'NETWORK_STATUS': network_status,'NETWORK_IPADDR': network_ipaddr, 'NETWORK_MACADDR': network_macaddr,
             'NETWORK_PORT': network_port, 'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update NETWORK_INFO set NETWORK_8=:NETWORK_NAME,NETWORK_8_STATUS=:NETWORK_STATUS,NETWORK_8_IPADDR=:NETWORK_IPADDR,NETWORK_8_MACADDR=:network_macaddr,NETWORK_8_PORT=:network_port where IP_ILO=:IP_ILO',
            param)
    connection.commit()
    connection.close()

def update_network9_info(network_name=None,network_status=None,network_ipaddr=None,network_macaddr=None,network_port=None, ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'NETWORK_NAME': network_name, 'NETWORK_STATUS': network_status,'NETWORK_IPADDR': network_ipaddr, 'NETWORK_MACADDR': network_macaddr,
             'NETWORK_PORT': network_port, 'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update NETWORK_INFO set NETWORK_9=:NETWORK_NAME,NETWORK_9_STATUS=:NETWORK_STATUS,NETWORK_9_IPADDR=:NETWORK_IPADDR,NETWORK_9_MACADDR=:network_macaddr,NETWORK_9_PORT=:network_port where IP_ILO=:IP_ILO',
            param)
    connection.commit()
    connection.close()

def update_network10_info(network_name=None,network_status=None,network_ipaddr=None,network_macaddr=None,network_port=None, ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'NETWORK_NAME': network_name, 'NETWORK_STATUS': network_status,'NETWORK_IPADDR': network_ipaddr, 'NETWORK_MACADDR': network_macaddr,
             'NETWORK_PORT': network_port, 'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update NETWORK_INFO set NETWORK_10=:NETWORK_NAME,NETWORK_10_STATUS=:NETWORK_STATUS,NETWORK_10_IPADDR=:NETWORK_IPADDR,NETWORK_10_MACADDR=:network_macaddr,NETWORK_10_PORT=:network_port where IP_ILO=:IP_ILO',
            param)
    connection.commit()
    connection.close()