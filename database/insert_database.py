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

def update_memory1_info(memory=None,socket=None,socket_status=None,socket_hp_smart=None,socket_part_number=None,socket_type=None,socket_size=None,socket_frequency=None,socket_minimum_voltage=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'MEMORY': memory, 'SOCKET': socket, 'SOCKET_STATUS': socket_status,
             'SOCKET_PART_NUMBER': socket_part_number, 'SOCKET_TYPE': socket_type, 'SOCKET_SIZE': socket_size,'SOCKET_FREQUENCY': socket_frequency,'SOCKET_MINIMUM_VOLTAGE': socket_minimum_voltage,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set MEMORY_1=:memory,SOCKET_1=:socket,SOCKET_1_STATUS=:socket_status,SOCKET_1_PART_NUMBER=:socket_part_number,SOCKET_1_TYPE=:socket_type,SOCKET_1_SIZE=:socket_size,SOCKET_1_FREQUENCY=:socket_frequency,SOCKET_1_MINIMUM_VOLTAGE=:socket_minimum_voltage where IP_ILO=:IP_ILO',
            param)
    connection.commit()
    connection.close()

def update_memory2_info(memory=None,socket=None,socket_status=None,socket_hp_smart=None,socket_part_number=None,socket_type=None,socket_size=None,socket_frequency=None,socket_minimum_voltage=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,
             'SOCKET_PART_NUMBER': socket_part_number, 'SOCKET_TYPE': socket_type, 'SOCKET_SIZE': socket_size,
             'SOCKET_FREQUENCY': socket_frequency, 'SOCKET_MINIMUM_VOLTAGE': socket_minimum_voltage,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET_2=:socket,SOCKET_2_STATUS=:socket_status,SOCKET_2_PART_NUMBER=:socket_part_number,SOCKET_2_TYPE=:socket_type,SOCKET_2_SIZE=:socket_size,SOCKET_2_FREQUENCY=:socket_frequency,SOCKET_2_MINIMUM_VOLTAGE=:socket_minimum_voltage where IP_ILO=:IP_ILO'
,param)
    connection.commit()
    connection.close()

def update_memory3_info(memory=None,socket=None,socket_status=None,socket_hp_smart=None,socket_part_number=None,socket_type=None,socket_size=None,socket_frequency=None,socket_minimum_voltage=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,
             'SOCKET_PART_NUMBER': socket_part_number, 'SOCKET_TYPE': socket_type, 'SOCKET_SIZE': socket_size,
             'SOCKET_FREQUENCY': socket_frequency, 'SOCKET_MINIMUM_VOLTAGE': socket_minimum_voltage,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET_3=:socket,SOCKET_3_STATUS=:socket_status,SOCKET_3_PART_NUMBER=:socket_part_number,SOCKET_3_TYPE=:socket_type,SOCKET_3_SIZE=:socket_size,SOCKET_3_FREQUENCY=:socket_frequency,SOCKET_3_MINIMUM_VOLTAGE=:socket_minimum_voltage where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_memory4_info(memory=None,socket=None,socket_status=None,socket_hp_smart=None,socket_part_number=None,socket_type=None,socket_size=None,socket_frequency=None,socket_minimum_voltage=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,
             'SOCKET_PART_NUMBER': socket_part_number, 'SOCKET_TYPE': socket_type, 'SOCKET_SIZE': socket_size,
             'SOCKET_FREQUENCY': socket_frequency, 'SOCKET_MINIMUM_VOLTAGE': socket_minimum_voltage,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET_4=:socket,SOCKET_4_STATUS=:socket_status,SOCKET_4_PART_NUMBER=:socket_part_number,SOCKET_4_TYPE=:socket_type,SOCKET_4_SIZE=:socket_size,SOCKET_4_FREQUENCY=:socket_frequency,SOCKET_4_MINIMUM_VOLTAGE=:socket_minimum_voltage where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()
def update_memory5_info(memory=None,socket=None,socket_status=None,socket_hp_smart=None,socket_part_number=None,socket_type=None,socket_size=None,socket_frequency=None,socket_minimum_voltage=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,
             'SOCKET_PART_NUMBER': socket_part_number, 'SOCKET_TYPE': socket_type, 'SOCKET_SIZE': socket_size,
             'SOCKET_FREQUENCY': socket_frequency, 'SOCKET_MINIMUM_VOLTAGE': socket_minimum_voltage,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET_5=:socket,SOCKET_5_STATUS=:socket_status,SOCKET_5_PART_NUMBER=:socket_part_number,SOCKET_5_TYPE=:socket_type,SOCKET_5_SIZE=:socket_size,SOCKET_5_FREQUENCY=:socket_frequency,SOCKET_5_MINIMUM_VOLTAGE=:socket_minimum_voltage where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_memory6_info(memory=None,socket=None,socket_status=None,socket_part_number=None,socket_type=None,socket_size=None,socket_frequency=None,socket_minimum_voltage=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,
             'SOCKET_PART_NUMBER': socket_part_number, 'SOCKET_TYPE': socket_type, 'SOCKET_SIZE': socket_size,
             'SOCKET_FREQUENCY': socket_frequency, 'SOCKET_MINIMUM_VOLTAGE': socket_minimum_voltage,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET_6=:socket,SOCKET_6_STATUS=:socket_status,SOCKET_6_PART_NUMBER=:socket_part_number,SOCKET_6_TYPE=:socket_type,SOCKET_6_SIZE=:socket_size,SOCKET_6_FREQUENCY=:socket_frequency,SOCKET_6_MINIMUM_VOLTAGE=:socket_minimum_voltage where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_memory7_info(memory=None,socket=None,socket_status=None,socket_part_number=None,socket_type=None,socket_size=None,socket_frequency=None,socket_minimum_voltage=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,
             'SOCKET_PART_NUMBER': socket_part_number, 'SOCKET_TYPE': socket_type, 'SOCKET_SIZE': socket_size,
             'SOCKET_FREQUENCY': socket_frequency, 'SOCKET_MINIMUM_VOLTAGE': socket_minimum_voltage,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET_7=:socket,SOCKET_7_STATUS=:socket_status,SOCKET_7_PART_NUMBER=:socket_part_number,SOCKET_7_TYPE=:socket_type,SOCKET_7_SIZE=:socket_size,SOCKET_7_FREQUENCY=:socket_frequency,SOCKET_7_MINIMUM_VOLTAGE=:socket_minimum_voltage where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_memory8_info(memory=None,socket=None,socket_status=None,socket_part_number=None,socket_type=None,socket_size=None,socket_frequency=None,socket_minimum_voltage=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,
             'SOCKET_PART_NUMBER': socket_part_number, 'SOCKET_TYPE': socket_type, 'SOCKET_SIZE': socket_size,
             'SOCKET_FREQUENCY': socket_frequency, 'SOCKET_MINIMUM_VOLTAGE': socket_minimum_voltage,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET_8=:socket,SOCKET_8_STATUS=:socket_status,SOCKET_8_PART_NUMBER=:socket_part_number,SOCKET_8_TYPE=:socket_type,SOCKET_8_SIZE=:socket_size,SOCKET_8_FREQUENCY=:socket_frequency,SOCKET_8_MINIMUM_VOLTAGE=:socket_minimum_voltage where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_memory9_info(memory=None,socket=None,socket_status=None,socket_part_number=None,socket_type=None,socket_size=None,socket_frequency=None,socket_minimum_voltage=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,
             'SOCKET_PART_NUMBER': socket_part_number, 'SOCKET_TYPE': socket_type, 'SOCKET_SIZE': socket_size,
             'SOCKET_FREQUENCY': socket_frequency, 'SOCKET_MINIMUM_VOLTAGE': socket_minimum_voltage,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET_9=:socket,SOCKET_9_STATUS=:socket_status,SOCKET_9_PART_NUMBER=:socket_part_number,SOCKET_9_TYPE=:socket_type,SOCKET_9_SIZE=:socket_size,SOCKET_9_FREQUENCY=:socket_frequency,SOCKET_9_MINIMUM_VOLTAGE=:socket_minimum_voltage where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_memory10_info(memory=None,socket=None,socket_status=None,socket_part_number=None,socket_type=None,socket_size=None,socket_frequency=None,socket_minimum_voltage=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,
             'SOCKET_PART_NUMBER': socket_part_number, 'SOCKET_TYPE': socket_type, 'SOCKET_SIZE': socket_size,
             'SOCKET_FREQUENCY': socket_frequency, 'SOCKET_MINIMUM_VOLTAGE': socket_minimum_voltage,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET_10=:socket,SOCKET_10_STATUS=:socket_status,SOCKET_10_PART_NUMBER=:socket_part_number,SOCKET_10_TYPE=:socket_type,SOCKET_10_SIZE=:socket_size,SOCKET_10_FREQUENCY=:socket_frequency,SOCKET_10_MINIMUM_VOLTAGE=:socket_minimum_voltage where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_memory11_info(memory=None,socket=None,socket_status=None,socket_part_number=None,socket_type=None,socket_size=None,socket_frequency=None,socket_minimum_voltage=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,
             'SOCKET_PART_NUMBER': socket_part_number, 'SOCKET_TYPE': socket_type, 'SOCKET_SIZE': socket_size,
             'SOCKET_FREQUENCY': socket_frequency, 'SOCKET_MINIMUM_VOLTAGE': socket_minimum_voltage,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET_11=:socket,SOCKET_11_STATUS=:socket_status,SOCKET_11_PART_NUMBER=:socket_part_number,SOCKET_11_TYPE=:socket_type,SOCKET_11_SIZE=:socket_size,SOCKET_11_FREQUENCY=:socket_frequency,SOCKET_11_MINIMUM_VOLTAGE=:socket_minimum_voltage where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_memory12_info(memory=None,socket=None,socket_status=None,socket_part_number=None,socket_type=None,socket_size=None,socket_frequency=None,socket_minimum_voltage=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,
             'SOCKET_PART_NUMBER': socket_part_number, 'SOCKET_TYPE': socket_type, 'SOCKET_SIZE': socket_size,
             'SOCKET_FREQUENCY': socket_frequency, 'SOCKET_MINIMUM_VOLTAGE': socket_minimum_voltage,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET_12=:socket,SOCKET_12_STATUS=:socket_status,SOCKET_12_PART_NUMBER=:socket_part_number,SOCKET_12_TYPE=:socket_type,SOCKET_12_SIZE=:socket_size,SOCKET_12_FREQUENCY=:socket_frequency,SOCKET_12_MINIMUM_VOLTAGE=:socket_minimum_voltage where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_memory2_1_info(memory=None,socket=None,socket_status=None,socket_part_number=None,socket_type=None,socket_size=None,socket_frequency=None,socket_minimum_voltage=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'MEMORY': memory, 'SOCKET': socket, 'SOCKET_STATUS': socket_status,
             'SOCKET_PART_NUMBER': socket_part_number, 'SOCKET_TYPE': socket_type, 'SOCKET_SIZE': socket_size,'SOCKET_FREQUENCY': socket_frequency,'SOCKET_MINIMUM_VOLTAGE': socket_minimum_voltage,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set MEMORY_2=:memory,SOCKET2_1=:socket,SOCKET2_1_STATUS=:socket_status,SOCKET2_1_PART_NUMBER=:socket_part_number,SOCKET2_1_TYPE=:socket_type,SOCKET2_1_SIZE=:socket_size,SOCKET2_1_FREQUENCY=:socket_frequency,SOCKET2_1_MINIMUM_VOLTAGE=:socket_minimum_voltage where IP_ILO=:IP_ILO',
            param)
    connection.commit()
    connection.close()

def update_memory2_2_info(memory=None,socket=None,socket_status=None,socket_hp_smart=None,socket_part_number=None,socket_type=None,socket_size=None,socket_frequency=None,socket_minimum_voltage=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,
             'SOCKET_PART_NUMBER': socket_part_number, 'SOCKET_TYPE': socket_type, 'SOCKET_SIZE': socket_size,
             'SOCKET_FREQUENCY': socket_frequency,'SOCKET_MINIMUM_VOLTAGE': socket_minimum_voltage, 'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET2_2=:socket,SOCKET2_2_STATUS=:socket_status,SOCKET2_2_PART_NUMBER=:socket_part_number,SOCKET2_2_TYPE=:socket_type,SOCKET2_2_SIZE=:socket_size,SOCKET2_2_FREQUENCY=:socket_frequency,SOCKET2_2_MINIMUM_VOLTAGE=:socket_minimum_voltage where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_memory2_3_info(memory=None,socket=None,socket_status=None,socket_hp_smart=None,socket_part_number=None,socket_type=None,socket_size=None,socket_frequency=None,socket_minimum_voltage=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,
             'SOCKET_PART_NUMBER': socket_part_number, 'SOCKET_TYPE': socket_type, 'SOCKET_SIZE': socket_size,
             'SOCKET_FREQUENCY': socket_frequency, 'SOCKET_MINIMUM_VOLTAGE': socket_minimum_voltage,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET2_3=:socket,SOCKET2_3_STATUS=:socket_status,SOCKET2_3_PART_NUMBER=:socket_part_number,SOCKET2_3_TYPE=:socket_type,SOCKET2_3_SIZE=:socket_size,SOCKET2_3_FREQUENCY=:socket_frequency,SOCKET2_3_MINIMUM_VOLTAGE=:socket_minimum_voltage where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_memory2_4_info(memory=None,socket=None,socket_status=None,socket_hp_smart=None,socket_part_number=None,socket_type=None,socket_size=None,socket_frequency=None,socket_minimum_voltage=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,
             'SOCKET_PART_NUMBER': socket_part_number, 'SOCKET_TYPE': socket_type, 'SOCKET_SIZE': socket_size,
             'SOCKET_FREQUENCY': socket_frequency, 'SOCKET_MINIMUM_VOLTAGE': socket_minimum_voltage,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET2_4=:socket,SOCKET2_4_STATUS=:socket_status,SOCKET2_4_PART_NUMBER=:socket_part_number,SOCKET2_4_TYPE=:socket_type,SOCKET2_4_SIZE=:socket_size,SOCKET2_4_FREQUENCY=:socket_frequency,SOCKET2_4_MINIMUM_VOLTAGE=:socket_minimum_voltage where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()
def update_memory2_5_info(memory=None,socket=None,socket_status=None,socket_part_number=None,socket_type=None,socket_size=None,socket_frequency=None,socket_minimum_voltage=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,
             'SOCKET_PART_NUMBER': socket_part_number, 'SOCKET_TYPE': socket_type, 'SOCKET_SIZE': socket_size,
             'SOCKET_FREQUENCY': socket_frequency, 'SOCKET_MINIMUM_VOLTAGE': socket_minimum_voltage,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET2_5=:socket,SOCKET2_5_STATUS=:socket_status,SOCKET2_5_PART_NUMBER=:socket_part_number,SOCKET2_5_TYPE=:socket_type,SOCKET2_5_SIZE=:socket_size,SOCKET2_5_FREQUENCY=:socket_frequency,SOCKET2_5_MINIMUM_VOLTAGE=:socket_minimum_voltage where IP_ILO=:IP_ILO',
            param)
    connection.commit()
    connection.close()

def update_memory2_6_info(memory=None,socket=None,socket_status=None,socket_part_number=None,socket_type=None,socket_size=None,socket_frequency=None,socket_minimum_voltage=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,
             'SOCKET_PART_NUMBER': socket_part_number, 'SOCKET_TYPE': socket_type, 'SOCKET_SIZE': socket_size,
             'SOCKET_FREQUENCY': socket_frequency,'SOCKET_MINIMUM_VOLTAGE': socket_minimum_voltage, 'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET2_6=:socket,SOCKET2_6_STATUS=:socket_status,SOCKET2_6_PART_NUMBER=:socket_part_number,SOCKET2_6_TYPE=:socket_type,SOCKET2_6_SIZE=:socket_size,SOCKET2_6_FREQUENCY=:socket_frequency,SOCKET2_6_MINIMUM_VOLTAGE=:socket_minimum_voltage where IP_ILO=:IP_ILO',
            param)
    connection.commit()
    connection.close()

def update_memory2_7_info(memory=None,socket=None,socket_status=None,socket_part_number=None,socket_type=None,socket_size=None,socket_frequency=None,socket_minimum_voltage=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,
             'SOCKET_PART_NUMBER': socket_part_number, 'SOCKET_TYPE': socket_type, 'SOCKET_SIZE': socket_size,
             'SOCKET_FREQUENCY': socket_frequency,'SOCKET_MINIMUM_VOLTAGE': socket_minimum_voltage, 'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET2_7=:socket,SOCKET2_7_STATUS=:socket_status,SOCKET2_7_PART_NUMBER=:socket_part_number,SOCKET2_7_TYPE=:socket_type,SOCKET2_7_SIZE=:socket_size,SOCKET2_7_FREQUENCY=:socket_frequency,SOCKET2_7_MINIMUM_VOLTAGE=:socket_minimum_voltage where IP_ILO=:IP_ILO',
            param)
    connection.commit()
    connection.close()

def update_memory2_8_info(memory=None,socket=None,socket_status=None,socket_part_number=None,socket_type=None,socket_size=None,socket_frequency=None,socket_minimum_voltage=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,
             'SOCKET_PART_NUMBER': socket_part_number, 'SOCKET_TYPE': socket_type, 'SOCKET_SIZE': socket_size,
             'SOCKET_FREQUENCY': socket_frequency,'SOCKET_MINIMUM_VOLTAGE': socket_minimum_voltage, 'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET2_8=:socket,SOCKET2_8_STATUS=:socket_status,SOCKET2_8_PART_NUMBER=:socket_part_number,SOCKET2_8_TYPE=:socket_type,SOCKET2_8_SIZE=:socket_size,SOCKET2_8_FREQUENCY=:socket_frequency,SOCKET2_8_MINIMUM_VOLTAGE=:socket_minimum_voltage where IP_ILO=:IP_ILO',
            param)
    connection.commit()
    connection.close()

def update_memory2_9_info(memory=None,socket=None,socket_status=None,socket_part_number=None,socket_type=None,socket_size=None,socket_frequency=None,socket_minimum_voltage=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,
             'SOCKET_PART_NUMBER': socket_part_number, 'SOCKET_TYPE': socket_type, 'SOCKET_SIZE': socket_size,
             'SOCKET_FREQUENCY': socket_frequency,'SOCKET_MINIMUM_VOLTAGE': socket_minimum_voltage, 'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET2_9=:socket,SOCKET2_9_STATUS=:socket_status,SOCKET2_9_PART_NUMBER=:socket_part_number,SOCKET2_9_TYPE=:socket_type,SOCKET2_9_SIZE=:socket_size,SOCKET2_9_FREQUENCY=:socket_frequency,SOCKET2_9_MINIMUM_VOLTAGE=:socket_minimum_voltage where IP_ILO=:IP_ILO',
            param)
    connection.commit()
    connection.close()

def update_memory2_10_info(memory=None,socket=None,socket_status=None,socket_part_number=None,socket_type=None,socket_size=None,socket_frequency=None,socket_minimum_voltage=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,
             'SOCKET_PART_NUMBER': socket_part_number, 'SOCKET_TYPE': socket_type, 'SOCKET_SIZE': socket_size,
             'SOCKET_FREQUENCY': socket_frequency, 'SOCKET_MINIMUM_VOLTAGE': socket_minimum_voltage,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET2_10=:socket,SOCKET2_10_STATUS=:socket_status,SOCKET2_10_PART_NUMBER=:socket_part_number,SOCKET2_10_TYPE=:socket_type,SOCKET2_10_SIZE=:socket_size,SOCKET2_10_FREQUENCY=:socket_frequency,SOCKET2_10_MINIMUM_VOLTAGE=:socket_minimum_voltage where IP_ILO=:IP_ILO',
            param)
    connection.commit()
    connection.close()

def update_memory2_11_info(memory=None,socket=None,socket_status=None,socket_part_number=None,socket_type=None,socket_size=None,socket_frequency=None,socket_minimum_voltage=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,
             'SOCKET_PART_NUMBER': socket_part_number, 'SOCKET_TYPE': socket_type, 'SOCKET_SIZE': socket_size,
             'SOCKET_FREQUENCY': socket_frequency, 'SOCKET_MINIMUM_VOLTAGE': socket_minimum_voltage,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET2_11=:socket,SOCKET2_11_STATUS=:socket_status,SOCKET2_11_PART_NUMBER=:socket_part_number,SOCKET2_11_TYPE=:socket_type,SOCKET2_11_SIZE=:socket_size,SOCKET2_11_FREQUENCY=:socket_frequency,SOCKET2_11_MINIMUM_VOLTAGE=:socket_minimum_voltage where IP_ILO=:IP_ILO',
            param)
    connection.commit()
    connection.close()

def update_memory2_12_info(memory=None,socket=None,socket_status=None,socket_part_number=None,socket_type=None,socket_size=None,socket_frequency=None,socket_minimum_voltage=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,
             'SOCKET_PART_NUMBER': socket_part_number, 'SOCKET_TYPE': socket_type, 'SOCKET_SIZE': socket_size,
             'SOCKET_FREQUENCY': socket_frequency, 'SOCKET_MINIMUM_VOLTAGE': socket_minimum_voltage,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET2_12=:socket,SOCKET2_12_STATUS=:socket_status,SOCKET2_12_PART_NUMBER=:socket_part_number,SOCKET2_12_TYPE=:socket_type,SOCKET2_12_SIZE=:socket_size,SOCKET2_12_FREQUENCY=:socket_frequency,SOCKET2_12_MINIMUM_VOLTAGE=:socket_minimum_voltage where IP_ILO=:IP_ILO',
            param)
    connection.commit()
    connection.close()

def update_memory1_ilo3_info(socket=None,socket_status=None,socket_size=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,'SOCKET_SIZE': socket_size,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET_1=:socket,SOCKET_1_STATUS=:socket_status,SOCKET_1_SIZE=:socket_size where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_memory2_ilo3_info(socket=None,socket_status=None,socket_size=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,'SOCKET_SIZE': socket_size,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET_2=:socket,SOCKET_2_STATUS=:socket_status,SOCKET_2_SIZE=:socket_size where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_memory3_ilo3_info(socket=None,socket_status=None,socket_size=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,'SOCKET_SIZE': socket_size,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET_3=:socket,SOCKET_3_STATUS=:socket_status,SOCKET_3_SIZE=:socket_size, where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_memory4_ilo3_info(socket=None,socket_status=None,socket_size=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,'SOCKET_SIZE': socket_size,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET_4=:socket,SOCKET_4_STATUS=:socket_status,SOCKET_4_SIZE=:socket_size where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()
def update_memory5_ilo3_info(socket=None,socket_status=None,socket_size=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,'SOCKET_SIZE': socket_size, 'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET_5=:socket,SOCKET_5_STATUS=:socket_status,SOCKET_5_SIZE=:socket_size where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_memory6_ilo3_info(socket=None,socket_status=None,socket_size=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,'SOCKET_SIZE': socket_size,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET_6=:socket,SOCKET_6_STATUS=:socket_status,SOCKET_6_SIZE=:socket_size where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_memory7_ilo3_info(socket=None,socket_status=None,socket_size=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,'SOCKET_SIZE': socket_size, 'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET_7=:socket,SOCKET_7_STATUS=:socket_status,SOCKET_7_SIZE=:socket_size where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_memory8_ilo3_info(socket=None,socket_status=None,socket_size=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,'SOCKET_SIZE': socket_size,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET_8=:socket,SOCKET_8_STATUS=:socket_status,SOCKET_8_SIZE=:socket_size where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_memory9_ilo3_info(socket=None,socket_status=None,socket_size=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status, 'SOCKET_SIZE': socket_size, 'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET_9=:socket,SOCKET_9_STATUS=:socket_status,SOCKET_9_SIZE=:socket_size where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_memory2_1_ilo3_info(socket=None,socket_status=None,socket_size=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,'SOCKET_SIZE': socket_size,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET2_1=:socket,SOCKET2_1_STATUS=:socket_status,SOCKET2_1_SIZE=:socket_size where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_memory2_2_ilo3_info(socket=None,socket_status=None,socket_size=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,'SOCKET_SIZE': socket_size,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET2_2=:socket,SOCKET2_2_STATUS=:socket_status,SOCKET2_2_SIZE=:socket_size where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_memory2_3_ilo3_info(socket=None,socket_status=None,socket_size=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,'SOCKET_SIZE': socket_size,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET2_3=:socket,SOCKET2_3_STATUS=:socket_status,SOCKET2_3_SIZE=:socket_size, where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_memory2_4_ilo3_info(socket=None,socket_status=None,socket_size=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,'SOCKET_SIZE': socket_size,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET2_4=:socket,SOCKET2_4_STATUS=:socket_status,SOCKET2_4_SIZE=:socket_size where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()
def update_memory2_5_ilo3_info(socket=None,socket_status=None,socket_size=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,'SOCKET_SIZE': socket_size, 'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET2_5=:socket,SOCKET2_5_STATUS=:socket_status,SOCKET2_5_SIZE=:socket_size where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_memory2_6_ilo3_info(socket=None,socket_status=None,socket_size=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,'SOCKET_SIZE': socket_size,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET2_6=:socket,SOCKET2_6_STATUS=:socket_status,SOCKET2_6_SIZE=:socket_size where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_memory2_7_ilo3_info(socket=None,socket_status=None,socket_size=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,'SOCKET_SIZE': socket_size, 'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET2_7=:socket,SOCKET2_7_STATUS=:socket_status,SOCKET2_7_SIZE=:socket_size where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_memory2_8_ilo3_info(socket=None,socket_status=None,socket_size=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,'SOCKET_SIZE': socket_size,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET2_8=:socket,SOCKET2_8_STATUS=:socket_status,SOCKET2_8_SIZE=:socket_size where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_memory2_9_ilo3_info(socket=None,socket_status=None,socket_size=None,ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status, 'SOCKET_SIZE': socket_size, 'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET2_9=:socket,SOCKET2_9_STATUS=:socket_status,SOCKET2_9_SIZE=:socket_size where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def update_storage_1_info(logical_drive=None,logical_drive_status=None,logical_drive_capacity=None,logical_drive_tolerance=None,logical_drive_type=None,physical_drive_label_1=None,physical_drive_status_1=None,physical_drive_capacity_1=None,physical_drive_model_1=None,physical_drive_sn_1=None,physical_drive_confi_1=None,physical_drive_fw_1=None,
                                                                                                                               physical_drive_label_2=None,physical_drive_status_2=None,physical_drive_capacity_2=None,physical_drive_model_2=None,physical_drive_sn_2=None,physical_drive_confi_2=None,physical_drive_fw_2=None,
                                                                                                                               physical_drive_label_3=None,physical_drive_status_3=None,physical_drive_capacity_3=None,physical_drive_model_3=None,physical_drive_sn_3=None,physical_drive_confi_3=None,physical_drive_fw_3=None,
                                                                                                                               physical_drive_label_4=None,physical_drive_status_4=None,physical_drive_capacity_4=None,physical_drive_model_4=None,physical_drive_sn_4=None,physical_drive_confi_4=None,physical_drive_fw_4=None,
                                                                                                                               physical_drive_label_5=None,physical_drive_status_5=None,physical_drive_capacity_5=None,physical_drive_model_5=None,physical_drive_sn_5=None,physical_drive_confi_5=None,physical_drive_fw_5=None,
                                                                                                                               physical_drive_label_6=None,physical_drive_status_6=None,physical_drive_capacity_6=None,physical_drive_model_6=None,physical_drive_sn_6=None,physical_drive_confi_6=None,physical_drive_fw_6=None,
                                                                                                                               physical_drive_label_7=None,physical_drive_status_7=None,physical_drive_capacity_7=None,physical_drive_model_7=None,physical_drive_sn_7=None,physical_drive_confi_7=None,physical_drive_fw_7=None,
                                                                                                                               physical_drive_label_8=None,physical_drive_status_8=None,physical_drive_capacity_8=None,physical_drive_model_8=None,physical_drive_sn_8=None,physical_drive_confi_8=None,physical_drive_fw_8=None,
                                                                                                                               physical_drive_label_9=None,physical_drive_status_9=None,physical_drive_capacity_9=None,physical_drive_model_9=None,physical_drive_sn_9=None,physical_drive_confi_9=None,physical_drive_fw_9=None,
                                                                                                                               physical_drive_label_10=None,physical_drive_status_10=None,physical_drive_capacity_10=None,physical_drive_model_10=None,physical_drive_sn_10=None,physical_drive_confi_10=None,physical_drive_fw_10=None,
                                                                                                                               physical_drive_label_11=None,physical_drive_status_11=None,physical_drive_capacity_11=None,physical_drive_model_11=None,physical_drive_sn_11=None,physical_drive_confi_11=None,physical_drive_fw_11=None,
                                                                                                                               physical_drive_label_12=None,physical_drive_status_12=None,physical_drive_capacity_12=None,physical_drive_model_12=None,physical_drive_sn_12=None,physical_drive_confi_12=None,physical_drive_fw_12=None,
                                                                                                                               physical_drive_label_13=None,physical_drive_status_13=None,physical_drive_capacity_13=None,physical_drive_model_13=None,physical_drive_sn_13=None,physical_drive_confi_13=None,physical_drive_fw_13=None,
                                                                                                                               physical_drive_label_14=None,physical_drive_status_14=None,physical_drive_capacity_14=None,physical_drive_model_14=None,physical_drive_sn_14=None,physical_drive_confi_14=None,physical_drive_fw_14=None,
                                                                                                                               ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'LOGICAL_DRIVE_1': logical_drive, 'LOGICAL_DRIVE_STATUS_1': logical_drive_status, 'LOGICAL_DRIVE_CAPACITY_1': logical_drive_capacity,'LOGICAL_DRIVE_TOLERANCE_1': logical_drive_tolerance,'LOGICAL_DRIVE_TYPE_1': logical_drive_type,
    'PHYSICAL_DRIVE_LABEL_1_1': physical_drive_label_1,'PHYSICAL_DRIVE_STATUS_1_1': physical_drive_status_1,'PHYSICAL_DRIVE_MODEL_1_1': physical_drive_model_1,'PHYSICAL_DRIVE_CAPACITY_1_1': physical_drive_capacity_1,'PHYSICAL_DRIVE_SN_1_1': physical_drive_sn_1,'PHYSICAL_DRIVE_CONFI_1_1': physical_drive_confi_1,'PHYSICAL_DRIVE_FW_1_1': physical_drive_fw_1,
    'PHYSICAL_DRIVE_LABEL_1_2': physical_drive_label_2,'PHYSICAL_DRIVE_STATUS_1_2': physical_drive_status_2,'PHYSICAL_DRIVE_MODEL_1_2': physical_drive_model_2,'PHYSICAL_DRIVE_CAPACITY_1_2': physical_drive_capacity_2,'PHYSICAL_DRIVE_SN_1_2': physical_drive_sn_2,'PHYSICAL_DRIVE_CONFI_1_2': physical_drive_confi_2,'PHYSICAL_DRIVE_FW_1_2': physical_drive_fw_2,
    'PHYSICAL_DRIVE_LABEL_1_3': physical_drive_label_3,'PHYSICAL_DRIVE_STATUS_1_3': physical_drive_status_3,'PHYSICAL_DRIVE_MODEL_1_3': physical_drive_model_3,'PHYSICAL_DRIVE_CAPACITY_1_3': physical_drive_capacity_3,'PHYSICAL_DRIVE_SN_1_3': physical_drive_sn_3,'PHYSICAL_DRIVE_CONFI_1_3': physical_drive_confi_3,'PHYSICAL_DRIVE_FW_1_3': physical_drive_fw_3,
    'PHYSICAL_DRIVE_LABEL_1_4': physical_drive_label_4,'PHYSICAL_DRIVE_STATUS_1_4': physical_drive_status_4,'PHYSICAL_DRIVE_MODEL_1_4': physical_drive_model_4,'PHYSICAL_DRIVE_CAPACITY_1_4': physical_drive_capacity_4,'PHYSICAL_DRIVE_SN_1_4': physical_drive_sn_4,'PHYSICAL_DRIVE_CONFI_1_4': physical_drive_confi_4,'PHYSICAL_DRIVE_FW_1_4': physical_drive_fw_4,
    'PHYSICAL_DRIVE_LABEL_1_5': physical_drive_label_5,'PHYSICAL_DRIVE_STATUS_1_5': physical_drive_status_5,'PHYSICAL_DRIVE_MODEL_1_5': physical_drive_model_5,'PHYSICAL_DRIVE_CAPACITY_1_5': physical_drive_capacity_5,'PHYSICAL_DRIVE_SN_1_5': physical_drive_sn_5,'PHYSICAL_DRIVE_CONFI_1_5': physical_drive_confi_5,'PHYSICAL_DRIVE_FW_1_5': physical_drive_fw_5,
    'PHYSICAL_DRIVE_LABEL_1_6': physical_drive_label_6,'PHYSICAL_DRIVE_STATUS_1_6': physical_drive_status_6,'PHYSICAL_DRIVE_MODEL_1_6': physical_drive_model_6,'PHYSICAL_DRIVE_CAPACITY_1_6': physical_drive_capacity_6,'PHYSICAL_DRIVE_SN_1_6': physical_drive_sn_6,'PHYSICAL_DRIVE_CONFI_1_6': physical_drive_confi_6,'PHYSICAL_DRIVE_FW_1_6': physical_drive_fw_6,
    'PHYSICAL_DRIVE_LABEL_1_7': physical_drive_label_7,'PHYSICAL_DRIVE_STATUS_1_7': physical_drive_status_7,'PHYSICAL_DRIVE_MODEL_1_7': physical_drive_model_7,'PHYSICAL_DRIVE_CAPACITY_1_7': physical_drive_capacity_7,'PHYSICAL_DRIVE_SN_1_7': physical_drive_sn_7,'PHYSICAL_DRIVE_CONFI_1_7': physical_drive_confi_7,'PHYSICAL_DRIVE_FW_1_7': physical_drive_fw_7,
    'PHYSICAL_DRIVE_LABEL_1_8': physical_drive_label_8,'PHYSICAL_DRIVE_STATUS_1_8': physical_drive_status_8,'PHYSICAL_DRIVE_MODEL_1_8': physical_drive_model_8,'PHYSICAL_DRIVE_CAPACITY_1_8': physical_drive_capacity_8,'PHYSICAL_DRIVE_SN_1_8': physical_drive_sn_8,'PHYSICAL_DRIVE_CONFI_1_8': physical_drive_confi_8,'PHYSICAL_DRIVE_FW_1_8': physical_drive_fw_8,
    'PHYSICAL_DRIVE_LABEL_1_9': physical_drive_label_9,'PHYSICAL_DRIVE_STATUS_1_9': physical_drive_status_9,'PHYSICAL_DRIVE_MODEL_1_9': physical_drive_model_9,'PHYSICAL_DRIVE_CAPACITY_1_9': physical_drive_capacity_9,'PHYSICAL_DRIVE_SN_1_9': physical_drive_sn_9,'PHYSICAL_DRIVE_CONFI_1_9': physical_drive_confi_9,'PHYSICAL_DRIVE_FW_1_9': physical_drive_fw_9,
    'PHYSICAL_DRIVE_LABEL_1_10': physical_drive_label_10,'PHYSICAL_DRIVE_STATUS_1_10': physical_drive_status_10,'PHYSICAL_DRIVE_MODEL_1_10': physical_drive_model_10,'PHYSICAL_DRIVE_CAPACITY_1_10': physical_drive_capacity_10, 'PHYSICAL_DRIVE_SN_1_10': physical_drive_sn_10,'PHYSICAL_DRIVE_CONFI_1_10': physical_drive_confi_10, 'PHYSICAL_DRIVE_FW_1_10': physical_drive_fw_10,
    'PHYSICAL_DRIVE_LABEL_1_11': physical_drive_label_11,'PHYSICAL_DRIVE_STATUS_1_11': physical_drive_status_11,'PHYSICAL_DRIVE_MODEL_1_11': physical_drive_model_11,'PHYSICAL_DRIVE_CAPACITY_1_11': physical_drive_capacity_11, 'PHYSICAL_DRIVE_SN_1_11': physical_drive_sn_11,'PHYSICAL_DRIVE_CONFI_1_11': physical_drive_confi_11, 'PHYSICAL_DRIVE_FW_1_11': physical_drive_fw_11,
    'PHYSICAL_DRIVE_LABEL_1_12': physical_drive_label_12,'PHYSICAL_DRIVE_STATUS_1_12': physical_drive_status_12,'PHYSICAL_DRIVE_MODEL_1_12': physical_drive_model_12,'PHYSICAL_DRIVE_CAPACITY_1_12': physical_drive_capacity_12, 'PHYSICAL_DRIVE_SN_1_12': physical_drive_sn_12,'PHYSICAL_DRIVE_CONFI_1_12': physical_drive_confi_12, 'PHYSICAL_DRIVE_FW_1_12': physical_drive_fw_12,
    'PHYSICAL_DRIVE_LABEL_1_13': physical_drive_label_13,'PHYSICAL_DRIVE_STATUS_1_13': physical_drive_status_13,'PHYSICAL_DRIVE_MODEL_1_13': physical_drive_model_13,'PHYSICAL_DRIVE_CAPACITY_1_13': physical_drive_capacity_13, 'PHYSICAL_DRIVE_SN_1_13': physical_drive_sn_13,'PHYSICAL_DRIVE_CONFI_1_13': physical_drive_confi_13, 'PHYSICAL_DRIVE_FW_1_13': physical_drive_fw_13,
    'PHYSICAL_DRIVE_LABEL_1_14': physical_drive_label_14,'PHYSICAL_DRIVE_STATUS_1_14': physical_drive_status_14,'PHYSICAL_DRIVE_MODEL_1_14': physical_drive_model_14,'PHYSICAL_DRIVE_CAPACITY_1_14': physical_drive_capacity_14, 'PHYSICAL_DRIVE_SN_1_14': physical_drive_sn_14,'PHYSICAL_DRIVE_CONFI_1_14': physical_drive_confi_14, 'PHYSICAL_DRIVE_FW_1_14': physical_drive_fw_14,
    'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update STORAGE_INFO set LOGICAL_DRIVE_1=:LOGICAL_DRIVE_1,LOGICAL_DRIVE_STATUS_1=:LOGICAL_DRIVE_STATUS_1,LOGICAL_DRIVE_CAPACITY_1=:LOGICAL_DRIVE_CAPACITY_1,LOGICAL_DRIVE_TOLERANCE_1=:LOGICAL_DRIVE_TOLERANCE_1,LOGICAL_DRIVE_TYPE_1=:LOGICAL_DRIVE_TYPE_1, \
             PHYSICAL_DRIVE_LABEL_1_1=:PHYSICAL_DRIVE_LABEL_1_1 ,PHYSICAL_DRIVE_STATUS_1_1=:PHYSICAL_DRIVE_STATUS_1_1,PHYSICAL_DRIVE_MODEL_1_1=:PHYSICAL_DRIVE_MODEL_1_1,PHYSICAL_DRIVE_CAPACITY_1_1=:PHYSICAL_DRIVE_CAPACITY_1_1,PHYSICAL_DRIVE_SN_1_1=:PHYSICAL_DRIVE_SN_1_1,PHYSICAL_DRIVE_CONFI_1_1=:PHYSICAL_DRIVE_CONFI_1_1,PHYSICAL_DRIVE_FW_1_1=:PHYSICAL_DRIVE_FW_1_1, \
             PHYSICAL_DRIVE_LABEL_1_2=:PHYSICAL_DRIVE_LABEL_1_2 ,PHYSICAL_DRIVE_STATUS_1_2=:PHYSICAL_DRIVE_STATUS_1_2,PHYSICAL_DRIVE_MODEL_1_2=:PHYSICAL_DRIVE_MODEL_1_2,PHYSICAL_DRIVE_CAPACITY_1_2=:PHYSICAL_DRIVE_CAPACITY_1_2,PHYSICAL_DRIVE_SN_1_2=:PHYSICAL_DRIVE_SN_1_2,PHYSICAL_DRIVE_CONFI_1_2=:PHYSICAL_DRIVE_CONFI_1_2,PHYSICAL_DRIVE_FW_1_2=:PHYSICAL_DRIVE_FW_1_2, \
             PHYSICAL_DRIVE_LABEL_1_3=:PHYSICAL_DRIVE_LABEL_1_3 ,PHYSICAL_DRIVE_STATUS_1_3=:PHYSICAL_DRIVE_STATUS_1_3,PHYSICAL_DRIVE_MODEL_1_3=:PHYSICAL_DRIVE_MODEL_1_3,PHYSICAL_DRIVE_CAPACITY_1_3=:PHYSICAL_DRIVE_CAPACITY_1_3,PHYSICAL_DRIVE_SN_1_3=:PHYSICAL_DRIVE_SN_1_3,PHYSICAL_DRIVE_CONFI_1_3=:PHYSICAL_DRIVE_CONFI_1_3,PHYSICAL_DRIVE_FW_1_3=:PHYSICAL_DRIVE_FW_1_3, \
             PHYSICAL_DRIVE_LABEL_1_4=:PHYSICAL_DRIVE_LABEL_1_4 ,PHYSICAL_DRIVE_STATUS_1_4=:PHYSICAL_DRIVE_STATUS_1_4,PHYSICAL_DRIVE_MODEL_1_4=:PHYSICAL_DRIVE_MODEL_1_4,PHYSICAL_DRIVE_CAPACITY_1_4=:PHYSICAL_DRIVE_CAPACITY_1_4,PHYSICAL_DRIVE_SN_1_4=:PHYSICAL_DRIVE_SN_1_4,PHYSICAL_DRIVE_CONFI_1_4=:PHYSICAL_DRIVE_CONFI_1_4,PHYSICAL_DRIVE_FW_1_4=:PHYSICAL_DRIVE_FW_1_4, \
             PHYSICAL_DRIVE_LABEL_1_5=:PHYSICAL_DRIVE_LABEL_1_5 ,PHYSICAL_DRIVE_STATUS_1_5=:PHYSICAL_DRIVE_STATUS_1_5,PHYSICAL_DRIVE_MODEL_1_5=:PHYSICAL_DRIVE_MODEL_1_5,PHYSICAL_DRIVE_CAPACITY_1_5=:PHYSICAL_DRIVE_CAPACITY_1_5,PHYSICAL_DRIVE_SN_1_5=:PHYSICAL_DRIVE_SN_1_5,PHYSICAL_DRIVE_CONFI_1_5=:PHYSICAL_DRIVE_CONFI_1_5,PHYSICAL_DRIVE_FW_1_5=:PHYSICAL_DRIVE_FW_1_5, \
             PHYSICAL_DRIVE_LABEL_1_6=:PHYSICAL_DRIVE_LABEL_1_6 ,PHYSICAL_DRIVE_STATUS_1_6=:PHYSICAL_DRIVE_STATUS_1_6,PHYSICAL_DRIVE_MODEL_1_6=:PHYSICAL_DRIVE_MODEL_1_6,PHYSICAL_DRIVE_CAPACITY_1_6=:PHYSICAL_DRIVE_CAPACITY_1_6,PHYSICAL_DRIVE_SN_1_6=:PHYSICAL_DRIVE_SN_1_6,PHYSICAL_DRIVE_CONFI_1_6=:PHYSICAL_DRIVE_CONFI_1_6,PHYSICAL_DRIVE_FW_1_6=:PHYSICAL_DRIVE_FW_1_6, \
             PHYSICAL_DRIVE_LABEL_1_7=:PHYSICAL_DRIVE_LABEL_1_7 ,PHYSICAL_DRIVE_STATUS_1_7=:PHYSICAL_DRIVE_STATUS_1_7,PHYSICAL_DRIVE_MODEL_1_7=:PHYSICAL_DRIVE_MODEL_1_7,PHYSICAL_DRIVE_CAPACITY_1_7=:PHYSICAL_DRIVE_CAPACITY_1_7,PHYSICAL_DRIVE_SN_1_7=:PHYSICAL_DRIVE_SN_1_7,PHYSICAL_DRIVE_CONFI_1_7=:PHYSICAL_DRIVE_CONFI_1_7,PHYSICAL_DRIVE_FW_1_7=:PHYSICAL_DRIVE_FW_1_7, \
             PHYSICAL_DRIVE_LABEL_1_8=:PHYSICAL_DRIVE_LABEL_1_8 ,PHYSICAL_DRIVE_STATUS_1_8=:PHYSICAL_DRIVE_STATUS_1_8,PHYSICAL_DRIVE_MODEL_1_8=:PHYSICAL_DRIVE_MODEL_1_8,PHYSICAL_DRIVE_CAPACITY_1_8=:PHYSICAL_DRIVE_CAPACITY_1_8,PHYSICAL_DRIVE_SN_1_8=:PHYSICAL_DRIVE_SN_1_8,PHYSICAL_DRIVE_CONFI_1_8=:PHYSICAL_DRIVE_CONFI_1_8,PHYSICAL_DRIVE_FW_1_8=:PHYSICAL_DRIVE_FW_1_8, \
             PHYSICAL_DRIVE_LABEL_1_9=:PHYSICAL_DRIVE_LABEL_1_9 ,PHYSICAL_DRIVE_STATUS_1_9=:PHYSICAL_DRIVE_STATUS_1_9,PHYSICAL_DRIVE_MODEL_1_9=:PHYSICAL_DRIVE_MODEL_1_9,PHYSICAL_DRIVE_CAPACITY_1_9=:PHYSICAL_DRIVE_CAPACITY_1_9,PHYSICAL_DRIVE_SN_1_9=:PHYSICAL_DRIVE_SN_1_9,PHYSICAL_DRIVE_CONFI_1_9=:PHYSICAL_DRIVE_CONFI_1_9,PHYSICAL_DRIVE_FW_1_9=:PHYSICAL_DRIVE_FW_1_9, \
             PHYSICAL_DRIVE_LABEL_1_10=:PHYSICAL_DRIVE_LABEL_1_10 ,PHYSICAL_DRIVE_STATUS_1_10=:PHYSICAL_DRIVE_STATUS_1_10,PHYSICAL_DRIVE_MODEL_1_10=:PHYSICAL_DRIVE_MODEL_1_10,PHYSICAL_DRIVE_CAPACITY_1_10=:PHYSICAL_DRIVE_CAPACITY_1_10,PHYSICAL_DRIVE_SN_1_10=:PHYSICAL_DRIVE_SN_1_10,PHYSICAL_DRIVE_CONFI_1_10=:PHYSICAL_DRIVE_CONFI_1_10,PHYSICAL_DRIVE_FW_1_10=:PHYSICAL_DRIVE_FW_1_10, \
             PHYSICAL_DRIVE_LABEL_1_11=:PHYSICAL_DRIVE_LABEL_1_11 ,PHYSICAL_DRIVE_STATUS_1_11=:PHYSICAL_DRIVE_STATUS_1_11,PHYSICAL_DRIVE_MODEL_1_11=:PHYSICAL_DRIVE_MODEL_1_11,PHYSICAL_DRIVE_CAPACITY_1_11=:PHYSICAL_DRIVE_CAPACITY_1_11,PHYSICAL_DRIVE_SN_1_11=:PHYSICAL_DRIVE_SN_1_11,PHYSICAL_DRIVE_CONFI_1_11=:PHYSICAL_DRIVE_CONFI_1_11,PHYSICAL_DRIVE_FW_1_11=:PHYSICAL_DRIVE_FW_1_11, \
             PHYSICAL_DRIVE_LABEL_1_12=:PHYSICAL_DRIVE_LABEL_1_12 ,PHYSICAL_DRIVE_STATUS_1_12=:PHYSICAL_DRIVE_STATUS_1_12,PHYSICAL_DRIVE_MODEL_1_12=:PHYSICAL_DRIVE_MODEL_1_12,PHYSICAL_DRIVE_CAPACITY_1_12=:PHYSICAL_DRIVE_CAPACITY_1_12,PHYSICAL_DRIVE_SN_1_12=:PHYSICAL_DRIVE_SN_1_12,PHYSICAL_DRIVE_CONFI_1_12=:PHYSICAL_DRIVE_CONFI_1_12,PHYSICAL_DRIVE_FW_1_12=:PHYSICAL_DRIVE_FW_1_12, \
             PHYSICAL_DRIVE_LABEL_1_13=:PHYSICAL_DRIVE_LABEL_1_13 ,PHYSICAL_DRIVE_STATUS_1_13=:PHYSICAL_DRIVE_STATUS_1_13,PHYSICAL_DRIVE_MODEL_1_13=:PHYSICAL_DRIVE_MODEL_1_13,PHYSICAL_DRIVE_CAPACITY_1_13=:PHYSICAL_DRIVE_CAPACITY_1_13,PHYSICAL_DRIVE_SN_1_13=:PHYSICAL_DRIVE_SN_1_13,PHYSICAL_DRIVE_CONFI_1_13=:PHYSICAL_DRIVE_CONFI_1_13,PHYSICAL_DRIVE_FW_1_13=:PHYSICAL_DRIVE_FW_1_13, \
             PHYSICAL_DRIVE_LABEL_1_14=:PHYSICAL_DRIVE_LABEL_1_14 ,PHYSICAL_DRIVE_STATUS_1_14=:PHYSICAL_DRIVE_STATUS_1_14,PHYSICAL_DRIVE_MODEL_1_14=:PHYSICAL_DRIVE_MODEL_1_14,PHYSICAL_DRIVE_CAPACITY_1_14=:PHYSICAL_DRIVE_CAPACITY_1_14,PHYSICAL_DRIVE_SN_1_14=:PHYSICAL_DRIVE_SN_1_14,PHYSICAL_DRIVE_CONFI_1_14=:PHYSICAL_DRIVE_CONFI_1_14,PHYSICAL_DRIVE_FW_1_14=:PHYSICAL_DRIVE_FW_1_14 where IP_ILO=:IP_ILO',
             param)
    connection.commit()
    connection.close()

def update_storage_2_info(logical_drive=None,logical_drive_status=None,logical_drive_capacity=None,logical_drive_tolerance=None,logical_drive_type=None,physical_drive_label_1=None,physical_drive_status_1=None,physical_drive_capacity_1=None,physical_drive_model_1=None,physical_drive_sn_1=None,physical_drive_confi_1=None,physical_drive_fw_1=None,
                                                                                                                               physical_drive_label_2=None,physical_drive_status_2=None,physical_drive_capacity_2=None,physical_drive_model_2=None,physical_drive_sn_2=None,physical_drive_confi_2=None,physical_drive_fw_2=None,
                                                                                                                               physical_drive_label_3=None,physical_drive_status_3=None,physical_drive_capacity_3=None,physical_drive_model_3=None,physical_drive_sn_3=None,physical_drive_confi_3=None,physical_drive_fw_3=None,
                                                                                                                               physical_drive_label_4=None,physical_drive_status_4=None,physical_drive_capacity_4=None,physical_drive_model_4=None,physical_drive_sn_4=None,physical_drive_confi_4=None,physical_drive_fw_4=None,
                                                                                                                               physical_drive_label_5=None,physical_drive_status_5=None,physical_drive_capacity_5=None,physical_drive_model_5=None,physical_drive_sn_5=None,physical_drive_confi_5=None,physical_drive_fw_5=None,
                                                                                                                               physical_drive_label_6=None,physical_drive_status_6=None,physical_drive_capacity_6=None,physical_drive_model_6=None,physical_drive_sn_6=None,physical_drive_confi_6=None,physical_drive_fw_6=None,
                                                                                                                               physical_drive_label_7=None,physical_drive_status_7=None,physical_drive_capacity_7=None,physical_drive_model_7=None,physical_drive_sn_7=None,physical_drive_confi_7=None,physical_drive_fw_7=None,
                                                                                                                               physical_drive_label_8=None,physical_drive_status_8=None,physical_drive_capacity_8=None,physical_drive_model_8=None,physical_drive_sn_8=None,physical_drive_confi_8=None,physical_drive_fw_8=None,
                                                                                                                               physical_drive_label_9=None,physical_drive_status_9=None,physical_drive_capacity_9=None,physical_drive_model_9=None,physical_drive_sn_9=None,physical_drive_confi_9=None,physical_drive_fw_9=None,
                                                                                                                               physical_drive_label_10=None,physical_drive_status_10=None,physical_drive_capacity_10=None,physical_drive_model_10=None,physical_drive_sn_10=None,physical_drive_confi_10=None,physical_drive_fw_10=None,
                                                                                                                               ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'LOGICAL_DRIVE_2': logical_drive, 'LOGICAL_DRIVE_STATUS_2': logical_drive_status, 'LOGICAL_DRIVE_CAPACITY_2': logical_drive_capacity,'LOGICAL_DRIVE_TOLERANCE_2': logical_drive_tolerance,'LOGICAL_DRIVE_TYPE_2': logical_drive_type,
    'PHYSICAL_DRIVE_LABEL_2_1': physical_drive_label_1,'PHYSICAL_DRIVE_STATUS_2_1': physical_drive_status_1,'PHYSICAL_DRIVE_MODEL_2_1': physical_drive_model_1,'PHYSICAL_DRIVE_CAPACITY_2_1': physical_drive_capacity_1,'PHYSICAL_DRIVE_SN_2_1': physical_drive_sn_1,'PHYSICAL_DRIVE_CONFI_2_1': physical_drive_confi_1,'PHYSICAL_DRIVE_FW_2_1': physical_drive_fw_1,
    'PHYSICAL_DRIVE_LABEL_2_2': physical_drive_label_2,'PHYSICAL_DRIVE_STATUS_2_2': physical_drive_status_2,'PHYSICAL_DRIVE_MODEL_2_2': physical_drive_model_2,'PHYSICAL_DRIVE_CAPACITY_2_2': physical_drive_capacity_2,'PHYSICAL_DRIVE_SN_2_2': physical_drive_sn_2,'PHYSICAL_DRIVE_CONFI_2_2': physical_drive_confi_2,'PHYSICAL_DRIVE_FW_2_2': physical_drive_fw_2,
    'PHYSICAL_DRIVE_LABEL_2_3': physical_drive_label_3,'PHYSICAL_DRIVE_STATUS_2_3': physical_drive_status_3,'PHYSICAL_DRIVE_MODEL_2_3': physical_drive_model_3,'PHYSICAL_DRIVE_CAPACITY_2_3': physical_drive_capacity_3,'PHYSICAL_DRIVE_SN_2_3': physical_drive_sn_3,'PHYSICAL_DRIVE_CONFI_2_3': physical_drive_confi_3,'PHYSICAL_DRIVE_FW_2_3': physical_drive_fw_3,
    'PHYSICAL_DRIVE_LABEL_2_4': physical_drive_label_4,'PHYSICAL_DRIVE_STATUS_2_4': physical_drive_status_4,'PHYSICAL_DRIVE_MODEL_2_4': physical_drive_model_4,'PHYSICAL_DRIVE_CAPACITY_2_4': physical_drive_capacity_4,'PHYSICAL_DRIVE_SN_2_4': physical_drive_sn_4,'PHYSICAL_DRIVE_CONFI_2_4': physical_drive_confi_4,'PHYSICAL_DRIVE_FW_2_4': physical_drive_fw_4,
    'PHYSICAL_DRIVE_LABEL_2_5': physical_drive_label_5,'PHYSICAL_DRIVE_STATUS_2_5': physical_drive_status_5,'PHYSICAL_DRIVE_MODEL_2_5': physical_drive_model_5,'PHYSICAL_DRIVE_CAPACITY_2_5': physical_drive_capacity_5,'PHYSICAL_DRIVE_SN_2_5': physical_drive_sn_5,'PHYSICAL_DRIVE_CONFI_2_5': physical_drive_confi_5,'PHYSICAL_DRIVE_FW_2_5': physical_drive_fw_5,
    'PHYSICAL_DRIVE_LABEL_2_6': physical_drive_label_6,'PHYSICAL_DRIVE_STATUS_2_6': physical_drive_status_6,'PHYSICAL_DRIVE_MODEL_2_6': physical_drive_model_6,'PHYSICAL_DRIVE_CAPACITY_2_6': physical_drive_capacity_6,'PHYSICAL_DRIVE_SN_2_6': physical_drive_sn_6,'PHYSICAL_DRIVE_CONFI_2_6': physical_drive_confi_6,'PHYSICAL_DRIVE_FW_2_6': physical_drive_fw_6,
    'PHYSICAL_DRIVE_LABEL_2_7': physical_drive_label_7,'PHYSICAL_DRIVE_STATUS_2_7': physical_drive_status_7,'PHYSICAL_DRIVE_MODEL_2_7': physical_drive_model_7,'PHYSICAL_DRIVE_CAPACITY_2_7': physical_drive_capacity_7,'PHYSICAL_DRIVE_SN_2_7': physical_drive_sn_7,'PHYSICAL_DRIVE_CONFI_2_7': physical_drive_confi_7,'PHYSICAL_DRIVE_FW_2_7': physical_drive_fw_7,
    'PHYSICAL_DRIVE_LABEL_2_8': physical_drive_label_8,'PHYSICAL_DRIVE_STATUS_2_8': physical_drive_status_8,'PHYSICAL_DRIVE_MODEL_2_8': physical_drive_model_8,'PHYSICAL_DRIVE_CAPACITY_2_8': physical_drive_capacity_8,'PHYSICAL_DRIVE_SN_2_8': physical_drive_sn_8,'PHYSICAL_DRIVE_CONFI_2_8': physical_drive_confi_8,'PHYSICAL_DRIVE_FW_2_8': physical_drive_fw_8,
    'PHYSICAL_DRIVE_LABEL_2_9': physical_drive_label_9,'PHYSICAL_DRIVE_STATUS_2_9': physical_drive_status_9,'PHYSICAL_DRIVE_MODEL_2_9': physical_drive_model_9,'PHYSICAL_DRIVE_CAPACITY_2_9': physical_drive_capacity_9,'PHYSICAL_DRIVE_SN_2_9': physical_drive_sn_9,'PHYSICAL_DRIVE_CONFI_2_9': physical_drive_confi_9,'PHYSICAL_DRIVE_FW_2_9': physical_drive_fw_9,
    'PHYSICAL_DRIVE_LABEL_2_10': physical_drive_label_10,'PHYSICAL_DRIVE_STATUS_2_10': physical_drive_status_10,'PHYSICAL_DRIVE_MODEL_2_10': physical_drive_model_10,'PHYSICAL_DRIVE_CAPACITY_2_10': physical_drive_capacity_10, 'PHYSICAL_DRIVE_SN_2_10': physical_drive_sn_10,'PHYSICAL_DRIVE_CONFI_2_10': physical_drive_confi_10, 'PHYSICAL_DRIVE_FW_2_10': physical_drive_fw_10,
    'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update STORAGE_INFO set LOGICAL_DRIVE_2=:LOGICAL_DRIVE_2,LOGICAL_DRIVE_STATUS_2=:LOGICAL_DRIVE_STATUS_2,LOGICAL_DRIVE_CAPACITY_2=:LOGICAL_DRIVE_CAPACITY_2,LOGICAL_DRIVE_TOLERANCE_2=:LOGICAL_DRIVE_TOLERANCE_2,LOGICAL_DRIVE_TYPE_2=:LOGICAL_DRIVE_TYPE_2, \
                         PHYSICAL_DRIVE_LABEL_2_1=:PHYSICAL_DRIVE_LABEL_2_1 ,PHYSICAL_DRIVE_STATUS_2_1=:PHYSICAL_DRIVE_STATUS_2_1,PHYSICAL_DRIVE_MODEL_2_1=:PHYSICAL_DRIVE_MODEL_2_1,PHYSICAL_DRIVE_CAPACITY_2_1=:PHYSICAL_DRIVE_CAPACITY_2_1,PHYSICAL_DRIVE_SN_2_1=:PHYSICAL_DRIVE_SN_2_1,PHYSICAL_DRIVE_CONFI_2_1=:PHYSICAL_DRIVE_CONFI_2_1,PHYSICAL_DRIVE_FW_2_1=:PHYSICAL_DRIVE_FW_2_1, \
                         PHYSICAL_DRIVE_LABEL_2_2=:PHYSICAL_DRIVE_LABEL_2_2 ,PHYSICAL_DRIVE_STATUS_2_2=:PHYSICAL_DRIVE_STATUS_2_2,PHYSICAL_DRIVE_MODEL_2_2=:PHYSICAL_DRIVE_MODEL_2_2,PHYSICAL_DRIVE_CAPACITY_2_2=:PHYSICAL_DRIVE_CAPACITY_2_2,PHYSICAL_DRIVE_SN_2_2=:PHYSICAL_DRIVE_SN_2_2,PHYSICAL_DRIVE_CONFI_2_2=:PHYSICAL_DRIVE_CONFI_2_2,PHYSICAL_DRIVE_FW_2_2=:PHYSICAL_DRIVE_FW_2_2, \
                         PHYSICAL_DRIVE_LABEL_2_3=:PHYSICAL_DRIVE_LABEL_2_3 ,PHYSICAL_DRIVE_STATUS_2_3=:PHYSICAL_DRIVE_STATUS_2_3,PHYSICAL_DRIVE_MODEL_2_3=:PHYSICAL_DRIVE_MODEL_2_3,PHYSICAL_DRIVE_CAPACITY_2_3=:PHYSICAL_DRIVE_CAPACITY_2_3,PHYSICAL_DRIVE_SN_2_3=:PHYSICAL_DRIVE_SN_2_3,PHYSICAL_DRIVE_CONFI_2_3=:PHYSICAL_DRIVE_CONFI_2_3,PHYSICAL_DRIVE_FW_2_3=:PHYSICAL_DRIVE_FW_2_3, \
                         PHYSICAL_DRIVE_LABEL_2_4=:PHYSICAL_DRIVE_LABEL_2_4 ,PHYSICAL_DRIVE_STATUS_2_4=:PHYSICAL_DRIVE_STATUS_2_4,PHYSICAL_DRIVE_MODEL_2_4=:PHYSICAL_DRIVE_MODEL_2_4,PHYSICAL_DRIVE_CAPACITY_2_4=:PHYSICAL_DRIVE_CAPACITY_2_4,PHYSICAL_DRIVE_SN_2_4=:PHYSICAL_DRIVE_SN_2_4,PHYSICAL_DRIVE_CONFI_2_4=:PHYSICAL_DRIVE_CONFI_2_4,PHYSICAL_DRIVE_FW_2_4=:PHYSICAL_DRIVE_FW_2_4, \
                         PHYSICAL_DRIVE_LABEL_2_5=:PHYSICAL_DRIVE_LABEL_2_5 ,PHYSICAL_DRIVE_STATUS_2_5=:PHYSICAL_DRIVE_STATUS_2_5,PHYSICAL_DRIVE_MODEL_2_5=:PHYSICAL_DRIVE_MODEL_2_5,PHYSICAL_DRIVE_CAPACITY_2_5=:PHYSICAL_DRIVE_CAPACITY_2_5,PHYSICAL_DRIVE_SN_2_5=:PHYSICAL_DRIVE_SN_2_5,PHYSICAL_DRIVE_CONFI_2_5=:PHYSICAL_DRIVE_CONFI_2_5,PHYSICAL_DRIVE_FW_2_5=:PHYSICAL_DRIVE_FW_2_5, \
                         PHYSICAL_DRIVE_LABEL_2_6=:PHYSICAL_DRIVE_LABEL_2_6 ,PHYSICAL_DRIVE_STATUS_2_6=:PHYSICAL_DRIVE_STATUS_2_6,PHYSICAL_DRIVE_MODEL_2_6=:PHYSICAL_DRIVE_MODEL_2_6,PHYSICAL_DRIVE_CAPACITY_2_6=:PHYSICAL_DRIVE_CAPACITY_2_6,PHYSICAL_DRIVE_SN_2_6=:PHYSICAL_DRIVE_SN_2_6,PHYSICAL_DRIVE_CONFI_2_6=:PHYSICAL_DRIVE_CONFI_2_6,PHYSICAL_DRIVE_FW_2_6=:PHYSICAL_DRIVE_FW_2_6, \
                         PHYSICAL_DRIVE_LABEL_2_7=:PHYSICAL_DRIVE_LABEL_2_7 ,PHYSICAL_DRIVE_STATUS_2_7=:PHYSICAL_DRIVE_STATUS_2_7,PHYSICAL_DRIVE_MODEL_2_7=:PHYSICAL_DRIVE_MODEL_2_7,PHYSICAL_DRIVE_CAPACITY_2_7=:PHYSICAL_DRIVE_CAPACITY_2_7,PHYSICAL_DRIVE_SN_2_7=:PHYSICAL_DRIVE_SN_2_7,PHYSICAL_DRIVE_CONFI_2_7=:PHYSICAL_DRIVE_CONFI_2_7,PHYSICAL_DRIVE_FW_2_7=:PHYSICAL_DRIVE_FW_2_7, \
                         PHYSICAL_DRIVE_LABEL_2_8=:PHYSICAL_DRIVE_LABEL_2_8 ,PHYSICAL_DRIVE_STATUS_2_8=:PHYSICAL_DRIVE_STATUS_2_8,PHYSICAL_DRIVE_MODEL_2_8=:PHYSICAL_DRIVE_MODEL_2_8,PHYSICAL_DRIVE_CAPACITY_2_8=:PHYSICAL_DRIVE_CAPACITY_2_8,PHYSICAL_DRIVE_SN_2_8=:PHYSICAL_DRIVE_SN_2_8,PHYSICAL_DRIVE_CONFI_2_8=:PHYSICAL_DRIVE_CONFI_2_8,PHYSICAL_DRIVE_FW_2_8=:PHYSICAL_DRIVE_FW_2_8, \
                         PHYSICAL_DRIVE_LABEL_2_9=:PHYSICAL_DRIVE_LABEL_2_9 ,PHYSICAL_DRIVE_STATUS_2_9=:PHYSICAL_DRIVE_STATUS_2_9,PHYSICAL_DRIVE_MODEL_2_9=:PHYSICAL_DRIVE_MODEL_2_9,PHYSICAL_DRIVE_CAPACITY_2_9=:PHYSICAL_DRIVE_CAPACITY_2_9,PHYSICAL_DRIVE_SN_2_9=:PHYSICAL_DRIVE_SN_2_9,PHYSICAL_DRIVE_CONFI_2_9=:PHYSICAL_DRIVE_CONFI_2_9,PHYSICAL_DRIVE_FW_2_9=:PHYSICAL_DRIVE_FW_2_9, \
                         PHYSICAL_DRIVE_LABEL_2_10=:PHYSICAL_DRIVE_LABEL_2_10 ,PHYSICAL_DRIVE_STATUS_2_10=:PHYSICAL_DRIVE_STATUS_2_10,PHYSICAL_DRIVE_MODEL_2_10=:PHYSICAL_DRIVE_MODEL_2_10,PHYSICAL_DRIVE_CAPACITY_2_10=:PHYSICAL_DRIVE_CAPACITY_2_10,PHYSICAL_DRIVE_SN_2_10=:PHYSICAL_DRIVE_SN_2_10,PHYSICAL_DRIVE_CONFI_2_10=:PHYSICAL_DRIVE_CONFI_2_10,PHYSICAL_DRIVE_FW_2_10=:PHYSICAL_DRIVE_FW_2_10 where IP_ILO=:IP_ILO',
                         param)
    connection.commit()
    connection.close()

def update_storage_3_info(logical_drive=None,logical_drive_status=None,logical_drive_capacity=None,logical_drive_tolerance=None,logical_drive_type=None,physical_drive_label_1=None,physical_drive_status_1=None,physical_drive_capacity_1=None,physical_drive_model_1=None,physical_drive_sn_1=None,physical_drive_confi_1=None,physical_drive_fw_1=None,
                                                                                                                               physical_drive_label_2=None,physical_drive_status_2=None,physical_drive_capacity_2=None,physical_drive_model_2=None,physical_drive_sn_2=None,physical_drive_confi_2=None,physical_drive_fw_2=None,
                                                                                                                               physical_drive_label_3=None,physical_drive_status_3=None,physical_drive_capacity_3=None,physical_drive_model_3=None,physical_drive_sn_3=None,physical_drive_confi_3=None,physical_drive_fw_3=None,
                                                                                                                               physical_drive_label_4=None,physical_drive_status_4=None,physical_drive_capacity_4=None,physical_drive_model_4=None,physical_drive_sn_4=None,physical_drive_confi_4=None,physical_drive_fw_4=None,
                                                                                                                               physical_drive_label_5=None,physical_drive_status_5=None,physical_drive_capacity_5=None,physical_drive_model_5=None,physical_drive_sn_5=None,physical_drive_confi_5=None,physical_drive_fw_5=None,
                                                                                                                               physical_drive_label_6=None,physical_drive_status_6=None,physical_drive_capacity_6=None,physical_drive_model_6=None,physical_drive_sn_6=None,physical_drive_confi_6=None,physical_drive_fw_6=None,
                                                                                                                               physical_drive_label_7=None,physical_drive_status_7=None,physical_drive_capacity_7=None,physical_drive_model_7=None,physical_drive_sn_7=None,physical_drive_confi_7=None,physical_drive_fw_7=None,
                                                                                                                               physical_drive_label_8=None,physical_drive_status_8=None,physical_drive_capacity_8=None,physical_drive_model_8=None,physical_drive_sn_8=None,physical_drive_confi_8=None,physical_drive_fw_8=None,
                                                                                                                               physical_drive_label_9=None,physical_drive_status_9=None,physical_drive_capacity_9=None,physical_drive_model_9=None,physical_drive_sn_9=None,physical_drive_confi_9=None,physical_drive_fw_9=None,
                                                                                                                               physical_drive_label_10=None,physical_drive_status_10=None,physical_drive_capacity_10=None,physical_drive_model_10=None,physical_drive_sn_10=None,physical_drive_confi_10=None,physical_drive_fw_10=None,
                                                                                                                               ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'LOGICAL_DRIVE_3': logical_drive, 'LOGICAL_DRIVE_STATUS_3': logical_drive_status, 'LOGICAL_DRIVE_CAPACITY_3': logical_drive_capacity,'LOGICAL_DRIVE_TOLERANCE_3': logical_drive_tolerance,'LOGICAL_DRIVE_TYPE_3': logical_drive_type,
    'PHYSICAL_DRIVE_LABEL_3_1': physical_drive_label_1,'PHYSICAL_DRIVE_STATUS_3_1': physical_drive_status_1,'PHYSICAL_DRIVE_MODEL_3_1': physical_drive_model_1,'PHYSICAL_DRIVE_CAPACITY_3_1': physical_drive_capacity_1,'PHYSICAL_DRIVE_SN_3_1': physical_drive_sn_1,'PHYSICAL_DRIVE_CONFI_3_1': physical_drive_confi_1,'PHYSICAL_DRIVE_FW_3_1': physical_drive_fw_1,
    'PHYSICAL_DRIVE_LABEL_3_2': physical_drive_label_2,'PHYSICAL_DRIVE_STATUS_3_2': physical_drive_status_2,'PHYSICAL_DRIVE_MODEL_3_2': physical_drive_model_2,'PHYSICAL_DRIVE_CAPACITY_3_2': physical_drive_capacity_2,'PHYSICAL_DRIVE_SN_3_2': physical_drive_sn_2,'PHYSICAL_DRIVE_CONFI_3_2': physical_drive_confi_2,'PHYSICAL_DRIVE_FW_3_2': physical_drive_fw_2,
    'PHYSICAL_DRIVE_LABEL_3_3': physical_drive_label_3,'PHYSICAL_DRIVE_STATUS_3_3': physical_drive_status_3,'PHYSICAL_DRIVE_MODEL_3_3': physical_drive_model_3,'PHYSICAL_DRIVE_CAPACITY_3_3': physical_drive_capacity_3,'PHYSICAL_DRIVE_SN_3_3': physical_drive_sn_3,'PHYSICAL_DRIVE_CONFI_3_3': physical_drive_confi_3,'PHYSICAL_DRIVE_FW_3_3': physical_drive_fw_3,
    'PHYSICAL_DRIVE_LABEL_3_4': physical_drive_label_4,'PHYSICAL_DRIVE_STATUS_3_4': physical_drive_status_4,'PHYSICAL_DRIVE_MODEL_3_4': physical_drive_model_4,'PHYSICAL_DRIVE_CAPACITY_3_4': physical_drive_capacity_4,'PHYSICAL_DRIVE_SN_3_4': physical_drive_sn_4,'PHYSICAL_DRIVE_CONFI_3_4': physical_drive_confi_4,'PHYSICAL_DRIVE_FW_3_4': physical_drive_fw_4,
    'PHYSICAL_DRIVE_LABEL_3_5': physical_drive_label_5,'PHYSICAL_DRIVE_STATUS_3_5': physical_drive_status_5,'PHYSICAL_DRIVE_MODEL_3_5': physical_drive_model_5,'PHYSICAL_DRIVE_CAPACITY_3_5': physical_drive_capacity_5,'PHYSICAL_DRIVE_SN_3_5': physical_drive_sn_5,'PHYSICAL_DRIVE_CONFI_3_5': physical_drive_confi_5,'PHYSICAL_DRIVE_FW_3_5': physical_drive_fw_5,
    'PHYSICAL_DRIVE_LABEL_3_6': physical_drive_label_6,'PHYSICAL_DRIVE_STATUS_3_6': physical_drive_status_6,'PHYSICAL_DRIVE_MODEL_3_6': physical_drive_model_6,'PHYSICAL_DRIVE_CAPACITY_3_6': physical_drive_capacity_6,'PHYSICAL_DRIVE_SN_3_6': physical_drive_sn_6,'PHYSICAL_DRIVE_CONFI_3_6': physical_drive_confi_6,'PHYSICAL_DRIVE_FW_3_6': physical_drive_fw_6,
    'PHYSICAL_DRIVE_LABEL_3_7': physical_drive_label_7,'PHYSICAL_DRIVE_STATUS_3_7': physical_drive_status_7,'PHYSICAL_DRIVE_MODEL_3_7': physical_drive_model_7,'PHYSICAL_DRIVE_CAPACITY_3_7': physical_drive_capacity_7,'PHYSICAL_DRIVE_SN_3_7': physical_drive_sn_7,'PHYSICAL_DRIVE_CONFI_3_7': physical_drive_confi_7,'PHYSICAL_DRIVE_FW_3_7': physical_drive_fw_7,
    'PHYSICAL_DRIVE_LABEL_3_8': physical_drive_label_8,'PHYSICAL_DRIVE_STATUS_3_8': physical_drive_status_8,'PHYSICAL_DRIVE_MODEL_3_8': physical_drive_model_8,'PHYSICAL_DRIVE_CAPACITY_3_8': physical_drive_capacity_8,'PHYSICAL_DRIVE_SN_3_8': physical_drive_sn_8,'PHYSICAL_DRIVE_CONFI_3_8': physical_drive_confi_8,'PHYSICAL_DRIVE_FW_3_8': physical_drive_fw_8,
    'PHYSICAL_DRIVE_LABEL_3_9': physical_drive_label_9,'PHYSICAL_DRIVE_STATUS_3_9': physical_drive_status_9,'PHYSICAL_DRIVE_MODEL_3_9': physical_drive_model_9,'PHYSICAL_DRIVE_CAPACITY_3_9': physical_drive_capacity_9,'PHYSICAL_DRIVE_SN_3_9': physical_drive_sn_9,'PHYSICAL_DRIVE_CONFI_3_9': physical_drive_confi_9,'PHYSICAL_DRIVE_FW_3_9': physical_drive_fw_9,
    'PHYSICAL_DRIVE_LABEL_3_10': physical_drive_label_10,'PHYSICAL_DRIVE_STATUS_3_10': physical_drive_status_10,'PHYSICAL_DRIVE_MODEL_3_10': physical_drive_model_10,'PHYSICAL_DRIVE_CAPACITY_3_10': physical_drive_capacity_10, 'PHYSICAL_DRIVE_SN_3_10': physical_drive_sn_10,'PHYSICAL_DRIVE_CONFI_3_10': physical_drive_confi_10, 'PHYSICAL_DRIVE_FW_3_10': physical_drive_fw_10,
    'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update STORAGE_INFO set LOGICAL_DRIVE_3=:LOGICAL_DRIVE_3,LOGICAL_DRIVE_STATUS_3=:LOGICAL_DRIVE_STATUS_3,LOGICAL_DRIVE_CAPACITY_3=:LOGICAL_DRIVE_CAPACITY_3,LOGICAL_DRIVE_TOLERANCE_3=:LOGICAL_DRIVE_TOLERANCE_3,LOGICAL_DRIVE_TYPE_3=:LOGICAL_DRIVE_TYPE_3, \
                         PHYSICAL_DRIVE_LABEL_3_1=:PHYSICAL_DRIVE_LABEL_3_1 ,PHYSICAL_DRIVE_STATUS_3_1=:PHYSICAL_DRIVE_STATUS_3_1,PHYSICAL_DRIVE_MODEL_3_1=:PHYSICAL_DRIVE_MODEL_3_1,PHYSICAL_DRIVE_CAPACITY_3_1=:PHYSICAL_DRIVE_CAPACITY_3_1,PHYSICAL_DRIVE_SN_3_1=:PHYSICAL_DRIVE_SN_3_1,PHYSICAL_DRIVE_CONFI_3_1=:PHYSICAL_DRIVE_CONFI_3_1,PHYSICAL_DRIVE_FW_3_1=:PHYSICAL_DRIVE_FW_3_1, \
                         PHYSICAL_DRIVE_LABEL_3_2=:PHYSICAL_DRIVE_LABEL_3_2 ,PHYSICAL_DRIVE_STATUS_3_2=:PHYSICAL_DRIVE_STATUS_3_2,PHYSICAL_DRIVE_MODEL_3_2=:PHYSICAL_DRIVE_MODEL_3_2,PHYSICAL_DRIVE_CAPACITY_3_2=:PHYSICAL_DRIVE_CAPACITY_3_2,PHYSICAL_DRIVE_SN_3_2=:PHYSICAL_DRIVE_SN_3_2,PHYSICAL_DRIVE_CONFI_3_2=:PHYSICAL_DRIVE_CONFI_3_2,PHYSICAL_DRIVE_FW_3_2=:PHYSICAL_DRIVE_FW_3_2, \
                         PHYSICAL_DRIVE_LABEL_3_3=:PHYSICAL_DRIVE_LABEL_3_3 ,PHYSICAL_DRIVE_STATUS_3_3=:PHYSICAL_DRIVE_STATUS_3_3,PHYSICAL_DRIVE_MODEL_3_3=:PHYSICAL_DRIVE_MODEL_3_3,PHYSICAL_DRIVE_CAPACITY_3_3=:PHYSICAL_DRIVE_CAPACITY_3_3,PHYSICAL_DRIVE_SN_3_3=:PHYSICAL_DRIVE_SN_3_3,PHYSICAL_DRIVE_CONFI_3_3=:PHYSICAL_DRIVE_CONFI_3_3,PHYSICAL_DRIVE_FW_3_3=:PHYSICAL_DRIVE_FW_3_3, \
                         PHYSICAL_DRIVE_LABEL_3_4=:PHYSICAL_DRIVE_LABEL_3_4 ,PHYSICAL_DRIVE_STATUS_3_4=:PHYSICAL_DRIVE_STATUS_3_4,PHYSICAL_DRIVE_MODEL_3_4=:PHYSICAL_DRIVE_MODEL_3_4,PHYSICAL_DRIVE_CAPACITY_3_4=:PHYSICAL_DRIVE_CAPACITY_3_4,PHYSICAL_DRIVE_SN_3_4=:PHYSICAL_DRIVE_SN_3_4,PHYSICAL_DRIVE_CONFI_3_4=:PHYSICAL_DRIVE_CONFI_3_4,PHYSICAL_DRIVE_FW_3_4=:PHYSICAL_DRIVE_FW_3_4, \
                         PHYSICAL_DRIVE_LABEL_3_5=:PHYSICAL_DRIVE_LABEL_3_5 ,PHYSICAL_DRIVE_STATUS_3_5=:PHYSICAL_DRIVE_STATUS_3_5,PHYSICAL_DRIVE_MODEL_3_5=:PHYSICAL_DRIVE_MODEL_3_5,PHYSICAL_DRIVE_CAPACITY_3_5=:PHYSICAL_DRIVE_CAPACITY_3_5,PHYSICAL_DRIVE_SN_3_5=:PHYSICAL_DRIVE_SN_3_5,PHYSICAL_DRIVE_CONFI_3_5=:PHYSICAL_DRIVE_CONFI_3_5,PHYSICAL_DRIVE_FW_3_5=:PHYSICAL_DRIVE_FW_3_5, \
                         PHYSICAL_DRIVE_LABEL_3_6=:PHYSICAL_DRIVE_LABEL_3_6 ,PHYSICAL_DRIVE_STATUS_3_6=:PHYSICAL_DRIVE_STATUS_3_6,PHYSICAL_DRIVE_MODEL_3_6=:PHYSICAL_DRIVE_MODEL_3_6,PHYSICAL_DRIVE_CAPACITY_3_6=:PHYSICAL_DRIVE_CAPACITY_3_6,PHYSICAL_DRIVE_SN_3_6=:PHYSICAL_DRIVE_SN_3_6,PHYSICAL_DRIVE_CONFI_3_6=:PHYSICAL_DRIVE_CONFI_3_6,PHYSICAL_DRIVE_FW_3_6=:PHYSICAL_DRIVE_FW_3_6, \
                         PHYSICAL_DRIVE_LABEL_3_7=:PHYSICAL_DRIVE_LABEL_3_7 ,PHYSICAL_DRIVE_STATUS_3_7=:PHYSICAL_DRIVE_STATUS_3_7,PHYSICAL_DRIVE_MODEL_3_7=:PHYSICAL_DRIVE_MODEL_3_7,PHYSICAL_DRIVE_CAPACITY_3_7=:PHYSICAL_DRIVE_CAPACITY_3_7,PHYSICAL_DRIVE_SN_3_7=:PHYSICAL_DRIVE_SN_3_7,PHYSICAL_DRIVE_CONFI_3_7=:PHYSICAL_DRIVE_CONFI_3_7,PHYSICAL_DRIVE_FW_3_7=:PHYSICAL_DRIVE_FW_3_7, \
                         PHYSICAL_DRIVE_LABEL_3_8=:PHYSICAL_DRIVE_LABEL_3_8 ,PHYSICAL_DRIVE_STATUS_3_8=:PHYSICAL_DRIVE_STATUS_3_8,PHYSICAL_DRIVE_MODEL_3_8=:PHYSICAL_DRIVE_MODEL_3_8,PHYSICAL_DRIVE_CAPACITY_3_8=:PHYSICAL_DRIVE_CAPACITY_3_8,PHYSICAL_DRIVE_SN_3_8=:PHYSICAL_DRIVE_SN_3_8,PHYSICAL_DRIVE_CONFI_3_8=:PHYSICAL_DRIVE_CONFI_3_8,PHYSICAL_DRIVE_FW_3_8=:PHYSICAL_DRIVE_FW_3_8, \
                         PHYSICAL_DRIVE_LABEL_3_9=:PHYSICAL_DRIVE_LABEL_3_9 ,PHYSICAL_DRIVE_STATUS_3_9=:PHYSICAL_DRIVE_STATUS_3_9,PHYSICAL_DRIVE_MODEL_3_9=:PHYSICAL_DRIVE_MODEL_3_9,PHYSICAL_DRIVE_CAPACITY_3_9=:PHYSICAL_DRIVE_CAPACITY_3_9,PHYSICAL_DRIVE_SN_3_9=:PHYSICAL_DRIVE_SN_3_9,PHYSICAL_DRIVE_CONFI_3_9=:PHYSICAL_DRIVE_CONFI_3_9,PHYSICAL_DRIVE_FW_3_9=:PHYSICAL_DRIVE_FW_3_9, \
                         PHYSICAL_DRIVE_LABEL_3_10=:PHYSICAL_DRIVE_LABEL_3_10 ,PHYSICAL_DRIVE_STATUS_3_10=:PHYSICAL_DRIVE_STATUS_3_10,PHYSICAL_DRIVE_MODEL_3_10=:PHYSICAL_DRIVE_MODEL_3_10,PHYSICAL_DRIVE_CAPACITY_3_10=:PHYSICAL_DRIVE_CAPACITY_3_10,PHYSICAL_DRIVE_SN_3_10=:PHYSICAL_DRIVE_SN_3_10,PHYSICAL_DRIVE_CONFI_3_10=:PHYSICAL_DRIVE_CONFI_3_10,PHYSICAL_DRIVE_FW_3_10=:PHYSICAL_DRIVE_FW_3_10 where IP_ILO=:IP_ILO',
                         param)
    connection.commit()
    connection.close()

def update_storage_4_info(logical_drive=None,logical_drive_status=None,logical_drive_capacity=None,logical_drive_tolerance=None,logical_drive_type=None,physical_drive_label_1=None,physical_drive_status_1=None,physical_drive_capacity_1=None,physical_drive_model_1=None,physical_drive_sn_1=None,physical_drive_confi_1=None,physical_drive_fw_1=None,
                                                                                                                               physical_drive_label_2=None,physical_drive_status_2=None,physical_drive_capacity_2=None,physical_drive_model_2=None,physical_drive_sn_2=None,physical_drive_confi_2=None,physical_drive_fw_2=None,
                                                                                                                               physical_drive_label_3=None,physical_drive_status_3=None,physical_drive_capacity_3=None,physical_drive_model_3=None,physical_drive_sn_3=None,physical_drive_confi_3=None,physical_drive_fw_3=None,
                                                                                                                               physical_drive_label_4=None,physical_drive_status_4=None,physical_drive_capacity_4=None,physical_drive_model_4=None,physical_drive_sn_4=None,physical_drive_confi_4=None,physical_drive_fw_4=None,
                                                                                                                               physical_drive_label_5=None,physical_drive_status_5=None,physical_drive_capacity_5=None,physical_drive_model_5=None,physical_drive_sn_5=None,physical_drive_confi_5=None,physical_drive_fw_5=None,
                                                                                                                               physical_drive_label_6=None,physical_drive_status_6=None,physical_drive_capacity_6=None,physical_drive_model_6=None,physical_drive_sn_6=None,physical_drive_confi_6=None,physical_drive_fw_6=None,
                                                                                                                               physical_drive_label_7=None,physical_drive_status_7=None,physical_drive_capacity_7=None,physical_drive_model_7=None,physical_drive_sn_7=None,physical_drive_confi_7=None,physical_drive_fw_7=None,
                                                                                                                               physical_drive_label_8=None,physical_drive_status_8=None,physical_drive_capacity_8=None,physical_drive_model_8=None,physical_drive_sn_8=None,physical_drive_confi_8=None,physical_drive_fw_8=None,
                                                                                                                               physical_drive_label_9=None,physical_drive_status_9=None,physical_drive_capacity_9=None,physical_drive_model_9=None,physical_drive_sn_9=None,physical_drive_confi_9=None,physical_drive_fw_9=None,
                                                                                                                               physical_drive_label_10=None,physical_drive_status_10=None,physical_drive_capacity_10=None,physical_drive_model_10=None,physical_drive_sn_10=None,physical_drive_confi_10=None,physical_drive_fw_10=None,
                                                                                                                               ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'LOGICAL_DRIVE_4': logical_drive, 'LOGICAL_DRIVE_STATUS_4': logical_drive_status, 'LOGICAL_DRIVE_CAPACITY_4': logical_drive_capacity,'LOGICAL_DRIVE_TOLERANCE_4': logical_drive_tolerance,'LOGICAL_DRIVE_TYPE_4': logical_drive_type,
    'PHYSICAL_DRIVE_LABEL_4_1': physical_drive_label_1,'PHYSICAL_DRIVE_STATUS_4_1': physical_drive_status_1,'PHYSICAL_DRIVE_MODEL_4_1': physical_drive_model_1,'PHYSICAL_DRIVE_CAPACITY_4_1': physical_drive_capacity_1,'PHYSICAL_DRIVE_SN_4_1': physical_drive_sn_1,'PHYSICAL_DRIVE_CONFI_4_1': physical_drive_confi_1,'PHYSICAL_DRIVE_FW_4_1': physical_drive_fw_1,
    'PHYSICAL_DRIVE_LABEL_4_2': physical_drive_label_2,'PHYSICAL_DRIVE_STATUS_4_2': physical_drive_status_2,'PHYSICAL_DRIVE_MODEL_4_2': physical_drive_model_2,'PHYSICAL_DRIVE_CAPACITY_4_2': physical_drive_capacity_2,'PHYSICAL_DRIVE_SN_4_2': physical_drive_sn_2,'PHYSICAL_DRIVE_CONFI_4_2': physical_drive_confi_2,'PHYSICAL_DRIVE_FW_4_2': physical_drive_fw_2,
    'PHYSICAL_DRIVE_LABEL_4_3': physical_drive_label_3,'PHYSICAL_DRIVE_STATUS_4_3': physical_drive_status_3,'PHYSICAL_DRIVE_MODEL_4_3': physical_drive_model_3,'PHYSICAL_DRIVE_CAPACITY_4_3': physical_drive_capacity_3,'PHYSICAL_DRIVE_SN_4_3': physical_drive_sn_3,'PHYSICAL_DRIVE_CONFI_4_3': physical_drive_confi_3,'PHYSICAL_DRIVE_FW_4_3': physical_drive_fw_3,
    'PHYSICAL_DRIVE_LABEL_4_4': physical_drive_label_4,'PHYSICAL_DRIVE_STATUS_4_4': physical_drive_status_4,'PHYSICAL_DRIVE_MODEL_4_4': physical_drive_model_4,'PHYSICAL_DRIVE_CAPACITY_4_4': physical_drive_capacity_4,'PHYSICAL_DRIVE_SN_4_4': physical_drive_sn_4,'PHYSICAL_DRIVE_CONFI_4_4': physical_drive_confi_4,'PHYSICAL_DRIVE_FW_4_4': physical_drive_fw_4,
    'PHYSICAL_DRIVE_LABEL_4_5': physical_drive_label_5,'PHYSICAL_DRIVE_STATUS_4_5': physical_drive_status_5,'PHYSICAL_DRIVE_MODEL_4_5': physical_drive_model_5,'PHYSICAL_DRIVE_CAPACITY_4_5': physical_drive_capacity_5,'PHYSICAL_DRIVE_SN_4_5': physical_drive_sn_5,'PHYSICAL_DRIVE_CONFI_4_5': physical_drive_confi_5,'PHYSICAL_DRIVE_FW_4_5': physical_drive_fw_5,
    'PHYSICAL_DRIVE_LABEL_4_6': physical_drive_label_6,'PHYSICAL_DRIVE_STATUS_4_6': physical_drive_status_6,'PHYSICAL_DRIVE_MODEL_4_6': physical_drive_model_6,'PHYSICAL_DRIVE_CAPACITY_4_6': physical_drive_capacity_6,'PHYSICAL_DRIVE_SN_4_6': physical_drive_sn_6,'PHYSICAL_DRIVE_CONFI_4_6': physical_drive_confi_6,'PHYSICAL_DRIVE_FW_4_6': physical_drive_fw_6,
    'PHYSICAL_DRIVE_LABEL_4_7': physical_drive_label_7,'PHYSICAL_DRIVE_STATUS_4_7': physical_drive_status_7,'PHYSICAL_DRIVE_MODEL_4_7': physical_drive_model_7,'PHYSICAL_DRIVE_CAPACITY_4_7': physical_drive_capacity_7,'PHYSICAL_DRIVE_SN_4_7': physical_drive_sn_7,'PHYSICAL_DRIVE_CONFI_4_7': physical_drive_confi_7,'PHYSICAL_DRIVE_FW_4_7': physical_drive_fw_7,
    'PHYSICAL_DRIVE_LABEL_4_8': physical_drive_label_8,'PHYSICAL_DRIVE_STATUS_4_8': physical_drive_status_8,'PHYSICAL_DRIVE_MODEL_4_8': physical_drive_model_8,'PHYSICAL_DRIVE_CAPACITY_4_8': physical_drive_capacity_8,'PHYSICAL_DRIVE_SN_4_8': physical_drive_sn_8,'PHYSICAL_DRIVE_CONFI_4_8': physical_drive_confi_8,'PHYSICAL_DRIVE_FW_4_8': physical_drive_fw_8,
    'PHYSICAL_DRIVE_LABEL_4_9': physical_drive_label_9,'PHYSICAL_DRIVE_STATUS_4_9': physical_drive_status_9,'PHYSICAL_DRIVE_MODEL_4_9': physical_drive_model_9,'PHYSICAL_DRIVE_CAPACITY_4_9': physical_drive_capacity_9,'PHYSICAL_DRIVE_SN_4_9': physical_drive_sn_9,'PHYSICAL_DRIVE_CONFI_4_9': physical_drive_confi_9,'PHYSICAL_DRIVE_FW_4_9': physical_drive_fw_9,
    'PHYSICAL_DRIVE_LABEL_4_10': physical_drive_label_10,'PHYSICAL_DRIVE_STATUS_4_10': physical_drive_status_10,'PHYSICAL_DRIVE_MODEL_4_10': physical_drive_model_10,'PHYSICAL_DRIVE_CAPACITY_4_10': physical_drive_capacity_10, 'PHYSICAL_DRIVE_SN_4_10': physical_drive_sn_10,'PHYSICAL_DRIVE_CONFI_4_10': physical_drive_confi_10, 'PHYSICAL_DRIVE_FW_4_10': physical_drive_fw_10,
    'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update STORAGE_INFO set LOGICAL_DRIVE_4=:LOGICAL_DRIVE_4,LOGICAL_DRIVE_STATUS_4=:LOGICAL_DRIVE_STATUS_4,LOGICAL_DRIVE_CAPACITY_4=:LOGICAL_DRIVE_CAPACITY_4,LOGICAL_DRIVE_TOLERANCE_4=:LOGICAL_DRIVE_TOLERANCE_4,LOGICAL_DRIVE_TYPE_4=:LOGICAL_DRIVE_TYPE_4, \
                         PHYSICAL_DRIVE_LABEL_4_1=:PHYSICAL_DRIVE_LABEL_4_1 ,PHYSICAL_DRIVE_STATUS_4_1=:PHYSICAL_DRIVE_STATUS_4_1,PHYSICAL_DRIVE_MODEL_4_1=:PHYSICAL_DRIVE_MODEL_4_1,PHYSICAL_DRIVE_CAPACITY_4_1=:PHYSICAL_DRIVE_CAPACITY_4_1,PHYSICAL_DRIVE_SN_4_1=:PHYSICAL_DRIVE_SN_4_1,PHYSICAL_DRIVE_CONFI_4_1=:PHYSICAL_DRIVE_CONFI_4_1,PHYSICAL_DRIVE_FW_4_1=:PHYSICAL_DRIVE_FW_4_1, \
                         PHYSICAL_DRIVE_LABEL_4_2=:PHYSICAL_DRIVE_LABEL_4_2 ,PHYSICAL_DRIVE_STATUS_4_2=:PHYSICAL_DRIVE_STATUS_4_2,PHYSICAL_DRIVE_MODEL_4_2=:PHYSICAL_DRIVE_MODEL_4_2,PHYSICAL_DRIVE_CAPACITY_4_2=:PHYSICAL_DRIVE_CAPACITY_4_2,PHYSICAL_DRIVE_SN_4_2=:PHYSICAL_DRIVE_SN_4_2,PHYSICAL_DRIVE_CONFI_4_2=:PHYSICAL_DRIVE_CONFI_4_2,PHYSICAL_DRIVE_FW_4_2=:PHYSICAL_DRIVE_FW_4_2, \
                         PHYSICAL_DRIVE_LABEL_4_3=:PHYSICAL_DRIVE_LABEL_4_3 ,PHYSICAL_DRIVE_STATUS_4_3=:PHYSICAL_DRIVE_STATUS_4_3,PHYSICAL_DRIVE_MODEL_4_3=:PHYSICAL_DRIVE_MODEL_4_3,PHYSICAL_DRIVE_CAPACITY_4_3=:PHYSICAL_DRIVE_CAPACITY_4_3,PHYSICAL_DRIVE_SN_4_3=:PHYSICAL_DRIVE_SN_4_3,PHYSICAL_DRIVE_CONFI_4_3=:PHYSICAL_DRIVE_CONFI_4_3,PHYSICAL_DRIVE_FW_4_3=:PHYSICAL_DRIVE_FW_4_3, \
                         PHYSICAL_DRIVE_LABEL_4_4=:PHYSICAL_DRIVE_LABEL_4_4 ,PHYSICAL_DRIVE_STATUS_4_4=:PHYSICAL_DRIVE_STATUS_4_4,PHYSICAL_DRIVE_MODEL_4_4=:PHYSICAL_DRIVE_MODEL_4_4,PHYSICAL_DRIVE_CAPACITY_4_4=:PHYSICAL_DRIVE_CAPACITY_4_4,PHYSICAL_DRIVE_SN_4_4=:PHYSICAL_DRIVE_SN_4_4,PHYSICAL_DRIVE_CONFI_4_4=:PHYSICAL_DRIVE_CONFI_4_4,PHYSICAL_DRIVE_FW_4_4=:PHYSICAL_DRIVE_FW_4_4, \
                         PHYSICAL_DRIVE_LABEL_4_5=:PHYSICAL_DRIVE_LABEL_4_5 ,PHYSICAL_DRIVE_STATUS_4_5=:PHYSICAL_DRIVE_STATUS_4_5,PHYSICAL_DRIVE_MODEL_4_5=:PHYSICAL_DRIVE_MODEL_4_5,PHYSICAL_DRIVE_CAPACITY_4_5=:PHYSICAL_DRIVE_CAPACITY_4_5,PHYSICAL_DRIVE_SN_4_5=:PHYSICAL_DRIVE_SN_4_5,PHYSICAL_DRIVE_CONFI_4_5=:PHYSICAL_DRIVE_CONFI_4_5,PHYSICAL_DRIVE_FW_4_5=:PHYSICAL_DRIVE_FW_4_5, \
                         PHYSICAL_DRIVE_LABEL_4_6=:PHYSICAL_DRIVE_LABEL_4_6 ,PHYSICAL_DRIVE_STATUS_4_6=:PHYSICAL_DRIVE_STATUS_4_6,PHYSICAL_DRIVE_MODEL_4_6=:PHYSICAL_DRIVE_MODEL_4_6,PHYSICAL_DRIVE_CAPACITY_4_6=:PHYSICAL_DRIVE_CAPACITY_4_6,PHYSICAL_DRIVE_SN_4_6=:PHYSICAL_DRIVE_SN_4_6,PHYSICAL_DRIVE_CONFI_4_6=:PHYSICAL_DRIVE_CONFI_4_6,PHYSICAL_DRIVE_FW_4_6=:PHYSICAL_DRIVE_FW_4_6, \
                         PHYSICAL_DRIVE_LABEL_4_7=:PHYSICAL_DRIVE_LABEL_4_7 ,PHYSICAL_DRIVE_STATUS_4_7=:PHYSICAL_DRIVE_STATUS_4_7,PHYSICAL_DRIVE_MODEL_4_7=:PHYSICAL_DRIVE_MODEL_4_7,PHYSICAL_DRIVE_CAPACITY_4_7=:PHYSICAL_DRIVE_CAPACITY_4_7,PHYSICAL_DRIVE_SN_4_7=:PHYSICAL_DRIVE_SN_4_7,PHYSICAL_DRIVE_CONFI_4_7=:PHYSICAL_DRIVE_CONFI_4_7,PHYSICAL_DRIVE_FW_4_7=:PHYSICAL_DRIVE_FW_4_7, \
                         PHYSICAL_DRIVE_LABEL_4_8=:PHYSICAL_DRIVE_LABEL_4_8 ,PHYSICAL_DRIVE_STATUS_4_8=:PHYSICAL_DRIVE_STATUS_4_8,PHYSICAL_DRIVE_MODEL_4_8=:PHYSICAL_DRIVE_MODEL_4_8,PHYSICAL_DRIVE_CAPACITY_4_8=:PHYSICAL_DRIVE_CAPACITY_4_8,PHYSICAL_DRIVE_SN_4_8=:PHYSICAL_DRIVE_SN_4_8,PHYSICAL_DRIVE_CONFI_4_8=:PHYSICAL_DRIVE_CONFI_4_8,PHYSICAL_DRIVE_FW_4_8=:PHYSICAL_DRIVE_FW_4_8, \
                         PHYSICAL_DRIVE_LABEL_4_9=:PHYSICAL_DRIVE_LABEL_4_9 ,PHYSICAL_DRIVE_STATUS_4_9=:PHYSICAL_DRIVE_STATUS_4_9,PHYSICAL_DRIVE_MODEL_4_9=:PHYSICAL_DRIVE_MODEL_4_9,PHYSICAL_DRIVE_CAPACITY_4_9=:PHYSICAL_DRIVE_CAPACITY_4_9,PHYSICAL_DRIVE_SN_4_9=:PHYSICAL_DRIVE_SN_4_9,PHYSICAL_DRIVE_CONFI_4_9=:PHYSICAL_DRIVE_CONFI_4_9,PHYSICAL_DRIVE_FW_4_9=:PHYSICAL_DRIVE_FW_4_9, \
                         PHYSICAL_DRIVE_LABEL_4_10=:PHYSICAL_DRIVE_LABEL_4_10 ,PHYSICAL_DRIVE_STATUS_4_10=:PHYSICAL_DRIVE_STATUS_4_10,PHYSICAL_DRIVE_MODEL_4_10=:PHYSICAL_DRIVE_MODEL_4_10,PHYSICAL_DRIVE_CAPACITY_4_10=:PHYSICAL_DRIVE_CAPACITY_4_10,PHYSICAL_DRIVE_SN_4_10=:PHYSICAL_DRIVE_SN_4_10,PHYSICAL_DRIVE_CONFI_4_10=:PHYSICAL_DRIVE_CONFI_4_10,PHYSICAL_DRIVE_FW_4_10=:PHYSICAL_DRIVE_FW_4_10 where IP_ILO=:IP_ILO',
                         param)
    connection.commit()
    connection.close()

def update_storage_5_info(logical_drive=None,logical_drive_status=None,logical_drive_capacity=None,logical_drive_tolerance=None,logical_drive_type=None,physical_drive_label_1=None,physical_drive_status_1=None,physical_drive_capacity_1=None,physical_drive_model_1=None,physical_drive_sn_1=None,physical_drive_confi_1=None,physical_drive_fw_1=None,
                                                                                                                               physical_drive_label_2=None,physical_drive_status_2=None,physical_drive_capacity_2=None,physical_drive_model_2=None,physical_drive_sn_2=None,physical_drive_confi_2=None,physical_drive_fw_2=None,
                                                                                                                               physical_drive_label_3=None,physical_drive_status_3=None,physical_drive_capacity_3=None,physical_drive_model_3=None,physical_drive_sn_3=None,physical_drive_confi_3=None,physical_drive_fw_3=None,
                                                                                                                               physical_drive_label_4=None,physical_drive_status_4=None,physical_drive_capacity_4=None,physical_drive_model_4=None,physical_drive_sn_4=None,physical_drive_confi_4=None,physical_drive_fw_4=None,
                                                                                                                               physical_drive_label_5=None,physical_drive_status_5=None,physical_drive_capacity_5=None,physical_drive_model_5=None,physical_drive_sn_5=None,physical_drive_confi_5=None,physical_drive_fw_5=None,
                                                                                                                               physical_drive_label_6=None,physical_drive_status_6=None,physical_drive_capacity_6=None,physical_drive_model_6=None,physical_drive_sn_6=None,physical_drive_confi_6=None,physical_drive_fw_6=None,
                                                                                                                               physical_drive_label_7=None,physical_drive_status_7=None,physical_drive_capacity_7=None,physical_drive_model_7=None,physical_drive_sn_7=None,physical_drive_confi_7=None,physical_drive_fw_7=None,
                                                                                                                               physical_drive_label_8=None,physical_drive_status_8=None,physical_drive_capacity_8=None,physical_drive_model_8=None,physical_drive_sn_8=None,physical_drive_confi_8=None,physical_drive_fw_8=None,
                                                                                                                               physical_drive_label_9=None,physical_drive_status_9=None,physical_drive_capacity_9=None,physical_drive_model_9=None,physical_drive_sn_9=None,physical_drive_confi_9=None,physical_drive_fw_9=None,
                                                                                                                               physical_drive_label_10=None,physical_drive_status_10=None,physical_drive_capacity_10=None,physical_drive_model_10=None,physical_drive_sn_10=None,physical_drive_confi_10=None,physical_drive_fw_10=None,
                                                                                                                               ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'LOGICAL_DRIVE_5': logical_drive, 'LOGICAL_DRIVE_STATUS_5': logical_drive_status, 'LOGICAL_DRIVE_CAPACITY_5': logical_drive_capacity,'LOGICAL_DRIVE_TOLERANCE_5': logical_drive_tolerance,'LOGICAL_DRIVE_TYPE_5': logical_drive_type,
    'PHYSICAL_DRIVE_LABEL_5_1': physical_drive_label_1,'PHYSICAL_DRIVE_STATUS_5_1': physical_drive_status_1,'PHYSICAL_DRIVE_MODEL_5_1': physical_drive_model_1,'PHYSICAL_DRIVE_CAPACITY_5_1': physical_drive_capacity_1,'PHYSICAL_DRIVE_SN_5_1': physical_drive_sn_1,'PHYSICAL_DRIVE_CONFI_5_1': physical_drive_confi_1,'PHYSICAL_DRIVE_FW_5_1': physical_drive_fw_1,
    'PHYSICAL_DRIVE_LABEL_5_2': physical_drive_label_2,'PHYSICAL_DRIVE_STATUS_5_2': physical_drive_status_2,'PHYSICAL_DRIVE_MODEL_5_2': physical_drive_model_2,'PHYSICAL_DRIVE_CAPACITY_5_2': physical_drive_capacity_2,'PHYSICAL_DRIVE_SN_5_2': physical_drive_sn_2,'PHYSICAL_DRIVE_CONFI_5_2': physical_drive_confi_2,'PHYSICAL_DRIVE_FW_5_2': physical_drive_fw_2,
    'PHYSICAL_DRIVE_LABEL_5_3': physical_drive_label_3,'PHYSICAL_DRIVE_STATUS_5_3': physical_drive_status_3,'PHYSICAL_DRIVE_MODEL_5_3': physical_drive_model_3,'PHYSICAL_DRIVE_CAPACITY_5_3': physical_drive_capacity_3,'PHYSICAL_DRIVE_SN_5_3': physical_drive_sn_3,'PHYSICAL_DRIVE_CONFI_5_3': physical_drive_confi_3,'PHYSICAL_DRIVE_FW_5_3': physical_drive_fw_3,
    'PHYSICAL_DRIVE_LABEL_5_4': physical_drive_label_4,'PHYSICAL_DRIVE_STATUS_5_4': physical_drive_status_4,'PHYSICAL_DRIVE_MODEL_5_4': physical_drive_model_4,'PHYSICAL_DRIVE_CAPACITY_5_4': physical_drive_capacity_4,'PHYSICAL_DRIVE_SN_5_4': physical_drive_sn_4,'PHYSICAL_DRIVE_CONFI_5_4': physical_drive_confi_4,'PHYSICAL_DRIVE_FW_5_4': physical_drive_fw_4,
    'PHYSICAL_DRIVE_LABEL_5_5': physical_drive_label_5,'PHYSICAL_DRIVE_STATUS_5_5': physical_drive_status_5,'PHYSICAL_DRIVE_MODEL_5_5': physical_drive_model_5,'PHYSICAL_DRIVE_CAPACITY_5_5': physical_drive_capacity_5,'PHYSICAL_DRIVE_SN_5_5': physical_drive_sn_5,'PHYSICAL_DRIVE_CONFI_5_5': physical_drive_confi_5,'PHYSICAL_DRIVE_FW_5_5': physical_drive_fw_5,
    'PHYSICAL_DRIVE_LABEL_5_6': physical_drive_label_6,'PHYSICAL_DRIVE_STATUS_5_6': physical_drive_status_6,'PHYSICAL_DRIVE_MODEL_5_6': physical_drive_model_6,'PHYSICAL_DRIVE_CAPACITY_5_6': physical_drive_capacity_6,'PHYSICAL_DRIVE_SN_5_6': physical_drive_sn_6,'PHYSICAL_DRIVE_CONFI_5_6': physical_drive_confi_6,'PHYSICAL_DRIVE_FW_5_6': physical_drive_fw_6,
    'PHYSICAL_DRIVE_LABEL_5_7': physical_drive_label_7,'PHYSICAL_DRIVE_STATUS_5_7': physical_drive_status_7,'PHYSICAL_DRIVE_MODEL_5_7': physical_drive_model_7,'PHYSICAL_DRIVE_CAPACITY_5_7': physical_drive_capacity_7,'PHYSICAL_DRIVE_SN_5_7': physical_drive_sn_7,'PHYSICAL_DRIVE_CONFI_5_7': physical_drive_confi_7,'PHYSICAL_DRIVE_FW_5_7': physical_drive_fw_7,
    'PHYSICAL_DRIVE_LABEL_5_8': physical_drive_label_8,'PHYSICAL_DRIVE_STATUS_5_8': physical_drive_status_8,'PHYSICAL_DRIVE_MODEL_5_8': physical_drive_model_8,'PHYSICAL_DRIVE_CAPACITY_5_8': physical_drive_capacity_8,'PHYSICAL_DRIVE_SN_5_8': physical_drive_sn_8,'PHYSICAL_DRIVE_CONFI_5_8': physical_drive_confi_8,'PHYSICAL_DRIVE_FW_5_8': physical_drive_fw_8,
    'PHYSICAL_DRIVE_LABEL_5_9': physical_drive_label_9,'PHYSICAL_DRIVE_STATUS_5_9': physical_drive_status_9,'PHYSICAL_DRIVE_MODEL_5_9': physical_drive_model_9,'PHYSICAL_DRIVE_CAPACITY_5_9': physical_drive_capacity_9,'PHYSICAL_DRIVE_SN_5_9': physical_drive_sn_9,'PHYSICAL_DRIVE_CONFI_5_9': physical_drive_confi_9,'PHYSICAL_DRIVE_FW_5_9': physical_drive_fw_9,
    'PHYSICAL_DRIVE_LABEL_5_10': physical_drive_label_10,'PHYSICAL_DRIVE_STATUS_5_10': physical_drive_status_10,'PHYSICAL_DRIVE_MODEL_5_10': physical_drive_model_10,'PHYSICAL_DRIVE_CAPACITY_5_10': physical_drive_capacity_10, 'PHYSICAL_DRIVE_SN_5_10': physical_drive_sn_10,'PHYSICAL_DRIVE_CONFI_5_10': physical_drive_confi_10, 'PHYSICAL_DRIVE_FW_5_10': physical_drive_fw_10,
    'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update STORAGE_INFO set LOGICAL_DRIVE_5=:LOGICAL_DRIVE_5,LOGICAL_DRIVE_STATUS_5=:LOGICAL_DRIVE_STATUS_5,LOGICAL_DRIVE_CAPACITY_5=:LOGICAL_DRIVE_CAPACITY_5,LOGICAL_DRIVE_TOLERANCE_5=:LOGICAL_DRIVE_TOLERANCE_5,LOGICAL_DRIVE_TYPE_5=:LOGICAL_DRIVE_TYPE_5, \
                         PHYSICAL_DRIVE_LABEL_5_1=:PHYSICAL_DRIVE_LABEL_5_1 ,PHYSICAL_DRIVE_STATUS_5_1=:PHYSICAL_DRIVE_STATUS_5_1,PHYSICAL_DRIVE_MODEL_5_1=:PHYSICAL_DRIVE_MODEL_5_1,PHYSICAL_DRIVE_CAPACITY_5_1=:PHYSICAL_DRIVE_CAPACITY_5_1,PHYSICAL_DRIVE_SN_5_1=:PHYSICAL_DRIVE_SN_5_1,PHYSICAL_DRIVE_CONFI_5_1=:PHYSICAL_DRIVE_CONFI_5_1,PHYSICAL_DRIVE_FW_5_1=:PHYSICAL_DRIVE_FW_5_1, \
                         PHYSICAL_DRIVE_LABEL_5_2=:PHYSICAL_DRIVE_LABEL_5_2 ,PHYSICAL_DRIVE_STATUS_5_2=:PHYSICAL_DRIVE_STATUS_5_2,PHYSICAL_DRIVE_MODEL_5_2=:PHYSICAL_DRIVE_MODEL_5_2,PHYSICAL_DRIVE_CAPACITY_5_2=:PHYSICAL_DRIVE_CAPACITY_5_2,PHYSICAL_DRIVE_SN_5_2=:PHYSICAL_DRIVE_SN_5_2,PHYSICAL_DRIVE_CONFI_5_2=:PHYSICAL_DRIVE_CONFI_5_2,PHYSICAL_DRIVE_FW_5_2=:PHYSICAL_DRIVE_FW_5_2, \
                         PHYSICAL_DRIVE_LABEL_5_3=:PHYSICAL_DRIVE_LABEL_5_3 ,PHYSICAL_DRIVE_STATUS_5_3=:PHYSICAL_DRIVE_STATUS_5_3,PHYSICAL_DRIVE_MODEL_5_3=:PHYSICAL_DRIVE_MODEL_5_3,PHYSICAL_DRIVE_CAPACITY_5_3=:PHYSICAL_DRIVE_CAPACITY_5_3,PHYSICAL_DRIVE_SN_5_3=:PHYSICAL_DRIVE_SN_5_3,PHYSICAL_DRIVE_CONFI_5_3=:PHYSICAL_DRIVE_CONFI_5_3,PHYSICAL_DRIVE_FW_5_3=:PHYSICAL_DRIVE_FW_5_3, \
                         PHYSICAL_DRIVE_LABEL_5_4=:PHYSICAL_DRIVE_LABEL_5_4 ,PHYSICAL_DRIVE_STATUS_5_4=:PHYSICAL_DRIVE_STATUS_5_4,PHYSICAL_DRIVE_MODEL_5_4=:PHYSICAL_DRIVE_MODEL_5_4,PHYSICAL_DRIVE_CAPACITY_5_4=:PHYSICAL_DRIVE_CAPACITY_5_4,PHYSICAL_DRIVE_SN_5_4=:PHYSICAL_DRIVE_SN_5_4,PHYSICAL_DRIVE_CONFI_5_4=:PHYSICAL_DRIVE_CONFI_5_4,PHYSICAL_DRIVE_FW_5_4=:PHYSICAL_DRIVE_FW_5_4, \
                         PHYSICAL_DRIVE_LABEL_5_5=:PHYSICAL_DRIVE_LABEL_5_5 ,PHYSICAL_DRIVE_STATUS_5_5=:PHYSICAL_DRIVE_STATUS_5_5,PHYSICAL_DRIVE_MODEL_5_5=:PHYSICAL_DRIVE_MODEL_5_5,PHYSICAL_DRIVE_CAPACITY_5_5=:PHYSICAL_DRIVE_CAPACITY_5_5,PHYSICAL_DRIVE_SN_5_5=:PHYSICAL_DRIVE_SN_5_5,PHYSICAL_DRIVE_CONFI_5_5=:PHYSICAL_DRIVE_CONFI_5_5,PHYSICAL_DRIVE_FW_5_5=:PHYSICAL_DRIVE_FW_5_5, \
                         PHYSICAL_DRIVE_LABEL_5_6=:PHYSICAL_DRIVE_LABEL_5_6 ,PHYSICAL_DRIVE_STATUS_5_6=:PHYSICAL_DRIVE_STATUS_5_6,PHYSICAL_DRIVE_MODEL_5_6=:PHYSICAL_DRIVE_MODEL_5_6,PHYSICAL_DRIVE_CAPACITY_5_6=:PHYSICAL_DRIVE_CAPACITY_5_6,PHYSICAL_DRIVE_SN_5_6=:PHYSICAL_DRIVE_SN_5_6,PHYSICAL_DRIVE_CONFI_5_6=:PHYSICAL_DRIVE_CONFI_5_6,PHYSICAL_DRIVE_FW_5_6=:PHYSICAL_DRIVE_FW_5_6, \
                         PHYSICAL_DRIVE_LABEL_5_7=:PHYSICAL_DRIVE_LABEL_5_7 ,PHYSICAL_DRIVE_STATUS_5_7=:PHYSICAL_DRIVE_STATUS_5_7,PHYSICAL_DRIVE_MODEL_5_7=:PHYSICAL_DRIVE_MODEL_5_7,PHYSICAL_DRIVE_CAPACITY_5_7=:PHYSICAL_DRIVE_CAPACITY_5_7,PHYSICAL_DRIVE_SN_5_7=:PHYSICAL_DRIVE_SN_5_7,PHYSICAL_DRIVE_CONFI_5_7=:PHYSICAL_DRIVE_CONFI_5_7,PHYSICAL_DRIVE_FW_5_7=:PHYSICAL_DRIVE_FW_5_7, \
                         PHYSICAL_DRIVE_LABEL_5_8=:PHYSICAL_DRIVE_LABEL_5_8 ,PHYSICAL_DRIVE_STATUS_5_8=:PHYSICAL_DRIVE_STATUS_5_8,PHYSICAL_DRIVE_MODEL_5_8=:PHYSICAL_DRIVE_MODEL_5_8,PHYSICAL_DRIVE_CAPACITY_5_8=:PHYSICAL_DRIVE_CAPACITY_5_8,PHYSICAL_DRIVE_SN_5_8=:PHYSICAL_DRIVE_SN_5_8,PHYSICAL_DRIVE_CONFI_5_8=:PHYSICAL_DRIVE_CONFI_5_8,PHYSICAL_DRIVE_FW_5_8=:PHYSICAL_DRIVE_FW_5_8, \
                         PHYSICAL_DRIVE_LABEL_5_9=:PHYSICAL_DRIVE_LABEL_5_9 ,PHYSICAL_DRIVE_STATUS_5_9=:PHYSICAL_DRIVE_STATUS_5_9,PHYSICAL_DRIVE_MODEL_5_9=:PHYSICAL_DRIVE_MODEL_5_9,PHYSICAL_DRIVE_CAPACITY_5_9=:PHYSICAL_DRIVE_CAPACITY_5_9,PHYSICAL_DRIVE_SN_5_9=:PHYSICAL_DRIVE_SN_5_9,PHYSICAL_DRIVE_CONFI_5_9=:PHYSICAL_DRIVE_CONFI_5_9,PHYSICAL_DRIVE_FW_5_9=:PHYSICAL_DRIVE_FW_5_9, \
                         PHYSICAL_DRIVE_LABEL_5_10=:PHYSICAL_DRIVE_LABEL_5_10 ,PHYSICAL_DRIVE_STATUS_5_10=:PHYSICAL_DRIVE_STATUS_5_10,PHYSICAL_DRIVE_MODEL_5_10=:PHYSICAL_DRIVE_MODEL_5_10,PHYSICAL_DRIVE_CAPACITY_5_10=:PHYSICAL_DRIVE_CAPACITY_5_10,PHYSICAL_DRIVE_SN_5_10=:PHYSICAL_DRIVE_SN_5_10,PHYSICAL_DRIVE_CONFI_5_10=:PHYSICAL_DRIVE_CONFI_5_10,PHYSICAL_DRIVE_FW_5_10=:PHYSICAL_DRIVE_FW_5_10 where IP_ILO=:IP_ILO',
                         param)
    connection.commit()
    connection.close()

def update_storage_6_info(logical_drive=None,logical_drive_status=None,logical_drive_capacity=None,logical_drive_tolerance=None,logical_drive_type=None,physical_drive_label_1=None,physical_drive_status_1=None,physical_drive_capacity_1=None,physical_drive_model_1=None,physical_drive_sn_1=None,physical_drive_confi_1=None,physical_drive_fw_1=None,
                                                                                                                               physical_drive_label_2=None,physical_drive_status_2=None,physical_drive_capacity_2=None,physical_drive_model_2=None,physical_drive_sn_2=None,physical_drive_confi_2=None,physical_drive_fw_2=None,
                                                                                                                               physical_drive_label_3=None,physical_drive_status_3=None,physical_drive_capacity_3=None,physical_drive_model_3=None,physical_drive_sn_3=None,physical_drive_confi_3=None,physical_drive_fw_3=None,
                                                                                                                               physical_drive_label_4=None,physical_drive_status_4=None,physical_drive_capacity_4=None,physical_drive_model_4=None,physical_drive_sn_4=None,physical_drive_confi_4=None,physical_drive_fw_4=None,
                                                                                                                               physical_drive_label_5=None,physical_drive_status_5=None,physical_drive_capacity_5=None,physical_drive_model_5=None,physical_drive_sn_5=None,physical_drive_confi_5=None,physical_drive_fw_5=None,
                                                                                                                               physical_drive_label_6=None,physical_drive_status_6=None,physical_drive_capacity_6=None,physical_drive_model_6=None,physical_drive_sn_6=None,physical_drive_confi_6=None,physical_drive_fw_6=None,
                                                                                                                               physical_drive_label_7=None,physical_drive_status_7=None,physical_drive_capacity_7=None,physical_drive_model_7=None,physical_drive_sn_7=None,physical_drive_confi_7=None,physical_drive_fw_7=None,
                                                                                                                               physical_drive_label_8=None,physical_drive_status_8=None,physical_drive_capacity_8=None,physical_drive_model_8=None,physical_drive_sn_8=None,physical_drive_confi_8=None,physical_drive_fw_8=None,
                                                                                                                               physical_drive_label_9=None,physical_drive_status_9=None,physical_drive_capacity_9=None,physical_drive_model_9=None,physical_drive_sn_9=None,physical_drive_confi_9=None,physical_drive_fw_9=None,
                                                                                                                               physical_drive_label_10=None,physical_drive_status_10=None,physical_drive_capacity_10=None,physical_drive_model_10=None,physical_drive_sn_10=None,physical_drive_confi_10=None,physical_drive_fw_10=None,
                                                                                                                               ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'LOGICAL_DRIVE_6': logical_drive, 'LOGICAL_DRIVE_STATUS_6': logical_drive_status, 'LOGICAL_DRIVE_CAPACITY_6': logical_drive_capacity,'LOGICAL_DRIVE_TOLERANCE_6': logical_drive_tolerance,'LOGICAL_DRIVE_TYPE_6': logical_drive_type,
    'PHYSICAL_DRIVE_LABEL_6_1': physical_drive_label_1,'PHYSICAL_DRIVE_STATUS_6_1': physical_drive_status_1,'PHYSICAL_DRIVE_MODEL_6_1': physical_drive_model_1,'PHYSICAL_DRIVE_CAPACITY_6_1': physical_drive_capacity_1,'PHYSICAL_DRIVE_SN_6_1': physical_drive_sn_1,'PHYSICAL_DRIVE_CONFI_6_1': physical_drive_confi_1,'PHYSICAL_DRIVE_FW_6_1': physical_drive_fw_1,
    'PHYSICAL_DRIVE_LABEL_6_2': physical_drive_label_2,'PHYSICAL_DRIVE_STATUS_6_2': physical_drive_status_2,'PHYSICAL_DRIVE_MODEL_6_2': physical_drive_model_2,'PHYSICAL_DRIVE_CAPACITY_6_2': physical_drive_capacity_2,'PHYSICAL_DRIVE_SN_6_2': physical_drive_sn_2,'PHYSICAL_DRIVE_CONFI_6_2': physical_drive_confi_2,'PHYSICAL_DRIVE_FW_6_2': physical_drive_fw_2,
    'PHYSICAL_DRIVE_LABEL_6_3': physical_drive_label_3,'PHYSICAL_DRIVE_STATUS_6_3': physical_drive_status_3,'PHYSICAL_DRIVE_MODEL_6_3': physical_drive_model_3,'PHYSICAL_DRIVE_CAPACITY_6_3': physical_drive_capacity_3,'PHYSICAL_DRIVE_SN_6_3': physical_drive_sn_3,'PHYSICAL_DRIVE_CONFI_6_3': physical_drive_confi_3,'PHYSICAL_DRIVE_FW_6_3': physical_drive_fw_3,
    'PHYSICAL_DRIVE_LABEL_6_4': physical_drive_label_4,'PHYSICAL_DRIVE_STATUS_6_4': physical_drive_status_4,'PHYSICAL_DRIVE_MODEL_6_4': physical_drive_model_4,'PHYSICAL_DRIVE_CAPACITY_6_4': physical_drive_capacity_4,'PHYSICAL_DRIVE_SN_6_4': physical_drive_sn_4,'PHYSICAL_DRIVE_CONFI_6_4': physical_drive_confi_4,'PHYSICAL_DRIVE_FW_6_4': physical_drive_fw_4,
    'PHYSICAL_DRIVE_LABEL_6_5': physical_drive_label_5,'PHYSICAL_DRIVE_STATUS_6_5': physical_drive_status_5,'PHYSICAL_DRIVE_MODEL_6_5': physical_drive_model_5,'PHYSICAL_DRIVE_CAPACITY_6_5': physical_drive_capacity_5,'PHYSICAL_DRIVE_SN_6_5': physical_drive_sn_5,'PHYSICAL_DRIVE_CONFI_6_5': physical_drive_confi_5,'PHYSICAL_DRIVE_FW_6_5': physical_drive_fw_5,
    'PHYSICAL_DRIVE_LABEL_6_6': physical_drive_label_6,'PHYSICAL_DRIVE_STATUS_6_6': physical_drive_status_6,'PHYSICAL_DRIVE_MODEL_6_6': physical_drive_model_6,'PHYSICAL_DRIVE_CAPACITY_6_6': physical_drive_capacity_6,'PHYSICAL_DRIVE_SN_6_6': physical_drive_sn_6,'PHYSICAL_DRIVE_CONFI_6_6': physical_drive_confi_6,'PHYSICAL_DRIVE_FW_6_6': physical_drive_fw_6,
    'PHYSICAL_DRIVE_LABEL_6_7': physical_drive_label_7,'PHYSICAL_DRIVE_STATUS_6_7': physical_drive_status_7,'PHYSICAL_DRIVE_MODEL_6_7': physical_drive_model_7,'PHYSICAL_DRIVE_CAPACITY_6_7': physical_drive_capacity_7,'PHYSICAL_DRIVE_SN_6_7': physical_drive_sn_7,'PHYSICAL_DRIVE_CONFI_6_7': physical_drive_confi_7,'PHYSICAL_DRIVE_FW_6_7': physical_drive_fw_7,
    'PHYSICAL_DRIVE_LABEL_6_8': physical_drive_label_8,'PHYSICAL_DRIVE_STATUS_6_8': physical_drive_status_8,'PHYSICAL_DRIVE_MODEL_6_8': physical_drive_model_8,'PHYSICAL_DRIVE_CAPACITY_6_8': physical_drive_capacity_8,'PHYSICAL_DRIVE_SN_6_8': physical_drive_sn_8,'PHYSICAL_DRIVE_CONFI_6_8': physical_drive_confi_8,'PHYSICAL_DRIVE_FW_6_8': physical_drive_fw_8,
    'PHYSICAL_DRIVE_LABEL_6_9': physical_drive_label_9,'PHYSICAL_DRIVE_STATUS_6_9': physical_drive_status_9,'PHYSICAL_DRIVE_MODEL_6_9': physical_drive_model_9,'PHYSICAL_DRIVE_CAPACITY_6_9': physical_drive_capacity_9,'PHYSICAL_DRIVE_SN_6_9': physical_drive_sn_9,'PHYSICAL_DRIVE_CONFI_6_9': physical_drive_confi_9,'PHYSICAL_DRIVE_FW_6_9': physical_drive_fw_9,
    'PHYSICAL_DRIVE_LABEL_6_10': physical_drive_label_10,'PHYSICAL_DRIVE_STATUS_6_10': physical_drive_status_10,'PHYSICAL_DRIVE_MODEL_6_10': physical_drive_model_10,'PHYSICAL_DRIVE_CAPACITY_6_10': physical_drive_capacity_10, 'PHYSICAL_DRIVE_SN_6_10': physical_drive_sn_10,'PHYSICAL_DRIVE_CONFI_6_10': physical_drive_confi_10, 'PHYSICAL_DRIVE_FW_6_10': physical_drive_fw_10,
    'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update STORAGE_INFO set LOGICAL_DRIVE_6=:LOGICAL_DRIVE_6,LOGICAL_DRIVE_STATUS_6=:LOGICAL_DRIVE_STATUS_6,LOGICAL_DRIVE_CAPACITY_6=:LOGICAL_DRIVE_CAPACITY_6,LOGICAL_DRIVE_TOLERANCE_6=:LOGICAL_DRIVE_TOLERANCE_6,LOGICAL_DRIVE_TYPE_6=:LOGICAL_DRIVE_TYPE_6, \
                         PHYSICAL_DRIVE_LABEL_6_1=:PHYSICAL_DRIVE_LABEL_6_1 ,PHYSICAL_DRIVE_STATUS_6_1=:PHYSICAL_DRIVE_STATUS_6_1,PHYSICAL_DRIVE_MODEL_6_1=:PHYSICAL_DRIVE_MODEL_6_1,PHYSICAL_DRIVE_CAPACITY_6_1=:PHYSICAL_DRIVE_CAPACITY_6_1,PHYSICAL_DRIVE_SN_6_1=:PHYSICAL_DRIVE_SN_6_1,PHYSICAL_DRIVE_CONFI_6_1=:PHYSICAL_DRIVE_CONFI_6_1,PHYSICAL_DRIVE_FW_6_1=:PHYSICAL_DRIVE_FW_6_1, \
                         PHYSICAL_DRIVE_LABEL_6_2=:PHYSICAL_DRIVE_LABEL_6_2 ,PHYSICAL_DRIVE_STATUS_6_2=:PHYSICAL_DRIVE_STATUS_6_2,PHYSICAL_DRIVE_MODEL_6_2=:PHYSICAL_DRIVE_MODEL_6_2,PHYSICAL_DRIVE_CAPACITY_6_2=:PHYSICAL_DRIVE_CAPACITY_6_2,PHYSICAL_DRIVE_SN_6_2=:PHYSICAL_DRIVE_SN_6_2,PHYSICAL_DRIVE_CONFI_6_2=:PHYSICAL_DRIVE_CONFI_6_2,PHYSICAL_DRIVE_FW_6_2=:PHYSICAL_DRIVE_FW_6_2, \
                         PHYSICAL_DRIVE_LABEL_6_3=:PHYSICAL_DRIVE_LABEL_6_3 ,PHYSICAL_DRIVE_STATUS_6_3=:PHYSICAL_DRIVE_STATUS_6_3,PHYSICAL_DRIVE_MODEL_6_3=:PHYSICAL_DRIVE_MODEL_6_3,PHYSICAL_DRIVE_CAPACITY_6_3=:PHYSICAL_DRIVE_CAPACITY_6_3,PHYSICAL_DRIVE_SN_6_3=:PHYSICAL_DRIVE_SN_6_3,PHYSICAL_DRIVE_CONFI_6_3=:PHYSICAL_DRIVE_CONFI_6_3,PHYSICAL_DRIVE_FW_6_3=:PHYSICAL_DRIVE_FW_6_3, \
                         PHYSICAL_DRIVE_LABEL_6_4=:PHYSICAL_DRIVE_LABEL_6_4 ,PHYSICAL_DRIVE_STATUS_6_4=:PHYSICAL_DRIVE_STATUS_6_4,PHYSICAL_DRIVE_MODEL_6_4=:PHYSICAL_DRIVE_MODEL_6_4,PHYSICAL_DRIVE_CAPACITY_6_4=:PHYSICAL_DRIVE_CAPACITY_6_4,PHYSICAL_DRIVE_SN_6_4=:PHYSICAL_DRIVE_SN_6_4,PHYSICAL_DRIVE_CONFI_6_4=:PHYSICAL_DRIVE_CONFI_6_4,PHYSICAL_DRIVE_FW_6_4=:PHYSICAL_DRIVE_FW_6_4, \
                         PHYSICAL_DRIVE_LABEL_6_5=:PHYSICAL_DRIVE_LABEL_6_5 ,PHYSICAL_DRIVE_STATUS_6_5=:PHYSICAL_DRIVE_STATUS_6_5,PHYSICAL_DRIVE_MODEL_6_5=:PHYSICAL_DRIVE_MODEL_6_5,PHYSICAL_DRIVE_CAPACITY_6_5=:PHYSICAL_DRIVE_CAPACITY_6_5,PHYSICAL_DRIVE_SN_6_5=:PHYSICAL_DRIVE_SN_6_5,PHYSICAL_DRIVE_CONFI_6_5=:PHYSICAL_DRIVE_CONFI_6_5,PHYSICAL_DRIVE_FW_6_5=:PHYSICAL_DRIVE_FW_6_5, \
                         PHYSICAL_DRIVE_LABEL_6_6=:PHYSICAL_DRIVE_LABEL_6_6 ,PHYSICAL_DRIVE_STATUS_6_6=:PHYSICAL_DRIVE_STATUS_6_6,PHYSICAL_DRIVE_MODEL_6_6=:PHYSICAL_DRIVE_MODEL_6_6,PHYSICAL_DRIVE_CAPACITY_6_6=:PHYSICAL_DRIVE_CAPACITY_6_6,PHYSICAL_DRIVE_SN_6_6=:PHYSICAL_DRIVE_SN_6_6,PHYSICAL_DRIVE_CONFI_6_6=:PHYSICAL_DRIVE_CONFI_6_6,PHYSICAL_DRIVE_FW_6_6=:PHYSICAL_DRIVE_FW_6_6, \
                         PHYSICAL_DRIVE_LABEL_6_7=:PHYSICAL_DRIVE_LABEL_6_7 ,PHYSICAL_DRIVE_STATUS_6_7=:PHYSICAL_DRIVE_STATUS_6_7,PHYSICAL_DRIVE_MODEL_6_7=:PHYSICAL_DRIVE_MODEL_6_7,PHYSICAL_DRIVE_CAPACITY_6_7=:PHYSICAL_DRIVE_CAPACITY_6_7,PHYSICAL_DRIVE_SN_6_7=:PHYSICAL_DRIVE_SN_6_7,PHYSICAL_DRIVE_CONFI_6_7=:PHYSICAL_DRIVE_CONFI_6_7,PHYSICAL_DRIVE_FW_6_7=:PHYSICAL_DRIVE_FW_6_7, \
                         PHYSICAL_DRIVE_LABEL_6_8=:PHYSICAL_DRIVE_LABEL_6_8 ,PHYSICAL_DRIVE_STATUS_6_8=:PHYSICAL_DRIVE_STATUS_6_8,PHYSICAL_DRIVE_MODEL_6_8=:PHYSICAL_DRIVE_MODEL_6_8,PHYSICAL_DRIVE_CAPACITY_6_8=:PHYSICAL_DRIVE_CAPACITY_6_8,PHYSICAL_DRIVE_SN_6_8=:PHYSICAL_DRIVE_SN_6_8,PHYSICAL_DRIVE_CONFI_6_8=:PHYSICAL_DRIVE_CONFI_6_8,PHYSICAL_DRIVE_FW_6_8=:PHYSICAL_DRIVE_FW_6_8, \
                         PHYSICAL_DRIVE_LABEL_6_9=:PHYSICAL_DRIVE_LABEL_6_9 ,PHYSICAL_DRIVE_STATUS_6_9=:PHYSICAL_DRIVE_STATUS_6_9,PHYSICAL_DRIVE_MODEL_6_9=:PHYSICAL_DRIVE_MODEL_6_9,PHYSICAL_DRIVE_CAPACITY_6_9=:PHYSICAL_DRIVE_CAPACITY_6_9,PHYSICAL_DRIVE_SN_6_9=:PHYSICAL_DRIVE_SN_6_9,PHYSICAL_DRIVE_CONFI_6_9=:PHYSICAL_DRIVE_CONFI_6_9,PHYSICAL_DRIVE_FW_6_9=:PHYSICAL_DRIVE_FW_6_9, \
                         PHYSICAL_DRIVE_LABEL_6_10=:PHYSICAL_DRIVE_LABEL_6_10 ,PHYSICAL_DRIVE_STATUS_6_10=:PHYSICAL_DRIVE_STATUS_6_10,PHYSICAL_DRIVE_MODEL_6_10=:PHYSICAL_DRIVE_MODEL_6_10,PHYSICAL_DRIVE_CAPACITY_6_10=:PHYSICAL_DRIVE_CAPACITY_6_10,PHYSICAL_DRIVE_SN_6_10=:PHYSICAL_DRIVE_SN_6_10,PHYSICAL_DRIVE_CONFI_6_10=:PHYSICAL_DRIVE_CONFI_6_10,PHYSICAL_DRIVE_FW_6_10=:PHYSICAL_DRIVE_FW_6_10 where IP_ILO=:IP_ILO',
                         param)
    connection.commit()
    connection.close()

def update_storage_7_info(logical_drive=None,logical_drive_status=None,logical_drive_capacity=None,logical_drive_tolerance=None,logical_drive_type=None,physical_drive_label_1=None,physical_drive_status_1=None,physical_drive_capacity_1=None,physical_drive_model_1=None,physical_drive_sn_1=None,physical_drive_confi_1=None,physical_drive_fw_1=None,
                                                                                                                               physical_drive_label_2=None,physical_drive_status_2=None,physical_drive_capacity_2=None,physical_drive_model_2=None,physical_drive_sn_2=None,physical_drive_confi_2=None,physical_drive_fw_2=None,
                                                                                                                               physical_drive_label_3=None,physical_drive_status_3=None,physical_drive_capacity_3=None,physical_drive_model_3=None,physical_drive_sn_3=None,physical_drive_confi_3=None,physical_drive_fw_3=None,
                                                                                                                               physical_drive_label_4=None,physical_drive_status_4=None,physical_drive_capacity_4=None,physical_drive_model_4=None,physical_drive_sn_4=None,physical_drive_confi_4=None,physical_drive_fw_4=None,
                                                                                                                               physical_drive_label_5=None,physical_drive_status_5=None,physical_drive_capacity_5=None,physical_drive_model_5=None,physical_drive_sn_5=None,physical_drive_confi_5=None,physical_drive_fw_5=None,
                                                                                                                               physical_drive_label_6=None,physical_drive_status_6=None,physical_drive_capacity_6=None,physical_drive_model_6=None,physical_drive_sn_6=None,physical_drive_confi_6=None,physical_drive_fw_6=None,
                                                                                                                               physical_drive_label_7=None,physical_drive_status_7=None,physical_drive_capacity_7=None,physical_drive_model_7=None,physical_drive_sn_7=None,physical_drive_confi_7=None,physical_drive_fw_7=None,
                                                                                                                               physical_drive_label_8=None,physical_drive_status_8=None,physical_drive_capacity_8=None,physical_drive_model_8=None,physical_drive_sn_8=None,physical_drive_confi_8=None,physical_drive_fw_8=None,
                                                                                                                               physical_drive_label_9=None,physical_drive_status_9=None,physical_drive_capacity_9=None,physical_drive_model_9=None,physical_drive_sn_9=None,physical_drive_confi_9=None,physical_drive_fw_9=None,
                                                                                                                               physical_drive_label_10=None,physical_drive_status_10=None,physical_drive_capacity_10=None,physical_drive_model_10=None,physical_drive_sn_10=None,physical_drive_confi_10=None,physical_drive_fw_10=None,
                                                                                                                               ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'LOGICAL_DRIVE_7': logical_drive, 'LOGICAL_DRIVE_STATUS_7': logical_drive_status, 'LOGICAL_DRIVE_CAPACITY_7': logical_drive_capacity,'LOGICAL_DRIVE_TOLERANCE_7': logical_drive_tolerance,'LOGICAL_DRIVE_TYPE_7': logical_drive_type,
    'PHYSICAL_DRIVE_LABEL_7_1': physical_drive_label_1,'PHYSICAL_DRIVE_STATUS_7_1': physical_drive_status_1,'PHYSICAL_DRIVE_MODEL_7_1': physical_drive_model_1,'PHYSICAL_DRIVE_CAPACITY_7_1': physical_drive_capacity_1,'PHYSICAL_DRIVE_SN_7_1': physical_drive_sn_1,'PHYSICAL_DRIVE_CONFI_7_1': physical_drive_confi_1,'PHYSICAL_DRIVE_FW_7_1': physical_drive_fw_1,
    'PHYSICAL_DRIVE_LABEL_7_2': physical_drive_label_2,'PHYSICAL_DRIVE_STATUS_7_2': physical_drive_status_2,'PHYSICAL_DRIVE_MODEL_7_2': physical_drive_model_2,'PHYSICAL_DRIVE_CAPACITY_7_2': physical_drive_capacity_2,'PHYSICAL_DRIVE_SN_7_2': physical_drive_sn_2,'PHYSICAL_DRIVE_CONFI_7_2': physical_drive_confi_2,'PHYSICAL_DRIVE_FW_7_2': physical_drive_fw_2,
    'PHYSICAL_DRIVE_LABEL_7_3': physical_drive_label_3,'PHYSICAL_DRIVE_STATUS_7_3': physical_drive_status_3,'PHYSICAL_DRIVE_MODEL_7_3': physical_drive_model_3,'PHYSICAL_DRIVE_CAPACITY_7_3': physical_drive_capacity_3,'PHYSICAL_DRIVE_SN_7_3': physical_drive_sn_3,'PHYSICAL_DRIVE_CONFI_7_3': physical_drive_confi_3,'PHYSICAL_DRIVE_FW_7_3': physical_drive_fw_3,
    'PHYSICAL_DRIVE_LABEL_7_4': physical_drive_label_4,'PHYSICAL_DRIVE_STATUS_7_4': physical_drive_status_4,'PHYSICAL_DRIVE_MODEL_7_4': physical_drive_model_4,'PHYSICAL_DRIVE_CAPACITY_7_4': physical_drive_capacity_4,'PHYSICAL_DRIVE_SN_7_4': physical_drive_sn_4,'PHYSICAL_DRIVE_CONFI_7_4': physical_drive_confi_4,'PHYSICAL_DRIVE_FW_7_4': physical_drive_fw_4,
    'PHYSICAL_DRIVE_LABEL_7_5': physical_drive_label_5,'PHYSICAL_DRIVE_STATUS_7_5': physical_drive_status_5,'PHYSICAL_DRIVE_MODEL_7_5': physical_drive_model_5,'PHYSICAL_DRIVE_CAPACITY_7_5': physical_drive_capacity_5,'PHYSICAL_DRIVE_SN_7_5': physical_drive_sn_5,'PHYSICAL_DRIVE_CONFI_7_5': physical_drive_confi_5,'PHYSICAL_DRIVE_FW_7_5': physical_drive_fw_5,
    'PHYSICAL_DRIVE_LABEL_7_6': physical_drive_label_6,'PHYSICAL_DRIVE_STATUS_7_6': physical_drive_status_6,'PHYSICAL_DRIVE_MODEL_7_6': physical_drive_model_6,'PHYSICAL_DRIVE_CAPACITY_7_6': physical_drive_capacity_6,'PHYSICAL_DRIVE_SN_7_6': physical_drive_sn_6,'PHYSICAL_DRIVE_CONFI_7_6': physical_drive_confi_6,'PHYSICAL_DRIVE_FW_7_6': physical_drive_fw_6,
    'PHYSICAL_DRIVE_LABEL_7_7': physical_drive_label_7,'PHYSICAL_DRIVE_STATUS_7_7': physical_drive_status_7,'PHYSICAL_DRIVE_MODEL_7_7': physical_drive_model_7,'PHYSICAL_DRIVE_CAPACITY_7_7': physical_drive_capacity_7,'PHYSICAL_DRIVE_SN_7_7': physical_drive_sn_7,'PHYSICAL_DRIVE_CONFI_7_7': physical_drive_confi_7,'PHYSICAL_DRIVE_FW_7_7': physical_drive_fw_7,
    'PHYSICAL_DRIVE_LABEL_7_8': physical_drive_label_8,'PHYSICAL_DRIVE_STATUS_7_8': physical_drive_status_8,'PHYSICAL_DRIVE_MODEL_7_8': physical_drive_model_8,'PHYSICAL_DRIVE_CAPACITY_7_8': physical_drive_capacity_8,'PHYSICAL_DRIVE_SN_7_8': physical_drive_sn_8,'PHYSICAL_DRIVE_CONFI_7_8': physical_drive_confi_8,'PHYSICAL_DRIVE_FW_7_8': physical_drive_fw_8,
    'PHYSICAL_DRIVE_LABEL_7_9': physical_drive_label_9,'PHYSICAL_DRIVE_STATUS_7_9': physical_drive_status_9,'PHYSICAL_DRIVE_MODEL_7_9': physical_drive_model_9,'PHYSICAL_DRIVE_CAPACITY_7_9': physical_drive_capacity_9,'PHYSICAL_DRIVE_SN_7_9': physical_drive_sn_9,'PHYSICAL_DRIVE_CONFI_7_9': physical_drive_confi_9,'PHYSICAL_DRIVE_FW_7_9': physical_drive_fw_9,
    'PHYSICAL_DRIVE_LABEL_7_10': physical_drive_label_10,'PHYSICAL_DRIVE_STATUS_7_10': physical_drive_status_10,'PHYSICAL_DRIVE_MODEL_7_10': physical_drive_model_10,'PHYSICAL_DRIVE_CAPACITY_7_10': physical_drive_capacity_10, 'PHYSICAL_DRIVE_SN_7_10': physical_drive_sn_10,'PHYSICAL_DRIVE_CONFI_7_10': physical_drive_confi_10, 'PHYSICAL_DRIVE_FW_7_10': physical_drive_fw_10,
    'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update STORAGE_INFO set LOGICAL_DRIVE_7=:LOGICAL_DRIVE_7,LOGICAL_DRIVE_STATUS_7=:LOGICAL_DRIVE_STATUS_7,LOGICAL_DRIVE_CAPACITY_7=:LOGICAL_DRIVE_CAPACITY_7,LOGICAL_DRIVE_TOLERANCE_7=:LOGICAL_DRIVE_TOLERANCE_7,LOGICAL_DRIVE_TYPE_7=:LOGICAL_DRIVE_TYPE_7, \
                         PHYSICAL_DRIVE_LABEL_7_1=:PHYSICAL_DRIVE_LABEL_7_1 ,PHYSICAL_DRIVE_STATUS_7_1=:PHYSICAL_DRIVE_STATUS_7_1,PHYSICAL_DRIVE_MODEL_7_1=:PHYSICAL_DRIVE_MODEL_7_1,PHYSICAL_DRIVE_CAPACITY_7_1=:PHYSICAL_DRIVE_CAPACITY_7_1,PHYSICAL_DRIVE_SN_7_1=:PHYSICAL_DRIVE_SN_7_1,PHYSICAL_DRIVE_CONFI_7_1=:PHYSICAL_DRIVE_CONFI_7_1,PHYSICAL_DRIVE_FW_7_1=:PHYSICAL_DRIVE_FW_7_1, \
                         PHYSICAL_DRIVE_LABEL_7_2=:PHYSICAL_DRIVE_LABEL_7_2 ,PHYSICAL_DRIVE_STATUS_7_2=:PHYSICAL_DRIVE_STATUS_7_2,PHYSICAL_DRIVE_MODEL_7_2=:PHYSICAL_DRIVE_MODEL_7_2,PHYSICAL_DRIVE_CAPACITY_7_2=:PHYSICAL_DRIVE_CAPACITY_7_2,PHYSICAL_DRIVE_SN_7_2=:PHYSICAL_DRIVE_SN_7_2,PHYSICAL_DRIVE_CONFI_7_2=:PHYSICAL_DRIVE_CONFI_7_2,PHYSICAL_DRIVE_FW_7_2=:PHYSICAL_DRIVE_FW_7_2, \
                         PHYSICAL_DRIVE_LABEL_7_3=:PHYSICAL_DRIVE_LABEL_7_3 ,PHYSICAL_DRIVE_STATUS_7_3=:PHYSICAL_DRIVE_STATUS_7_3,PHYSICAL_DRIVE_MODEL_7_3=:PHYSICAL_DRIVE_MODEL_7_3,PHYSICAL_DRIVE_CAPACITY_7_3=:PHYSICAL_DRIVE_CAPACITY_7_3,PHYSICAL_DRIVE_SN_7_3=:PHYSICAL_DRIVE_SN_7_3,PHYSICAL_DRIVE_CONFI_7_3=:PHYSICAL_DRIVE_CONFI_7_3,PHYSICAL_DRIVE_FW_7_3=:PHYSICAL_DRIVE_FW_7_3, \
                         PHYSICAL_DRIVE_LABEL_7_4=:PHYSICAL_DRIVE_LABEL_7_4 ,PHYSICAL_DRIVE_STATUS_7_4=:PHYSICAL_DRIVE_STATUS_7_4,PHYSICAL_DRIVE_MODEL_7_4=:PHYSICAL_DRIVE_MODEL_7_4,PHYSICAL_DRIVE_CAPACITY_7_4=:PHYSICAL_DRIVE_CAPACITY_7_4,PHYSICAL_DRIVE_SN_7_4=:PHYSICAL_DRIVE_SN_7_4,PHYSICAL_DRIVE_CONFI_7_4=:PHYSICAL_DRIVE_CONFI_7_4,PHYSICAL_DRIVE_FW_7_4=:PHYSICAL_DRIVE_FW_7_4, \
                         PHYSICAL_DRIVE_LABEL_7_5=:PHYSICAL_DRIVE_LABEL_7_5 ,PHYSICAL_DRIVE_STATUS_7_5=:PHYSICAL_DRIVE_STATUS_7_5,PHYSICAL_DRIVE_MODEL_7_5=:PHYSICAL_DRIVE_MODEL_7_5,PHYSICAL_DRIVE_CAPACITY_7_5=:PHYSICAL_DRIVE_CAPACITY_7_5,PHYSICAL_DRIVE_SN_7_5=:PHYSICAL_DRIVE_SN_7_5,PHYSICAL_DRIVE_CONFI_7_5=:PHYSICAL_DRIVE_CONFI_7_5,PHYSICAL_DRIVE_FW_7_5=:PHYSICAL_DRIVE_FW_7_5, \
                         PHYSICAL_DRIVE_LABEL_7_6=:PHYSICAL_DRIVE_LABEL_7_6 ,PHYSICAL_DRIVE_STATUS_7_6=:PHYSICAL_DRIVE_STATUS_7_6,PHYSICAL_DRIVE_MODEL_7_6=:PHYSICAL_DRIVE_MODEL_7_6,PHYSICAL_DRIVE_CAPACITY_7_6=:PHYSICAL_DRIVE_CAPACITY_7_6,PHYSICAL_DRIVE_SN_7_6=:PHYSICAL_DRIVE_SN_7_6,PHYSICAL_DRIVE_CONFI_7_6=:PHYSICAL_DRIVE_CONFI_7_6,PHYSICAL_DRIVE_FW_7_6=:PHYSICAL_DRIVE_FW_7_6, \
                         PHYSICAL_DRIVE_LABEL_7_7=:PHYSICAL_DRIVE_LABEL_7_7 ,PHYSICAL_DRIVE_STATUS_7_7=:PHYSICAL_DRIVE_STATUS_7_7,PHYSICAL_DRIVE_MODEL_7_7=:PHYSICAL_DRIVE_MODEL_7_7,PHYSICAL_DRIVE_CAPACITY_7_7=:PHYSICAL_DRIVE_CAPACITY_7_7,PHYSICAL_DRIVE_SN_7_7=:PHYSICAL_DRIVE_SN_7_7,PHYSICAL_DRIVE_CONFI_7_7=:PHYSICAL_DRIVE_CONFI_7_7,PHYSICAL_DRIVE_FW_7_7=:PHYSICAL_DRIVE_FW_7_7, \
                         PHYSICAL_DRIVE_LABEL_7_8=:PHYSICAL_DRIVE_LABEL_7_8 ,PHYSICAL_DRIVE_STATUS_7_8=:PHYSICAL_DRIVE_STATUS_7_8,PHYSICAL_DRIVE_MODEL_7_8=:PHYSICAL_DRIVE_MODEL_7_8,PHYSICAL_DRIVE_CAPACITY_7_8=:PHYSICAL_DRIVE_CAPACITY_7_8,PHYSICAL_DRIVE_SN_7_8=:PHYSICAL_DRIVE_SN_7_8,PHYSICAL_DRIVE_CONFI_7_8=:PHYSICAL_DRIVE_CONFI_7_8,PHYSICAL_DRIVE_FW_7_8=:PHYSICAL_DRIVE_FW_7_8, \
                         PHYSICAL_DRIVE_LABEL_7_9=:PHYSICAL_DRIVE_LABEL_7_9 ,PHYSICAL_DRIVE_STATUS_7_9=:PHYSICAL_DRIVE_STATUS_7_9,PHYSICAL_DRIVE_MODEL_7_9=:PHYSICAL_DRIVE_MODEL_7_9,PHYSICAL_DRIVE_CAPACITY_7_9=:PHYSICAL_DRIVE_CAPACITY_7_9,PHYSICAL_DRIVE_SN_7_9=:PHYSICAL_DRIVE_SN_7_9,PHYSICAL_DRIVE_CONFI_7_9=:PHYSICAL_DRIVE_CONFI_7_9,PHYSICAL_DRIVE_FW_7_9=:PHYSICAL_DRIVE_FW_7_9, \
                         PHYSICAL_DRIVE_LABEL_7_10=:PHYSICAL_DRIVE_LABEL_7_10 ,PHYSICAL_DRIVE_STATUS_7_10=:PHYSICAL_DRIVE_STATUS_7_10,PHYSICAL_DRIVE_MODEL_7_10=:PHYSICAL_DRIVE_MODEL_7_10,PHYSICAL_DRIVE_CAPACITY_7_10=:PHYSICAL_DRIVE_CAPACITY_7_10,PHYSICAL_DRIVE_SN_7_10=:PHYSICAL_DRIVE_SN_7_10,PHYSICAL_DRIVE_CONFI_7_10=:PHYSICAL_DRIVE_CONFI_7_10,PHYSICAL_DRIVE_FW_7_10=:PHYSICAL_DRIVE_FW_7_10 where IP_ILO=:IP_ILO',
                         param)
    connection.commit()
    connection.close()

def update_storage_8_info(logical_drive=None,logical_drive_status=None,logical_drive_capacity=None,logical_drive_tolerance=None,logical_drive_type=None,physical_drive_label_1=None,physical_drive_status_1=None,physical_drive_capacity_1=None,physical_drive_model_1=None,physical_drive_sn_1=None,physical_drive_confi_1=None,physical_drive_fw_1=None,
                                                                                                                               physical_drive_label_2=None,physical_drive_status_2=None,physical_drive_capacity_2=None,physical_drive_model_2=None,physical_drive_sn_2=None,physical_drive_confi_2=None,physical_drive_fw_2=None,
                                                                                                                               physical_drive_label_3=None,physical_drive_status_3=None,physical_drive_capacity_3=None,physical_drive_model_3=None,physical_drive_sn_3=None,physical_drive_confi_3=None,physical_drive_fw_3=None,
                                                                                                                               physical_drive_label_4=None,physical_drive_status_4=None,physical_drive_capacity_4=None,physical_drive_model_4=None,physical_drive_sn_4=None,physical_drive_confi_4=None,physical_drive_fw_4=None,
                                                                                                                               physical_drive_label_5=None,physical_drive_status_5=None,physical_drive_capacity_5=None,physical_drive_model_5=None,physical_drive_sn_5=None,physical_drive_confi_5=None,physical_drive_fw_5=None,
                                                                                                                               physical_drive_label_6=None,physical_drive_status_6=None,physical_drive_capacity_6=None,physical_drive_model_6=None,physical_drive_sn_6=None,physical_drive_confi_6=None,physical_drive_fw_6=None,
                                                                                                                               physical_drive_label_7=None,physical_drive_status_7=None,physical_drive_capacity_7=None,physical_drive_model_7=None,physical_drive_sn_7=None,physical_drive_confi_7=None,physical_drive_fw_7=None,
                                                                                                                               physical_drive_label_8=None,physical_drive_status_8=None,physical_drive_capacity_8=None,physical_drive_model_8=None,physical_drive_sn_8=None,physical_drive_confi_8=None,physical_drive_fw_8=None,
                                                                                                                               physical_drive_label_9=None,physical_drive_status_9=None,physical_drive_capacity_9=None,physical_drive_model_9=None,physical_drive_sn_9=None,physical_drive_confi_9=None,physical_drive_fw_9=None,
                                                                                                                               physical_drive_label_10=None,physical_drive_status_10=None,physical_drive_capacity_10=None,physical_drive_model_10=None,physical_drive_sn_10=None,physical_drive_confi_10=None,physical_drive_fw_10=None,
                                                                                                                               ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'LOGICAL_DRIVE_8': logical_drive, 'LOGICAL_DRIVE_STATUS_8': logical_drive_status, 'LOGICAL_DRIVE_CAPACITY_8': logical_drive_capacity,'LOGICAL_DRIVE_TOLERANCE_8': logical_drive_tolerance,'LOGICAL_DRIVE_TYPE_8': logical_drive_type,
    'PHYSICAL_DRIVE_LABEL_8_1': physical_drive_label_1,'PHYSICAL_DRIVE_STATUS_8_1': physical_drive_status_1,'PHYSICAL_DRIVE_MODEL_8_1': physical_drive_model_1,'PHYSICAL_DRIVE_CAPACITY_8_1': physical_drive_capacity_1,'PHYSICAL_DRIVE_SN_8_1': physical_drive_sn_1,'PHYSICAL_DRIVE_CONFI_8_1': physical_drive_confi_1,'PHYSICAL_DRIVE_FW_8_1': physical_drive_fw_1,
    'PHYSICAL_DRIVE_LABEL_8_2': physical_drive_label_2,'PHYSICAL_DRIVE_STATUS_8_2': physical_drive_status_2,'PHYSICAL_DRIVE_MODEL_8_2': physical_drive_model_2,'PHYSICAL_DRIVE_CAPACITY_8_2': physical_drive_capacity_2,'PHYSICAL_DRIVE_SN_8_2': physical_drive_sn_2,'PHYSICAL_DRIVE_CONFI_8_2': physical_drive_confi_2,'PHYSICAL_DRIVE_FW_8_2': physical_drive_fw_2,
    'PHYSICAL_DRIVE_LABEL_8_3': physical_drive_label_3,'PHYSICAL_DRIVE_STATUS_8_3': physical_drive_status_3,'PHYSICAL_DRIVE_MODEL_8_3': physical_drive_model_3,'PHYSICAL_DRIVE_CAPACITY_8_3': physical_drive_capacity_3,'PHYSICAL_DRIVE_SN_8_3': physical_drive_sn_3,'PHYSICAL_DRIVE_CONFI_8_3': physical_drive_confi_3,'PHYSICAL_DRIVE_FW_8_3': physical_drive_fw_3,
    'PHYSICAL_DRIVE_LABEL_8_4': physical_drive_label_4,'PHYSICAL_DRIVE_STATUS_8_4': physical_drive_status_4,'PHYSICAL_DRIVE_MODEL_8_4': physical_drive_model_4,'PHYSICAL_DRIVE_CAPACITY_8_4': physical_drive_capacity_4,'PHYSICAL_DRIVE_SN_8_4': physical_drive_sn_4,'PHYSICAL_DRIVE_CONFI_8_4': physical_drive_confi_4,'PHYSICAL_DRIVE_FW_8_4': physical_drive_fw_4,
    'PHYSICAL_DRIVE_LABEL_8_5': physical_drive_label_5,'PHYSICAL_DRIVE_STATUS_8_5': physical_drive_status_5,'PHYSICAL_DRIVE_MODEL_8_5': physical_drive_model_5,'PHYSICAL_DRIVE_CAPACITY_8_5': physical_drive_capacity_5,'PHYSICAL_DRIVE_SN_8_5': physical_drive_sn_5,'PHYSICAL_DRIVE_CONFI_8_5': physical_drive_confi_5,'PHYSICAL_DRIVE_FW_8_5': physical_drive_fw_5,
    'PHYSICAL_DRIVE_LABEL_8_6': physical_drive_label_6,'PHYSICAL_DRIVE_STATUS_8_6': physical_drive_status_6,'PHYSICAL_DRIVE_MODEL_8_6': physical_drive_model_6,'PHYSICAL_DRIVE_CAPACITY_8_6': physical_drive_capacity_6,'PHYSICAL_DRIVE_SN_8_6': physical_drive_sn_6,'PHYSICAL_DRIVE_CONFI_8_6': physical_drive_confi_6,'PHYSICAL_DRIVE_FW_8_6': physical_drive_fw_6,
    'PHYSICAL_DRIVE_LABEL_8_7': physical_drive_label_7,'PHYSICAL_DRIVE_STATUS_8_7': physical_drive_status_7,'PHYSICAL_DRIVE_MODEL_8_7': physical_drive_model_7,'PHYSICAL_DRIVE_CAPACITY_8_7': physical_drive_capacity_7,'PHYSICAL_DRIVE_SN_8_7': physical_drive_sn_7,'PHYSICAL_DRIVE_CONFI_8_7': physical_drive_confi_7,'PHYSICAL_DRIVE_FW_8_7': physical_drive_fw_7,
    'PHYSICAL_DRIVE_LABEL_8_8': physical_drive_label_8,'PHYSICAL_DRIVE_STATUS_8_8': physical_drive_status_8,'PHYSICAL_DRIVE_MODEL_8_8': physical_drive_model_8,'PHYSICAL_DRIVE_CAPACITY_8_8': physical_drive_capacity_8,'PHYSICAL_DRIVE_SN_8_8': physical_drive_sn_8,'PHYSICAL_DRIVE_CONFI_8_8': physical_drive_confi_8,'PHYSICAL_DRIVE_FW_8_8': physical_drive_fw_8,
    'PHYSICAL_DRIVE_LABEL_8_9': physical_drive_label_9,'PHYSICAL_DRIVE_STATUS_8_9': physical_drive_status_9,'PHYSICAL_DRIVE_MODEL_8_9': physical_drive_model_9,'PHYSICAL_DRIVE_CAPACITY_8_9': physical_drive_capacity_9,'PHYSICAL_DRIVE_SN_8_9': physical_drive_sn_9,'PHYSICAL_DRIVE_CONFI_8_9': physical_drive_confi_9,'PHYSICAL_DRIVE_FW_8_9': physical_drive_fw_9,
    'PHYSICAL_DRIVE_LABEL_8_10': physical_drive_label_10,'PHYSICAL_DRIVE_STATUS_8_10': physical_drive_status_10,'PHYSICAL_DRIVE_MODEL_8_10': physical_drive_model_10,'PHYSICAL_DRIVE_CAPACITY_8_10': physical_drive_capacity_10, 'PHYSICAL_DRIVE_SN_8_10': physical_drive_sn_10,'PHYSICAL_DRIVE_CONFI_8_10': physical_drive_confi_10, 'PHYSICAL_DRIVE_FW_8_10': physical_drive_fw_10,
    'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update STORAGE_INFO set LOGICAL_DRIVE_8=:LOGICAL_DRIVE_8,LOGICAL_DRIVE_STATUS_8=:LOGICAL_DRIVE_STATUS_8,LOGICAL_DRIVE_CAPACITY_8=:LOGICAL_DRIVE_CAPACITY_8,LOGICAL_DRIVE_TOLERANCE_8=:LOGICAL_DRIVE_TOLERANCE_8,LOGICAL_DRIVE_TYPE_8=:LOGICAL_DRIVE_TYPE_8, \
                         PHYSICAL_DRIVE_LABEL_8_1=:PHYSICAL_DRIVE_LABEL_8_1 ,PHYSICAL_DRIVE_STATUS_8_1=:PHYSICAL_DRIVE_STATUS_8_1,PHYSICAL_DRIVE_MODEL_8_1=:PHYSICAL_DRIVE_MODEL_8_1,PHYSICAL_DRIVE_CAPACITY_8_1=:PHYSICAL_DRIVE_CAPACITY_8_1,PHYSICAL_DRIVE_SN_8_1=:PHYSICAL_DRIVE_SN_8_1,PHYSICAL_DRIVE_CONFI_8_1=:PHYSICAL_DRIVE_CONFI_8_1,PHYSICAL_DRIVE_FW_8_1=:PHYSICAL_DRIVE_FW_8_1, \
                         PHYSICAL_DRIVE_LABEL_8_2=:PHYSICAL_DRIVE_LABEL_8_2 ,PHYSICAL_DRIVE_STATUS_8_2=:PHYSICAL_DRIVE_STATUS_8_2,PHYSICAL_DRIVE_MODEL_8_2=:PHYSICAL_DRIVE_MODEL_8_2,PHYSICAL_DRIVE_CAPACITY_8_2=:PHYSICAL_DRIVE_CAPACITY_8_2,PHYSICAL_DRIVE_SN_8_2=:PHYSICAL_DRIVE_SN_8_2,PHYSICAL_DRIVE_CONFI_8_2=:PHYSICAL_DRIVE_CONFI_8_2,PHYSICAL_DRIVE_FW_8_2=:PHYSICAL_DRIVE_FW_8_2, \
                         PHYSICAL_DRIVE_LABEL_8_3=:PHYSICAL_DRIVE_LABEL_8_3 ,PHYSICAL_DRIVE_STATUS_8_3=:PHYSICAL_DRIVE_STATUS_8_3,PHYSICAL_DRIVE_MODEL_8_3=:PHYSICAL_DRIVE_MODEL_8_3,PHYSICAL_DRIVE_CAPACITY_8_3=:PHYSICAL_DRIVE_CAPACITY_8_3,PHYSICAL_DRIVE_SN_8_3=:PHYSICAL_DRIVE_SN_8_3,PHYSICAL_DRIVE_CONFI_8_3=:PHYSICAL_DRIVE_CONFI_8_3,PHYSICAL_DRIVE_FW_8_3=:PHYSICAL_DRIVE_FW_8_3, \
                         PHYSICAL_DRIVE_LABEL_8_4=:PHYSICAL_DRIVE_LABEL_8_4 ,PHYSICAL_DRIVE_STATUS_8_4=:PHYSICAL_DRIVE_STATUS_8_4,PHYSICAL_DRIVE_MODEL_8_4=:PHYSICAL_DRIVE_MODEL_8_4,PHYSICAL_DRIVE_CAPACITY_8_4=:PHYSICAL_DRIVE_CAPACITY_8_4,PHYSICAL_DRIVE_SN_8_4=:PHYSICAL_DRIVE_SN_8_4,PHYSICAL_DRIVE_CONFI_8_4=:PHYSICAL_DRIVE_CONFI_8_4,PHYSICAL_DRIVE_FW_8_4=:PHYSICAL_DRIVE_FW_8_4, \
                         PHYSICAL_DRIVE_LABEL_8_5=:PHYSICAL_DRIVE_LABEL_8_5 ,PHYSICAL_DRIVE_STATUS_8_5=:PHYSICAL_DRIVE_STATUS_8_5,PHYSICAL_DRIVE_MODEL_8_5=:PHYSICAL_DRIVE_MODEL_8_5,PHYSICAL_DRIVE_CAPACITY_8_5=:PHYSICAL_DRIVE_CAPACITY_8_5,PHYSICAL_DRIVE_SN_8_5=:PHYSICAL_DRIVE_SN_8_5,PHYSICAL_DRIVE_CONFI_8_5=:PHYSICAL_DRIVE_CONFI_8_5,PHYSICAL_DRIVE_FW_8_5=:PHYSICAL_DRIVE_FW_8_5, \
                         PHYSICAL_DRIVE_LABEL_8_6=:PHYSICAL_DRIVE_LABEL_8_6 ,PHYSICAL_DRIVE_STATUS_8_6=:PHYSICAL_DRIVE_STATUS_8_6,PHYSICAL_DRIVE_MODEL_8_6=:PHYSICAL_DRIVE_MODEL_8_6,PHYSICAL_DRIVE_CAPACITY_8_6=:PHYSICAL_DRIVE_CAPACITY_8_6,PHYSICAL_DRIVE_SN_8_6=:PHYSICAL_DRIVE_SN_8_6,PHYSICAL_DRIVE_CONFI_8_6=:PHYSICAL_DRIVE_CONFI_8_6,PHYSICAL_DRIVE_FW_8_6=:PHYSICAL_DRIVE_FW_8_6, \
                         PHYSICAL_DRIVE_LABEL_8_7=:PHYSICAL_DRIVE_LABEL_8_7 ,PHYSICAL_DRIVE_STATUS_8_7=:PHYSICAL_DRIVE_STATUS_8_7,PHYSICAL_DRIVE_MODEL_8_7=:PHYSICAL_DRIVE_MODEL_8_7,PHYSICAL_DRIVE_CAPACITY_8_7=:PHYSICAL_DRIVE_CAPACITY_8_7,PHYSICAL_DRIVE_SN_8_7=:PHYSICAL_DRIVE_SN_8_7,PHYSICAL_DRIVE_CONFI_8_7=:PHYSICAL_DRIVE_CONFI_8_7,PHYSICAL_DRIVE_FW_8_7=:PHYSICAL_DRIVE_FW_8_7, \
                         PHYSICAL_DRIVE_LABEL_8_8=:PHYSICAL_DRIVE_LABEL_8_8 ,PHYSICAL_DRIVE_STATUS_8_8=:PHYSICAL_DRIVE_STATUS_8_8,PHYSICAL_DRIVE_MODEL_8_8=:PHYSICAL_DRIVE_MODEL_8_8,PHYSICAL_DRIVE_CAPACITY_8_8=:PHYSICAL_DRIVE_CAPACITY_8_8,PHYSICAL_DRIVE_SN_8_8=:PHYSICAL_DRIVE_SN_8_8,PHYSICAL_DRIVE_CONFI_8_8=:PHYSICAL_DRIVE_CONFI_8_8,PHYSICAL_DRIVE_FW_8_8=:PHYSICAL_DRIVE_FW_8_8, \
                         PHYSICAL_DRIVE_LABEL_8_9=:PHYSICAL_DRIVE_LABEL_8_9 ,PHYSICAL_DRIVE_STATUS_8_9=:PHYSICAL_DRIVE_STATUS_8_9,PHYSICAL_DRIVE_MODEL_8_9=:PHYSICAL_DRIVE_MODEL_8_9,PHYSICAL_DRIVE_CAPACITY_8_9=:PHYSICAL_DRIVE_CAPACITY_8_9,PHYSICAL_DRIVE_SN_8_9=:PHYSICAL_DRIVE_SN_8_9,PHYSICAL_DRIVE_CONFI_8_9=:PHYSICAL_DRIVE_CONFI_8_9,PHYSICAL_DRIVE_FW_8_9=:PHYSICAL_DRIVE_FW_8_9, \
                         PHYSICAL_DRIVE_LABEL_8_10=:PHYSICAL_DRIVE_LABEL_8_10 ,PHYSICAL_DRIVE_STATUS_8_10=:PHYSICAL_DRIVE_STATUS_8_10,PHYSICAL_DRIVE_MODEL_8_10=:PHYSICAL_DRIVE_MODEL_8_10,PHYSICAL_DRIVE_CAPACITY_8_10=:PHYSICAL_DRIVE_CAPACITY_8_10,PHYSICAL_DRIVE_SN_8_10=:PHYSICAL_DRIVE_SN_8_10,PHYSICAL_DRIVE_CONFI_8_10=:PHYSICAL_DRIVE_CONFI_8_10,PHYSICAL_DRIVE_FW_8_10=:PHYSICAL_DRIVE_FW_8_10 where IP_ILO=:IP_ILO',
                         param)
    connection.commit()
    connection.close()

def update_storage_9_info(logical_drive=None,logical_drive_status=None,logical_drive_capacity=None,logical_drive_tolerance=None,logical_drive_type=None,physical_drive_label_1=None,physical_drive_status_1=None,physical_drive_capacity_1=None,physical_drive_model_1=None,physical_drive_sn_1=None,physical_drive_confi_1=None,physical_drive_fw_1=None,
                                                                                                                               physical_drive_label_2=None,physical_drive_status_2=None,physical_drive_capacity_2=None,physical_drive_model_2=None,physical_drive_sn_2=None,physical_drive_confi_2=None,physical_drive_fw_2=None,
                                                                                                                               physical_drive_label_3=None,physical_drive_status_3=None,physical_drive_capacity_3=None,physical_drive_model_3=None,physical_drive_sn_3=None,physical_drive_confi_3=None,physical_drive_fw_3=None,
                                                                                                                               physical_drive_label_4=None,physical_drive_status_4=None,physical_drive_capacity_4=None,physical_drive_model_4=None,physical_drive_sn_4=None,physical_drive_confi_4=None,physical_drive_fw_4=None,
                                                                                                                               physical_drive_label_5=None,physical_drive_status_5=None,physical_drive_capacity_5=None,physical_drive_model_5=None,physical_drive_sn_5=None,physical_drive_confi_5=None,physical_drive_fw_5=None,
                                                                                                                               physical_drive_label_6=None,physical_drive_status_6=None,physical_drive_capacity_6=None,physical_drive_model_6=None,physical_drive_sn_6=None,physical_drive_confi_6=None,physical_drive_fw_6=None,
                                                                                                                               physical_drive_label_7=None,physical_drive_status_7=None,physical_drive_capacity_7=None,physical_drive_model_7=None,physical_drive_sn_7=None,physical_drive_confi_7=None,physical_drive_fw_7=None,
                                                                                                                               physical_drive_label_8=None,physical_drive_status_8=None,physical_drive_capacity_8=None,physical_drive_model_8=None,physical_drive_sn_8=None,physical_drive_confi_8=None,physical_drive_fw_8=None,
                                                                                                                               physical_drive_label_9=None,physical_drive_status_9=None,physical_drive_capacity_9=None,physical_drive_model_9=None,physical_drive_sn_9=None,physical_drive_confi_9=None,physical_drive_fw_9=None,
                                                                                                                               physical_drive_label_10=None,physical_drive_status_10=None,physical_drive_capacity_10=None,physical_drive_model_10=None,physical_drive_sn_10=None,physical_drive_confi_10=None,physical_drive_fw_10=None,
                                                                                                                               ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'LOGICAL_DRIVE_9': logical_drive, 'LOGICAL_DRIVE_STATUS_9': logical_drive_status, 'LOGICAL_DRIVE_CAPACITY_9': logical_drive_capacity,'LOGICAL_DRIVE_TOLERANCE_9': logical_drive_tolerance,'LOGICAL_DRIVE_TYPE_9': logical_drive_type,
    'PHYSICAL_DRIVE_LABEL_9_1': physical_drive_label_1,'PHYSICAL_DRIVE_STATUS_9_1': physical_drive_status_1,'PHYSICAL_DRIVE_MODEL_9_1': physical_drive_model_1,'PHYSICAL_DRIVE_CAPACITY_9_1': physical_drive_capacity_1,'PHYSICAL_DRIVE_SN_9_1': physical_drive_sn_1,'PHYSICAL_DRIVE_CONFI_9_1': physical_drive_confi_1,'PHYSICAL_DRIVE_FW_9_1': physical_drive_fw_1,
    'PHYSICAL_DRIVE_LABEL_9_2': physical_drive_label_2,'PHYSICAL_DRIVE_STATUS_9_2': physical_drive_status_2,'PHYSICAL_DRIVE_MODEL_9_2': physical_drive_model_2,'PHYSICAL_DRIVE_CAPACITY_9_2': physical_drive_capacity_2,'PHYSICAL_DRIVE_SN_9_2': physical_drive_sn_2,'PHYSICAL_DRIVE_CONFI_9_2': physical_drive_confi_2,'PHYSICAL_DRIVE_FW_9_2': physical_drive_fw_2,
    'PHYSICAL_DRIVE_LABEL_9_3': physical_drive_label_3,'PHYSICAL_DRIVE_STATUS_9_3': physical_drive_status_3,'PHYSICAL_DRIVE_MODEL_9_3': physical_drive_model_3,'PHYSICAL_DRIVE_CAPACITY_9_3': physical_drive_capacity_3,'PHYSICAL_DRIVE_SN_9_3': physical_drive_sn_3,'PHYSICAL_DRIVE_CONFI_9_3': physical_drive_confi_3,'PHYSICAL_DRIVE_FW_9_3': physical_drive_fw_3,
    'PHYSICAL_DRIVE_LABEL_9_4': physical_drive_label_4,'PHYSICAL_DRIVE_STATUS_9_4': physical_drive_status_4,'PHYSICAL_DRIVE_MODEL_9_4': physical_drive_model_4,'PHYSICAL_DRIVE_CAPACITY_9_4': physical_drive_capacity_4,'PHYSICAL_DRIVE_SN_9_4': physical_drive_sn_4,'PHYSICAL_DRIVE_CONFI_9_4': physical_drive_confi_4,'PHYSICAL_DRIVE_FW_9_4': physical_drive_fw_4,
    'PHYSICAL_DRIVE_LABEL_9_5': physical_drive_label_5,'PHYSICAL_DRIVE_STATUS_9_5': physical_drive_status_5,'PHYSICAL_DRIVE_MODEL_9_5': physical_drive_model_5,'PHYSICAL_DRIVE_CAPACITY_9_5': physical_drive_capacity_5,'PHYSICAL_DRIVE_SN_9_5': physical_drive_sn_5,'PHYSICAL_DRIVE_CONFI_9_5': physical_drive_confi_5,'PHYSICAL_DRIVE_FW_9_5': physical_drive_fw_5,
    'PHYSICAL_DRIVE_LABEL_9_6': physical_drive_label_6,'PHYSICAL_DRIVE_STATUS_9_6': physical_drive_status_6,'PHYSICAL_DRIVE_MODEL_9_6': physical_drive_model_6,'PHYSICAL_DRIVE_CAPACITY_9_6': physical_drive_capacity_6,'PHYSICAL_DRIVE_SN_9_6': physical_drive_sn_6,'PHYSICAL_DRIVE_CONFI_9_6': physical_drive_confi_6,'PHYSICAL_DRIVE_FW_9_6': physical_drive_fw_6,
    'PHYSICAL_DRIVE_LABEL_9_7': physical_drive_label_7,'PHYSICAL_DRIVE_STATUS_9_7': physical_drive_status_7,'PHYSICAL_DRIVE_MODEL_9_7': physical_drive_model_7,'PHYSICAL_DRIVE_CAPACITY_9_7': physical_drive_capacity_7,'PHYSICAL_DRIVE_SN_9_7': physical_drive_sn_7,'PHYSICAL_DRIVE_CONFI_9_7': physical_drive_confi_7,'PHYSICAL_DRIVE_FW_9_7': physical_drive_fw_7,
    'PHYSICAL_DRIVE_LABEL_9_8': physical_drive_label_8,'PHYSICAL_DRIVE_STATUS_9_8': physical_drive_status_8,'PHYSICAL_DRIVE_MODEL_9_8': physical_drive_model_8,'PHYSICAL_DRIVE_CAPACITY_9_8': physical_drive_capacity_8,'PHYSICAL_DRIVE_SN_9_8': physical_drive_sn_8,'PHYSICAL_DRIVE_CONFI_9_8': physical_drive_confi_8,'PHYSICAL_DRIVE_FW_9_8': physical_drive_fw_8,
    'PHYSICAL_DRIVE_LABEL_9_9': physical_drive_label_9,'PHYSICAL_DRIVE_STATUS_9_9': physical_drive_status_9,'PHYSICAL_DRIVE_MODEL_9_9': physical_drive_model_9,'PHYSICAL_DRIVE_CAPACITY_9_9': physical_drive_capacity_9,'PHYSICAL_DRIVE_SN_9_9': physical_drive_sn_9,'PHYSICAL_DRIVE_CONFI_9_9': physical_drive_confi_9,'PHYSICAL_DRIVE_FW_9_9': physical_drive_fw_9,
    'PHYSICAL_DRIVE_LABEL_9_10': physical_drive_label_10,'PHYSICAL_DRIVE_STATUS_9_10': physical_drive_status_10,'PHYSICAL_DRIVE_MODEL_9_10': physical_drive_model_10,'PHYSICAL_DRIVE_CAPACITY_9_10': physical_drive_capacity_10, 'PHYSICAL_DRIVE_SN_9_10': physical_drive_sn_10,'PHYSICAL_DRIVE_CONFI_9_10': physical_drive_confi_10, 'PHYSICAL_DRIVE_FW_9_10': physical_drive_fw_10,
    'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update STORAGE_INFO set LOGICAL_DRIVE_9=:LOGICAL_DRIVE_9,LOGICAL_DRIVE_STATUS_9=:LOGICAL_DRIVE_STATUS_9,LOGICAL_DRIVE_CAPACITY_9=:LOGICAL_DRIVE_CAPACITY_9,LOGICAL_DRIVE_TOLERANCE_9=:LOGICAL_DRIVE_TOLERANCE_9,LOGICAL_DRIVE_TYPE_9=:LOGICAL_DRIVE_TYPE_9, \
                         PHYSICAL_DRIVE_LABEL_9_1=:PHYSICAL_DRIVE_LABEL_9_1 ,PHYSICAL_DRIVE_STATUS_9_1=:PHYSICAL_DRIVE_STATUS_9_1,PHYSICAL_DRIVE_MODEL_9_1=:PHYSICAL_DRIVE_MODEL_9_1,PHYSICAL_DRIVE_CAPACITY_9_1=:PHYSICAL_DRIVE_CAPACITY_9_1,PHYSICAL_DRIVE_SN_9_1=:PHYSICAL_DRIVE_SN_9_1,PHYSICAL_DRIVE_CONFI_9_1=:PHYSICAL_DRIVE_CONFI_9_1,PHYSICAL_DRIVE_FW_9_1=:PHYSICAL_DRIVE_FW_9_1, \
                         PHYSICAL_DRIVE_LABEL_9_2=:PHYSICAL_DRIVE_LABEL_9_2 ,PHYSICAL_DRIVE_STATUS_9_2=:PHYSICAL_DRIVE_STATUS_9_2,PHYSICAL_DRIVE_MODEL_9_2=:PHYSICAL_DRIVE_MODEL_9_2,PHYSICAL_DRIVE_CAPACITY_9_2=:PHYSICAL_DRIVE_CAPACITY_9_2,PHYSICAL_DRIVE_SN_9_2=:PHYSICAL_DRIVE_SN_9_2,PHYSICAL_DRIVE_CONFI_9_2=:PHYSICAL_DRIVE_CONFI_9_2,PHYSICAL_DRIVE_FW_9_2=:PHYSICAL_DRIVE_FW_9_2, \
                         PHYSICAL_DRIVE_LABEL_9_3=:PHYSICAL_DRIVE_LABEL_9_3 ,PHYSICAL_DRIVE_STATUS_9_3=:PHYSICAL_DRIVE_STATUS_9_3,PHYSICAL_DRIVE_MODEL_9_3=:PHYSICAL_DRIVE_MODEL_9_3,PHYSICAL_DRIVE_CAPACITY_9_3=:PHYSICAL_DRIVE_CAPACITY_9_3,PHYSICAL_DRIVE_SN_9_3=:PHYSICAL_DRIVE_SN_9_3,PHYSICAL_DRIVE_CONFI_9_3=:PHYSICAL_DRIVE_CONFI_9_3,PHYSICAL_DRIVE_FW_9_3=:PHYSICAL_DRIVE_FW_9_3, \
                         PHYSICAL_DRIVE_LABEL_9_4=:PHYSICAL_DRIVE_LABEL_9_4 ,PHYSICAL_DRIVE_STATUS_9_4=:PHYSICAL_DRIVE_STATUS_9_4,PHYSICAL_DRIVE_MODEL_9_4=:PHYSICAL_DRIVE_MODEL_9_4,PHYSICAL_DRIVE_CAPACITY_9_4=:PHYSICAL_DRIVE_CAPACITY_9_4,PHYSICAL_DRIVE_SN_9_4=:PHYSICAL_DRIVE_SN_9_4,PHYSICAL_DRIVE_CONFI_9_4=:PHYSICAL_DRIVE_CONFI_9_4,PHYSICAL_DRIVE_FW_9_4=:PHYSICAL_DRIVE_FW_9_4, \
                         PHYSICAL_DRIVE_LABEL_9_5=:PHYSICAL_DRIVE_LABEL_9_5 ,PHYSICAL_DRIVE_STATUS_9_5=:PHYSICAL_DRIVE_STATUS_9_5,PHYSICAL_DRIVE_MODEL_9_5=:PHYSICAL_DRIVE_MODEL_9_5,PHYSICAL_DRIVE_CAPACITY_9_5=:PHYSICAL_DRIVE_CAPACITY_9_5,PHYSICAL_DRIVE_SN_9_5=:PHYSICAL_DRIVE_SN_9_5,PHYSICAL_DRIVE_CONFI_9_5=:PHYSICAL_DRIVE_CONFI_9_5,PHYSICAL_DRIVE_FW_9_5=:PHYSICAL_DRIVE_FW_9_5, \
                         PHYSICAL_DRIVE_LABEL_9_6=:PHYSICAL_DRIVE_LABEL_9_6 ,PHYSICAL_DRIVE_STATUS_9_6=:PHYSICAL_DRIVE_STATUS_9_6,PHYSICAL_DRIVE_MODEL_9_6=:PHYSICAL_DRIVE_MODEL_9_6,PHYSICAL_DRIVE_CAPACITY_9_6=:PHYSICAL_DRIVE_CAPACITY_9_6,PHYSICAL_DRIVE_SN_9_6=:PHYSICAL_DRIVE_SN_9_6,PHYSICAL_DRIVE_CONFI_9_6=:PHYSICAL_DRIVE_CONFI_9_6,PHYSICAL_DRIVE_FW_9_6=:PHYSICAL_DRIVE_FW_9_6, \
                         PHYSICAL_DRIVE_LABEL_9_7=:PHYSICAL_DRIVE_LABEL_9_7 ,PHYSICAL_DRIVE_STATUS_9_7=:PHYSICAL_DRIVE_STATUS_9_7,PHYSICAL_DRIVE_MODEL_9_7=:PHYSICAL_DRIVE_MODEL_9_7,PHYSICAL_DRIVE_CAPACITY_9_7=:PHYSICAL_DRIVE_CAPACITY_9_7,PHYSICAL_DRIVE_SN_9_7=:PHYSICAL_DRIVE_SN_9_7,PHYSICAL_DRIVE_CONFI_9_7=:PHYSICAL_DRIVE_CONFI_9_7,PHYSICAL_DRIVE_FW_9_7=:PHYSICAL_DRIVE_FW_9_7, \
                         PHYSICAL_DRIVE_LABEL_9_8=:PHYSICAL_DRIVE_LABEL_9_8 ,PHYSICAL_DRIVE_STATUS_9_8=:PHYSICAL_DRIVE_STATUS_9_8,PHYSICAL_DRIVE_MODEL_9_8=:PHYSICAL_DRIVE_MODEL_9_8,PHYSICAL_DRIVE_CAPACITY_9_8=:PHYSICAL_DRIVE_CAPACITY_9_8,PHYSICAL_DRIVE_SN_9_8=:PHYSICAL_DRIVE_SN_9_8,PHYSICAL_DRIVE_CONFI_9_8=:PHYSICAL_DRIVE_CONFI_9_8,PHYSICAL_DRIVE_FW_9_8=:PHYSICAL_DRIVE_FW_9_8, \
                         PHYSICAL_DRIVE_LABEL_9_9=:PHYSICAL_DRIVE_LABEL_9_9 ,PHYSICAL_DRIVE_STATUS_9_9=:PHYSICAL_DRIVE_STATUS_9_9,PHYSICAL_DRIVE_MODEL_9_9=:PHYSICAL_DRIVE_MODEL_9_9,PHYSICAL_DRIVE_CAPACITY_9_9=:PHYSICAL_DRIVE_CAPACITY_9_9,PHYSICAL_DRIVE_SN_9_9=:PHYSICAL_DRIVE_SN_9_9,PHYSICAL_DRIVE_CONFI_9_9=:PHYSICAL_DRIVE_CONFI_9_9,PHYSICAL_DRIVE_FW_9_9=:PHYSICAL_DRIVE_FW_9_9, \
                         PHYSICAL_DRIVE_LABEL_9_10=:PHYSICAL_DRIVE_LABEL_9_10 ,PHYSICAL_DRIVE_STATUS_9_10=:PHYSICAL_DRIVE_STATUS_9_10,PHYSICAL_DRIVE_MODEL_9_10=:PHYSICAL_DRIVE_MODEL_9_10,PHYSICAL_DRIVE_CAPACITY_9_10=:PHYSICAL_DRIVE_CAPACITY_9_10,PHYSICAL_DRIVE_SN_9_10=:PHYSICAL_DRIVE_SN_9_10,PHYSICAL_DRIVE_CONFI_9_10=:PHYSICAL_DRIVE_CONFI_9_10,PHYSICAL_DRIVE_FW_9_10=:PHYSICAL_DRIVE_FW_9_10 where IP_ILO=:IP_ILO',
                         param)
    connection.commit()
    connection.close()

def update_storage_10_info(logical_drive=None,logical_drive_status=None,logical_drive_capacity=None,logical_drive_tolerance=None,logical_drive_type=None,physical_drive_label_1=None,physical_drive_status_1=None,physical_drive_capacity_1=None,physical_drive_model_1=None,physical_drive_sn_1=None,physical_drive_confi_1=None,physical_drive_fw_1=None,
                                                                                                                               physical_drive_label_2=None,physical_drive_status_2=None,physical_drive_capacity_2=None,physical_drive_model_2=None,physical_drive_sn_2=None,physical_drive_confi_2=None,physical_drive_fw_2=None,
                                                                                                                               physical_drive_label_3=None,physical_drive_status_3=None,physical_drive_capacity_3=None,physical_drive_model_3=None,physical_drive_sn_3=None,physical_drive_confi_3=None,physical_drive_fw_3=None,
                                                                                                                               physical_drive_label_4=None,physical_drive_status_4=None,physical_drive_capacity_4=None,physical_drive_model_4=None,physical_drive_sn_4=None,physical_drive_confi_4=None,physical_drive_fw_4=None,
                                                                                                                               physical_drive_label_5=None,physical_drive_status_5=None,physical_drive_capacity_5=None,physical_drive_model_5=None,physical_drive_sn_5=None,physical_drive_confi_5=None,physical_drive_fw_5=None,
                                                                                                                               physical_drive_label_6=None,physical_drive_status_6=None,physical_drive_capacity_6=None,physical_drive_model_6=None,physical_drive_sn_6=None,physical_drive_confi_6=None,physical_drive_fw_6=None,
                                                                                                                               physical_drive_label_7=None,physical_drive_status_7=None,physical_drive_capacity_7=None,physical_drive_model_7=None,physical_drive_sn_7=None,physical_drive_confi_7=None,physical_drive_fw_7=None,
                                                                                                                               physical_drive_label_8=None,physical_drive_status_8=None,physical_drive_capacity_8=None,physical_drive_model_8=None,physical_drive_sn_8=None,physical_drive_confi_8=None,physical_drive_fw_8=None,
                                                                                                                               physical_drive_label_9=None,physical_drive_status_9=None,physical_drive_capacity_9=None,physical_drive_model_9=None,physical_drive_sn_9=None,physical_drive_confi_9=None,physical_drive_fw_9=None,
                                                                                                                               physical_drive_label_10=None,physical_drive_status_10=None,physical_drive_capacity_10=None,physical_drive_model_10=None,physical_drive_sn_10=None,physical_drive_confi_10=None,physical_drive_fw_10=None,
                                                                                                                               ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'LOGICAL_DRIVE_10': logical_drive, 'LOGICAL_DRIVE_STATUS_10': logical_drive_status, 'LOGICAL_DRIVE_CAPACITY_10': logical_drive_capacity,'LOGICAL_DRIVE_TOLERANCE_10': logical_drive_tolerance,'LOGICAL_DRIVE_TYPE_10': logical_drive_type,
    'PHYSICAL_DRIVE_LABEL_10_1': physical_drive_label_1,'PHYSICAL_DRIVE_STATUS_10_1': physical_drive_status_1,'PHYSICAL_DRIVE_MODEL_10_1': physical_drive_model_1,'PHYSICAL_DRIVE_CAPACITY_10_1': physical_drive_capacity_1,'PHYSICAL_DRIVE_SN_10_1': physical_drive_sn_1,'PHYSICAL_DRIVE_CONFI_10_1': physical_drive_confi_1,'PHYSICAL_DRIVE_FW_10_1': physical_drive_fw_1,
    'PHYSICAL_DRIVE_LABEL_10_2': physical_drive_label_2,'PHYSICAL_DRIVE_STATUS_10_2': physical_drive_status_2,'PHYSICAL_DRIVE_MODEL_10_2': physical_drive_model_2,'PHYSICAL_DRIVE_CAPACITY_10_2': physical_drive_capacity_2,'PHYSICAL_DRIVE_SN_10_2': physical_drive_sn_2,'PHYSICAL_DRIVE_CONFI_10_2': physical_drive_confi_2,'PHYSICAL_DRIVE_FW_10_2': physical_drive_fw_2,
    'PHYSICAL_DRIVE_LABEL_10_3': physical_drive_label_3,'PHYSICAL_DRIVE_STATUS_10_3': physical_drive_status_3,'PHYSICAL_DRIVE_MODEL_10_3': physical_drive_model_3,'PHYSICAL_DRIVE_CAPACITY_10_3': physical_drive_capacity_3,'PHYSICAL_DRIVE_SN_10_3': physical_drive_sn_3,'PHYSICAL_DRIVE_CONFI_10_3': physical_drive_confi_3,'PHYSICAL_DRIVE_FW_10_3': physical_drive_fw_3,
    'PHYSICAL_DRIVE_LABEL_10_4': physical_drive_label_4,'PHYSICAL_DRIVE_STATUS_10_4': physical_drive_status_4,'PHYSICAL_DRIVE_MODEL_10_4': physical_drive_model_4,'PHYSICAL_DRIVE_CAPACITY_10_4': physical_drive_capacity_4,'PHYSICAL_DRIVE_SN_10_4': physical_drive_sn_4,'PHYSICAL_DRIVE_CONFI_10_4': physical_drive_confi_4,'PHYSICAL_DRIVE_FW_10_4': physical_drive_fw_4,
    'PHYSICAL_DRIVE_LABEL_10_5': physical_drive_label_5,'PHYSICAL_DRIVE_STATUS_10_5': physical_drive_status_5,'PHYSICAL_DRIVE_MODEL_10_5': physical_drive_model_5,'PHYSICAL_DRIVE_CAPACITY_10_5': physical_drive_capacity_5,'PHYSICAL_DRIVE_SN_10_5': physical_drive_sn_5,'PHYSICAL_DRIVE_CONFI_10_5': physical_drive_confi_5,'PHYSICAL_DRIVE_FW_10_5': physical_drive_fw_5,
    'PHYSICAL_DRIVE_LABEL_10_6': physical_drive_label_6,'PHYSICAL_DRIVE_STATUS_10_6': physical_drive_status_6,'PHYSICAL_DRIVE_MODEL_10_6': physical_drive_model_6,'PHYSICAL_DRIVE_CAPACITY_10_6': physical_drive_capacity_6,'PHYSICAL_DRIVE_SN_10_6': physical_drive_sn_6,'PHYSICAL_DRIVE_CONFI_10_6': physical_drive_confi_6,'PHYSICAL_DRIVE_FW_10_6': physical_drive_fw_6,
    'PHYSICAL_DRIVE_LABEL_10_7': physical_drive_label_7,'PHYSICAL_DRIVE_STATUS_10_7': physical_drive_status_7,'PHYSICAL_DRIVE_MODEL_10_7': physical_drive_model_7,'PHYSICAL_DRIVE_CAPACITY_10_7': physical_drive_capacity_7,'PHYSICAL_DRIVE_SN_10_7': physical_drive_sn_7,'PHYSICAL_DRIVE_CONFI_10_7': physical_drive_confi_7,'PHYSICAL_DRIVE_FW_10_7': physical_drive_fw_7,
    'PHYSICAL_DRIVE_LABEL_10_8': physical_drive_label_8,'PHYSICAL_DRIVE_STATUS_10_8': physical_drive_status_8,'PHYSICAL_DRIVE_MODEL_10_8': physical_drive_model_8,'PHYSICAL_DRIVE_CAPACITY_10_8': physical_drive_capacity_8,'PHYSICAL_DRIVE_SN_10_8': physical_drive_sn_8,'PHYSICAL_DRIVE_CONFI_10_8': physical_drive_confi_8,'PHYSICAL_DRIVE_FW_10_8': physical_drive_fw_8,
    'PHYSICAL_DRIVE_LABEL_10_9': physical_drive_label_9,'PHYSICAL_DRIVE_STATUS_10_9': physical_drive_status_9,'PHYSICAL_DRIVE_MODEL_10_9': physical_drive_model_9,'PHYSICAL_DRIVE_CAPACITY_10_9': physical_drive_capacity_9,'PHYSICAL_DRIVE_SN_10_9': physical_drive_sn_9,'PHYSICAL_DRIVE_CONFI_10_9': physical_drive_confi_9,'PHYSICAL_DRIVE_FW_10_9': physical_drive_fw_9,
    'PHYSICAL_DRIVE_LABEL_10_10': physical_drive_label_10,'PHYSICAL_DRIVE_STATUS_10_10': physical_drive_status_10,'PHYSICAL_DRIVE_MODEL_10_10': physical_drive_model_10,'PHYSICAL_DRIVE_CAPACITY_10_10': physical_drive_capacity_10, 'PHYSICAL_DRIVE_SN_10_10': physical_drive_sn_10,'PHYSICAL_DRIVE_CONFI_10_10': physical_drive_confi_10, 'PHYSICAL_DRIVE_FW_10_10': physical_drive_fw_10,
    'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update STORAGE_INFO set LOGICAL_DRIVE_10=:LOGICAL_DRIVE_10,LOGICAL_DRIVE_STATUS_10=:LOGICAL_DRIVE_STATUS_10,LOGICAL_DRIVE_CAPACITY_10=:LOGICAL_DRIVE_CAPACITY_10,LOGICAL_DRIVE_TOLERANCE_10=:LOGICAL_DRIVE_TOLERANCE_10,LOGICAL_DRIVE_TYPE_10=:LOGICAL_DRIVE_TYPE_10, \
                         PHYSICAL_DRIVE_LABEL_10_1=:PHYSICAL_DRIVE_LABEL_10_1 ,PHYSICAL_DRIVE_STATUS_10_1=:PHYSICAL_DRIVE_STATUS_10_1,PHYSICAL_DRIVE_MODEL_10_1=:PHYSICAL_DRIVE_MODEL_10_1,PHYSICAL_DRIVE_CAPACITY_10_1=:PHYSICAL_DRIVE_CAPACITY_10_1,PHYSICAL_DRIVE_SN_10_1=:PHYSICAL_DRIVE_SN_10_1,PHYSICAL_DRIVE_CONFI_10_1=:PHYSICAL_DRIVE_CONFI_10_1,PHYSICAL_DRIVE_FW_10_1=:PHYSICAL_DRIVE_FW_10_1, \
                         PHYSICAL_DRIVE_LABEL_10_2=:PHYSICAL_DRIVE_LABEL_10_2 ,PHYSICAL_DRIVE_STATUS_10_2=:PHYSICAL_DRIVE_STATUS_10_2,PHYSICAL_DRIVE_MODEL_10_2=:PHYSICAL_DRIVE_MODEL_10_2,PHYSICAL_DRIVE_CAPACITY_10_2=:PHYSICAL_DRIVE_CAPACITY_10_2,PHYSICAL_DRIVE_SN_10_2=:PHYSICAL_DRIVE_SN_10_2,PHYSICAL_DRIVE_CONFI_10_2=:PHYSICAL_DRIVE_CONFI_10_2,PHYSICAL_DRIVE_FW_10_2=:PHYSICAL_DRIVE_FW_10_2, \
                         PHYSICAL_DRIVE_LABEL_10_3=:PHYSICAL_DRIVE_LABEL_10_3 ,PHYSICAL_DRIVE_STATUS_10_3=:PHYSICAL_DRIVE_STATUS_10_3,PHYSICAL_DRIVE_MODEL_10_3=:PHYSICAL_DRIVE_MODEL_10_3,PHYSICAL_DRIVE_CAPACITY_10_3=:PHYSICAL_DRIVE_CAPACITY_10_3,PHYSICAL_DRIVE_SN_10_3=:PHYSICAL_DRIVE_SN_10_3,PHYSICAL_DRIVE_CONFI_10_3=:PHYSICAL_DRIVE_CONFI_10_3,PHYSICAL_DRIVE_FW_10_3=:PHYSICAL_DRIVE_FW_10_3, \
                         PHYSICAL_DRIVE_LABEL_10_4=:PHYSICAL_DRIVE_LABEL_10_4 ,PHYSICAL_DRIVE_STATUS_10_4=:PHYSICAL_DRIVE_STATUS_10_4,PHYSICAL_DRIVE_MODEL_10_4=:PHYSICAL_DRIVE_MODEL_10_4,PHYSICAL_DRIVE_CAPACITY_10_4=:PHYSICAL_DRIVE_CAPACITY_10_4,PHYSICAL_DRIVE_SN_10_4=:PHYSICAL_DRIVE_SN_10_4,PHYSICAL_DRIVE_CONFI_10_4=:PHYSICAL_DRIVE_CONFI_10_4,PHYSICAL_DRIVE_FW_10_4=:PHYSICAL_DRIVE_FW_10_4, \
                         PHYSICAL_DRIVE_LABEL_10_5=:PHYSICAL_DRIVE_LABEL_10_5 ,PHYSICAL_DRIVE_STATUS_10_5=:PHYSICAL_DRIVE_STATUS_10_5,PHYSICAL_DRIVE_MODEL_10_5=:PHYSICAL_DRIVE_MODEL_10_5,PHYSICAL_DRIVE_CAPACITY_10_5=:PHYSICAL_DRIVE_CAPACITY_10_5,PHYSICAL_DRIVE_SN_10_5=:PHYSICAL_DRIVE_SN_10_5,PHYSICAL_DRIVE_CONFI_10_5=:PHYSICAL_DRIVE_CONFI_10_5,PHYSICAL_DRIVE_FW_10_5=:PHYSICAL_DRIVE_FW_10_5, \
                         PHYSICAL_DRIVE_LABEL_10_6=:PHYSICAL_DRIVE_LABEL_10_6 ,PHYSICAL_DRIVE_STATUS_10_6=:PHYSICAL_DRIVE_STATUS_10_6,PHYSICAL_DRIVE_MODEL_10_6=:PHYSICAL_DRIVE_MODEL_10_6,PHYSICAL_DRIVE_CAPACITY_10_6=:PHYSICAL_DRIVE_CAPACITY_10_6,PHYSICAL_DRIVE_SN_10_6=:PHYSICAL_DRIVE_SN_10_6,PHYSICAL_DRIVE_CONFI_10_6=:PHYSICAL_DRIVE_CONFI_10_6,PHYSICAL_DRIVE_FW_10_6=:PHYSICAL_DRIVE_FW_10_6, \
                         PHYSICAL_DRIVE_LABEL_10_7=:PHYSICAL_DRIVE_LABEL_10_7 ,PHYSICAL_DRIVE_STATUS_10_7=:PHYSICAL_DRIVE_STATUS_10_7,PHYSICAL_DRIVE_MODEL_10_7=:PHYSICAL_DRIVE_MODEL_10_7,PHYSICAL_DRIVE_CAPACITY_10_7=:PHYSICAL_DRIVE_CAPACITY_10_7,PHYSICAL_DRIVE_SN_10_7=:PHYSICAL_DRIVE_SN_10_7,PHYSICAL_DRIVE_CONFI_10_7=:PHYSICAL_DRIVE_CONFI_10_7,PHYSICAL_DRIVE_FW_10_7=:PHYSICAL_DRIVE_FW_10_7, \
                         PHYSICAL_DRIVE_LABEL_10_8=:PHYSICAL_DRIVE_LABEL_10_8 ,PHYSICAL_DRIVE_STATUS_10_8=:PHYSICAL_DRIVE_STATUS_10_8,PHYSICAL_DRIVE_MODEL_10_8=:PHYSICAL_DRIVE_MODEL_10_8,PHYSICAL_DRIVE_CAPACITY_10_8=:PHYSICAL_DRIVE_CAPACITY_10_8,PHYSICAL_DRIVE_SN_10_8=:PHYSICAL_DRIVE_SN_10_8,PHYSICAL_DRIVE_CONFI_10_8=:PHYSICAL_DRIVE_CONFI_10_8,PHYSICAL_DRIVE_FW_10_8=:PHYSICAL_DRIVE_FW_10_8, \
                         PHYSICAL_DRIVE_LABEL_10_9=:PHYSICAL_DRIVE_LABEL_10_9 ,PHYSICAL_DRIVE_STATUS_10_9=:PHYSICAL_DRIVE_STATUS_10_9,PHYSICAL_DRIVE_MODEL_10_9=:PHYSICAL_DRIVE_MODEL_10_9,PHYSICAL_DRIVE_CAPACITY_10_9=:PHYSICAL_DRIVE_CAPACITY_10_9,PHYSICAL_DRIVE_SN_10_9=:PHYSICAL_DRIVE_SN_10_9,PHYSICAL_DRIVE_CONFI_10_9=:PHYSICAL_DRIVE_CONFI_10_9,PHYSICAL_DRIVE_FW_10_9=:PHYSICAL_DRIVE_FW_10_9, \
                         PHYSICAL_DRIVE_LABEL_10_10=:PHYSICAL_DRIVE_LABEL_10_10 ,PHYSICAL_DRIVE_STATUS_10_10=:PHYSICAL_DRIVE_STATUS_10_10,PHYSICAL_DRIVE_MODEL_10_10=:PHYSICAL_DRIVE_MODEL_10_10,PHYSICAL_DRIVE_CAPACITY_10_10=:PHYSICAL_DRIVE_CAPACITY_10_10,PHYSICAL_DRIVE_SN_10_10=:PHYSICAL_DRIVE_SN_10_10,PHYSICAL_DRIVE_CONFI_10_10=:PHYSICAL_DRIVE_CONFI_10_10,PHYSICAL_DRIVE_FW_10_10=:PHYSICAL_DRIVE_FW_10_10 where IP_ILO=:IP_ILO',
                         param)
    connection.commit()
    connection.close()

def update_storage_11_info(logical_drive=None,logical_drive_status=None,logical_drive_capacity=None,logical_drive_tolerance=None,logical_drive_type=None,physical_drive_label_1=None,physical_drive_status_1=None,physical_drive_capacity_1=None,physical_drive_model_1=None,physical_drive_sn_1=None,physical_drive_confi_1=None,physical_drive_fw_1=None,
                                                                                                                               physical_drive_label_2=None,physical_drive_status_2=None,physical_drive_capacity_2=None,physical_drive_model_2=None,physical_drive_sn_2=None,physical_drive_confi_2=None,physical_drive_fw_2=None,
                                                                                                                               physical_drive_label_3=None,physical_drive_status_3=None,physical_drive_capacity_3=None,physical_drive_model_3=None,physical_drive_sn_3=None,physical_drive_confi_3=None,physical_drive_fw_3=None,
                                                                                                                               physical_drive_label_4=None,physical_drive_status_4=None,physical_drive_capacity_4=None,physical_drive_model_4=None,physical_drive_sn_4=None,physical_drive_confi_4=None,physical_drive_fw_4=None,
                                                                                                                               physical_drive_label_5=None,physical_drive_status_5=None,physical_drive_capacity_5=None,physical_drive_model_5=None,physical_drive_sn_5=None,physical_drive_confi_5=None,physical_drive_fw_5=None,
                                                                                                                               physical_drive_label_6=None,physical_drive_status_6=None,physical_drive_capacity_6=None,physical_drive_model_6=None,physical_drive_sn_6=None,physical_drive_confi_6=None,physical_drive_fw_6=None,
                                                                                                                               physical_drive_label_7=None,physical_drive_status_7=None,physical_drive_capacity_7=None,physical_drive_model_7=None,physical_drive_sn_7=None,physical_drive_confi_7=None,physical_drive_fw_7=None,
                                                                                                                               physical_drive_label_8=None,physical_drive_status_8=None,physical_drive_capacity_8=None,physical_drive_model_8=None,physical_drive_sn_8=None,physical_drive_confi_8=None,physical_drive_fw_8=None,
                                                                                                                               physical_drive_label_9=None,physical_drive_status_9=None,physical_drive_capacity_9=None,physical_drive_model_9=None,physical_drive_sn_9=None,physical_drive_confi_9=None,physical_drive_fw_9=None,
                                                                                                                               physical_drive_label_10=None,physical_drive_status_10=None,physical_drive_capacity_10=None,physical_drive_model_10=None,physical_drive_sn_10=None,physical_drive_confi_10=None,physical_drive_fw_10=None,
                                                                                                                               ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'LOGICAL_DRIVE_11': logical_drive, 'LOGICAL_DRIVE_STATUS_11': logical_drive_status, 'LOGICAL_DRIVE_CAPACITY_11': logical_drive_capacity,'LOGICAL_DRIVE_TOLERANCE_11': logical_drive_tolerance,'LOGICAL_DRIVE_TYPE_11': logical_drive_type,
    'PHYSICAL_DRIVE_LABEL_11_1': physical_drive_label_1,'PHYSICAL_DRIVE_STATUS_11_1': physical_drive_status_1,'PHYSICAL_DRIVE_MODEL_11_1': physical_drive_model_1,'PHYSICAL_DRIVE_CAPACITY_11_1': physical_drive_capacity_1,'PHYSICAL_DRIVE_SN_11_1': physical_drive_sn_1,'PHYSICAL_DRIVE_CONFI_11_1': physical_drive_confi_1,'PHYSICAL_DRIVE_FW_11_1': physical_drive_fw_1,
    'PHYSICAL_DRIVE_LABEL_11_2': physical_drive_label_2,'PHYSICAL_DRIVE_STATUS_11_2': physical_drive_status_2,'PHYSICAL_DRIVE_MODEL_11_2': physical_drive_model_2,'PHYSICAL_DRIVE_CAPACITY_11_2': physical_drive_capacity_2,'PHYSICAL_DRIVE_SN_11_2': physical_drive_sn_2,'PHYSICAL_DRIVE_CONFI_11_2': physical_drive_confi_2,'PHYSICAL_DRIVE_FW_11_2': physical_drive_fw_2,
    'PHYSICAL_DRIVE_LABEL_11_3': physical_drive_label_3,'PHYSICAL_DRIVE_STATUS_11_3': physical_drive_status_3,'PHYSICAL_DRIVE_MODEL_11_3': physical_drive_model_3,'PHYSICAL_DRIVE_CAPACITY_11_3': physical_drive_capacity_3,'PHYSICAL_DRIVE_SN_11_3': physical_drive_sn_3,'PHYSICAL_DRIVE_CONFI_11_3': physical_drive_confi_3,'PHYSICAL_DRIVE_FW_11_3': physical_drive_fw_3,
    'PHYSICAL_DRIVE_LABEL_11_4': physical_drive_label_4,'PHYSICAL_DRIVE_STATUS_11_4': physical_drive_status_4,'PHYSICAL_DRIVE_MODEL_11_4': physical_drive_model_4,'PHYSICAL_DRIVE_CAPACITY_11_4': physical_drive_capacity_4,'PHYSICAL_DRIVE_SN_11_4': physical_drive_sn_4,'PHYSICAL_DRIVE_CONFI_11_4': physical_drive_confi_4,'PHYSICAL_DRIVE_FW_11_4': physical_drive_fw_4,
    'PHYSICAL_DRIVE_LABEL_11_5': physical_drive_label_5,'PHYSICAL_DRIVE_STATUS_11_5': physical_drive_status_5,'PHYSICAL_DRIVE_MODEL_11_5': physical_drive_model_5,'PHYSICAL_DRIVE_CAPACITY_11_5': physical_drive_capacity_5,'PHYSICAL_DRIVE_SN_11_5': physical_drive_sn_5,'PHYSICAL_DRIVE_CONFI_11_5': physical_drive_confi_5,'PHYSICAL_DRIVE_FW_11_5': physical_drive_fw_5,
    'PHYSICAL_DRIVE_LABEL_11_6': physical_drive_label_6,'PHYSICAL_DRIVE_STATUS_11_6': physical_drive_status_6,'PHYSICAL_DRIVE_MODEL_11_6': physical_drive_model_6,'PHYSICAL_DRIVE_CAPACITY_11_6': physical_drive_capacity_6,'PHYSICAL_DRIVE_SN_11_6': physical_drive_sn_6,'PHYSICAL_DRIVE_CONFI_11_6': physical_drive_confi_6,'PHYSICAL_DRIVE_FW_11_6': physical_drive_fw_6,
    'PHYSICAL_DRIVE_LABEL_11_7': physical_drive_label_7,'PHYSICAL_DRIVE_STATUS_11_7': physical_drive_status_7,'PHYSICAL_DRIVE_MODEL_11_7': physical_drive_model_7,'PHYSICAL_DRIVE_CAPACITY_11_7': physical_drive_capacity_7,'PHYSICAL_DRIVE_SN_11_7': physical_drive_sn_7,'PHYSICAL_DRIVE_CONFI_11_7': physical_drive_confi_7,'PHYSICAL_DRIVE_FW_11_7': physical_drive_fw_7,
    'PHYSICAL_DRIVE_LABEL_11_8': physical_drive_label_8,'PHYSICAL_DRIVE_STATUS_11_8': physical_drive_status_8,'PHYSICAL_DRIVE_MODEL_11_8': physical_drive_model_8,'PHYSICAL_DRIVE_CAPACITY_11_8': physical_drive_capacity_8,'PHYSICAL_DRIVE_SN_11_8': physical_drive_sn_8,'PHYSICAL_DRIVE_CONFI_11_8': physical_drive_confi_8,'PHYSICAL_DRIVE_FW_11_8': physical_drive_fw_8,
    'PHYSICAL_DRIVE_LABEL_11_9': physical_drive_label_9,'PHYSICAL_DRIVE_STATUS_11_9': physical_drive_status_9,'PHYSICAL_DRIVE_MODEL_11_9': physical_drive_model_9,'PHYSICAL_DRIVE_CAPACITY_11_9': physical_drive_capacity_9,'PHYSICAL_DRIVE_SN_11_9': physical_drive_sn_9,'PHYSICAL_DRIVE_CONFI_11_9': physical_drive_confi_9,'PHYSICAL_DRIVE_FW_11_9': physical_drive_fw_9,
    'PHYSICAL_DRIVE_LABEL_11_10': physical_drive_label_10,'PHYSICAL_DRIVE_STATUS_11_10': physical_drive_status_10,'PHYSICAL_DRIVE_MODEL_11_10': physical_drive_model_10,'PHYSICAL_DRIVE_CAPACITY_11_10': physical_drive_capacity_10, 'PHYSICAL_DRIVE_SN_11_10': physical_drive_sn_10,'PHYSICAL_DRIVE_CONFI_11_10': physical_drive_confi_10, 'PHYSICAL_DRIVE_FW_11_10': physical_drive_fw_10,
    'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update STORAGE_INFO set LOGICAL_DRIVE_11=:LOGICAL_DRIVE_11,LOGICAL_DRIVE_STATUS_11=:LOGICAL_DRIVE_STATUS_11,LOGICAL_DRIVE_CAPACITY_11=:LOGICAL_DRIVE_CAPACITY_11,LOGICAL_DRIVE_TOLERANCE_11=:LOGICAL_DRIVE_TOLERANCE_11,LOGICAL_DRIVE_TYPE_11=:LOGICAL_DRIVE_TYPE_11, \
                         PHYSICAL_DRIVE_LABEL_11_1=:PHYSICAL_DRIVE_LABEL_11_1 ,PHYSICAL_DRIVE_STATUS_11_1=:PHYSICAL_DRIVE_STATUS_11_1,PHYSICAL_DRIVE_MODEL_11_1=:PHYSICAL_DRIVE_MODEL_11_1,PHYSICAL_DRIVE_CAPACITY_11_1=:PHYSICAL_DRIVE_CAPACITY_11_1,PHYSICAL_DRIVE_SN_11_1=:PHYSICAL_DRIVE_SN_11_1,PHYSICAL_DRIVE_CONFI_11_1=:PHYSICAL_DRIVE_CONFI_11_1,PHYSICAL_DRIVE_FW_11_1=:PHYSICAL_DRIVE_FW_11_1, \
                         PHYSICAL_DRIVE_LABEL_11_2=:PHYSICAL_DRIVE_LABEL_11_2 ,PHYSICAL_DRIVE_STATUS_11_2=:PHYSICAL_DRIVE_STATUS_11_2,PHYSICAL_DRIVE_MODEL_11_2=:PHYSICAL_DRIVE_MODEL_11_2,PHYSICAL_DRIVE_CAPACITY_11_2=:PHYSICAL_DRIVE_CAPACITY_11_2,PHYSICAL_DRIVE_SN_11_2=:PHYSICAL_DRIVE_SN_11_2,PHYSICAL_DRIVE_CONFI_11_2=:PHYSICAL_DRIVE_CONFI_11_2,PHYSICAL_DRIVE_FW_11_2=:PHYSICAL_DRIVE_FW_11_2, \
                         PHYSICAL_DRIVE_LABEL_11_3=:PHYSICAL_DRIVE_LABEL_11_3 ,PHYSICAL_DRIVE_STATUS_11_3=:PHYSICAL_DRIVE_STATUS_11_3,PHYSICAL_DRIVE_MODEL_11_3=:PHYSICAL_DRIVE_MODEL_11_3,PHYSICAL_DRIVE_CAPACITY_11_3=:PHYSICAL_DRIVE_CAPACITY_11_3,PHYSICAL_DRIVE_SN_11_3=:PHYSICAL_DRIVE_SN_11_3,PHYSICAL_DRIVE_CONFI_11_3=:PHYSICAL_DRIVE_CONFI_11_3,PHYSICAL_DRIVE_FW_11_3=:PHYSICAL_DRIVE_FW_11_3, \
                         PHYSICAL_DRIVE_LABEL_11_4=:PHYSICAL_DRIVE_LABEL_11_4 ,PHYSICAL_DRIVE_STATUS_11_4=:PHYSICAL_DRIVE_STATUS_11_4,PHYSICAL_DRIVE_MODEL_11_4=:PHYSICAL_DRIVE_MODEL_11_4,PHYSICAL_DRIVE_CAPACITY_11_4=:PHYSICAL_DRIVE_CAPACITY_11_4,PHYSICAL_DRIVE_SN_11_4=:PHYSICAL_DRIVE_SN_11_4,PHYSICAL_DRIVE_CONFI_11_4=:PHYSICAL_DRIVE_CONFI_11_4,PHYSICAL_DRIVE_FW_11_4=:PHYSICAL_DRIVE_FW_11_4, \
                         PHYSICAL_DRIVE_LABEL_11_5=:PHYSICAL_DRIVE_LABEL_11_5 ,PHYSICAL_DRIVE_STATUS_11_5=:PHYSICAL_DRIVE_STATUS_11_5,PHYSICAL_DRIVE_MODEL_11_5=:PHYSICAL_DRIVE_MODEL_11_5,PHYSICAL_DRIVE_CAPACITY_11_5=:PHYSICAL_DRIVE_CAPACITY_11_5,PHYSICAL_DRIVE_SN_11_5=:PHYSICAL_DRIVE_SN_11_5,PHYSICAL_DRIVE_CONFI_11_5=:PHYSICAL_DRIVE_CONFI_11_5,PHYSICAL_DRIVE_FW_11_5=:PHYSICAL_DRIVE_FW_11_5, \
                         PHYSICAL_DRIVE_LABEL_11_6=:PHYSICAL_DRIVE_LABEL_11_6 ,PHYSICAL_DRIVE_STATUS_11_6=:PHYSICAL_DRIVE_STATUS_11_6,PHYSICAL_DRIVE_MODEL_11_6=:PHYSICAL_DRIVE_MODEL_11_6,PHYSICAL_DRIVE_CAPACITY_11_6=:PHYSICAL_DRIVE_CAPACITY_11_6,PHYSICAL_DRIVE_SN_11_6=:PHYSICAL_DRIVE_SN_11_6,PHYSICAL_DRIVE_CONFI_11_6=:PHYSICAL_DRIVE_CONFI_11_6,PHYSICAL_DRIVE_FW_11_6=:PHYSICAL_DRIVE_FW_11_6, \
                         PHYSICAL_DRIVE_LABEL_11_7=:PHYSICAL_DRIVE_LABEL_11_7 ,PHYSICAL_DRIVE_STATUS_11_7=:PHYSICAL_DRIVE_STATUS_11_7,PHYSICAL_DRIVE_MODEL_11_7=:PHYSICAL_DRIVE_MODEL_11_7,PHYSICAL_DRIVE_CAPACITY_11_7=:PHYSICAL_DRIVE_CAPACITY_11_7,PHYSICAL_DRIVE_SN_11_7=:PHYSICAL_DRIVE_SN_11_7,PHYSICAL_DRIVE_CONFI_11_7=:PHYSICAL_DRIVE_CONFI_11_7,PHYSICAL_DRIVE_FW_11_7=:PHYSICAL_DRIVE_FW_11_7, \
                         PHYSICAL_DRIVE_LABEL_11_8=:PHYSICAL_DRIVE_LABEL_11_8 ,PHYSICAL_DRIVE_STATUS_11_8=:PHYSICAL_DRIVE_STATUS_11_8,PHYSICAL_DRIVE_MODEL_11_8=:PHYSICAL_DRIVE_MODEL_11_8,PHYSICAL_DRIVE_CAPACITY_11_8=:PHYSICAL_DRIVE_CAPACITY_11_8,PHYSICAL_DRIVE_SN_11_8=:PHYSICAL_DRIVE_SN_11_8,PHYSICAL_DRIVE_CONFI_11_8=:PHYSICAL_DRIVE_CONFI_11_8,PHYSICAL_DRIVE_FW_11_8=:PHYSICAL_DRIVE_FW_11_8, \
                         PHYSICAL_DRIVE_LABEL_11_9=:PHYSICAL_DRIVE_LABEL_11_9 ,PHYSICAL_DRIVE_STATUS_11_9=:PHYSICAL_DRIVE_STATUS_11_9,PHYSICAL_DRIVE_MODEL_11_9=:PHYSICAL_DRIVE_MODEL_11_9,PHYSICAL_DRIVE_CAPACITY_11_9=:PHYSICAL_DRIVE_CAPACITY_11_9,PHYSICAL_DRIVE_SN_11_9=:PHYSICAL_DRIVE_SN_11_9,PHYSICAL_DRIVE_CONFI_11_9=:PHYSICAL_DRIVE_CONFI_11_9,PHYSICAL_DRIVE_FW_11_9=:PHYSICAL_DRIVE_FW_11_9, \
                         PHYSICAL_DRIVE_LABEL_11_10=:PHYSICAL_DRIVE_LABEL_11_10 ,PHYSICAL_DRIVE_STATUS_11_10=:PHYSICAL_DRIVE_STATUS_11_10,PHYSICAL_DRIVE_MODEL_11_10=:PHYSICAL_DRIVE_MODEL_11_10,PHYSICAL_DRIVE_CAPACITY_11_10=:PHYSICAL_DRIVE_CAPACITY_11_10,PHYSICAL_DRIVE_SN_11_10=:PHYSICAL_DRIVE_SN_11_10,PHYSICAL_DRIVE_CONFI_11_10=:PHYSICAL_DRIVE_CONFI_11_10,PHYSICAL_DRIVE_FW_11_10=:PHYSICAL_DRIVE_FW_11_10 where IP_ILO=:IP_ILO',
                         param)
    connection.commit()
    connection.close()

def update_storage_12_info(logical_drive=None,logical_drive_status=None,logical_drive_capacity=None,logical_drive_tolerance=None,logical_drive_type=None,physical_drive_label_1=None,physical_drive_status_1=None,physical_drive_capacity_1=None,physical_drive_model_1=None,physical_drive_sn_1=None,physical_drive_confi_1=None,physical_drive_fw_1=None,
                                                                                                                               physical_drive_label_2=None,physical_drive_status_2=None,physical_drive_capacity_2=None,physical_drive_model_2=None,physical_drive_sn_2=None,physical_drive_confi_2=None,physical_drive_fw_2=None,
                                                                                                                               physical_drive_label_3=None,physical_drive_status_3=None,physical_drive_capacity_3=None,physical_drive_model_3=None,physical_drive_sn_3=None,physical_drive_confi_3=None,physical_drive_fw_3=None,
                                                                                                                               physical_drive_label_4=None,physical_drive_status_4=None,physical_drive_capacity_4=None,physical_drive_model_4=None,physical_drive_sn_4=None,physical_drive_confi_4=None,physical_drive_fw_4=None,
                                                                                                                               physical_drive_label_5=None,physical_drive_status_5=None,physical_drive_capacity_5=None,physical_drive_model_5=None,physical_drive_sn_5=None,physical_drive_confi_5=None,physical_drive_fw_5=None,
                                                                                                                               physical_drive_label_6=None,physical_drive_status_6=None,physical_drive_capacity_6=None,physical_drive_model_6=None,physical_drive_sn_6=None,physical_drive_confi_6=None,physical_drive_fw_6=None,
                                                                                                                               physical_drive_label_7=None,physical_drive_status_7=None,physical_drive_capacity_7=None,physical_drive_model_7=None,physical_drive_sn_7=None,physical_drive_confi_7=None,physical_drive_fw_7=None,
                                                                                                                               physical_drive_label_8=None,physical_drive_status_8=None,physical_drive_capacity_8=None,physical_drive_model_8=None,physical_drive_sn_8=None,physical_drive_confi_8=None,physical_drive_fw_8=None,
                                                                                                                               physical_drive_label_9=None,physical_drive_status_9=None,physical_drive_capacity_9=None,physical_drive_model_9=None,physical_drive_sn_9=None,physical_drive_confi_9=None,physical_drive_fw_9=None,
                                                                                                                               physical_drive_label_10=None,physical_drive_status_10=None,physical_drive_capacity_10=None,physical_drive_model_10=None,physical_drive_sn_10=None,physical_drive_confi_10=None,physical_drive_fw_10=None,
                                                                                                                               ip=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'LOGICAL_DRIVE_12': logical_drive, 'LOGICAL_DRIVE_STATUS_12': logical_drive_status, 'LOGICAL_DRIVE_CAPACITY_12': logical_drive_capacity,'LOGICAL_DRIVE_TOLERANCE_12': logical_drive_tolerance,'LOGICAL_DRIVE_TYPE_12': logical_drive_type,
    'PHYSICAL_DRIVE_LABEL_12_1': physical_drive_label_1,'PHYSICAL_DRIVE_STATUS_12_1': physical_drive_status_1,'PHYSICAL_DRIVE_MODEL_12_1': physical_drive_model_1,'PHYSICAL_DRIVE_CAPACITY_12_1': physical_drive_capacity_1,'PHYSICAL_DRIVE_SN_12_1': physical_drive_sn_1,'PHYSICAL_DRIVE_CONFI_12_1': physical_drive_confi_1,'PHYSICAL_DRIVE_FW_12_1': physical_drive_fw_1,
    'PHYSICAL_DRIVE_LABEL_12_2': physical_drive_label_2,'PHYSICAL_DRIVE_STATUS_12_2': physical_drive_status_2,'PHYSICAL_DRIVE_MODEL_12_2': physical_drive_model_2,'PHYSICAL_DRIVE_CAPACITY_12_2': physical_drive_capacity_2,'PHYSICAL_DRIVE_SN_12_2': physical_drive_sn_2,'PHYSICAL_DRIVE_CONFI_12_2': physical_drive_confi_2,'PHYSICAL_DRIVE_FW_12_2': physical_drive_fw_2,
    'PHYSICAL_DRIVE_LABEL_12_3': physical_drive_label_3,'PHYSICAL_DRIVE_STATUS_12_3': physical_drive_status_3,'PHYSICAL_DRIVE_MODEL_12_3': physical_drive_model_3,'PHYSICAL_DRIVE_CAPACITY_12_3': physical_drive_capacity_3,'PHYSICAL_DRIVE_SN_12_3': physical_drive_sn_3,'PHYSICAL_DRIVE_CONFI_12_3': physical_drive_confi_3,'PHYSICAL_DRIVE_FW_12_3': physical_drive_fw_3,
    'PHYSICAL_DRIVE_LABEL_12_4': physical_drive_label_4,'PHYSICAL_DRIVE_STATUS_12_4': physical_drive_status_4,'PHYSICAL_DRIVE_MODEL_12_4': physical_drive_model_4,'PHYSICAL_DRIVE_CAPACITY_12_4': physical_drive_capacity_4,'PHYSICAL_DRIVE_SN_12_4': physical_drive_sn_4,'PHYSICAL_DRIVE_CONFI_12_4': physical_drive_confi_4,'PHYSICAL_DRIVE_FW_12_4': physical_drive_fw_4,
    'PHYSICAL_DRIVE_LABEL_12_5': physical_drive_label_5,'PHYSICAL_DRIVE_STATUS_12_5': physical_drive_status_5,'PHYSICAL_DRIVE_MODEL_12_5': physical_drive_model_5,'PHYSICAL_DRIVE_CAPACITY_12_5': physical_drive_capacity_5,'PHYSICAL_DRIVE_SN_12_5': physical_drive_sn_5,'PHYSICAL_DRIVE_CONFI_12_5': physical_drive_confi_5,'PHYSICAL_DRIVE_FW_12_5': physical_drive_fw_5,
    'PHYSICAL_DRIVE_LABEL_12_6': physical_drive_label_6,'PHYSICAL_DRIVE_STATUS_12_6': physical_drive_status_6,'PHYSICAL_DRIVE_MODEL_12_6': physical_drive_model_6,'PHYSICAL_DRIVE_CAPACITY_12_6': physical_drive_capacity_6,'PHYSICAL_DRIVE_SN_12_6': physical_drive_sn_6,'PHYSICAL_DRIVE_CONFI_12_6': physical_drive_confi_6,'PHYSICAL_DRIVE_FW_12_6': physical_drive_fw_6,
    'PHYSICAL_DRIVE_LABEL_12_7': physical_drive_label_7,'PHYSICAL_DRIVE_STATUS_12_7': physical_drive_status_7,'PHYSICAL_DRIVE_MODEL_12_7': physical_drive_model_7,'PHYSICAL_DRIVE_CAPACITY_12_7': physical_drive_capacity_7,'PHYSICAL_DRIVE_SN_12_7': physical_drive_sn_7,'PHYSICAL_DRIVE_CONFI_12_7': physical_drive_confi_7,'PHYSICAL_DRIVE_FW_12_7': physical_drive_fw_7,
    'PHYSICAL_DRIVE_LABEL_12_8': physical_drive_label_8,'PHYSICAL_DRIVE_STATUS_12_8': physical_drive_status_8,'PHYSICAL_DRIVE_MODEL_12_8': physical_drive_model_8,'PHYSICAL_DRIVE_CAPACITY_12_8': physical_drive_capacity_8,'PHYSICAL_DRIVE_SN_12_8': physical_drive_sn_8,'PHYSICAL_DRIVE_CONFI_12_8': physical_drive_confi_8,'PHYSICAL_DRIVE_FW_12_8': physical_drive_fw_8,
    'PHYSICAL_DRIVE_LABEL_12_9': physical_drive_label_9,'PHYSICAL_DRIVE_STATUS_12_9': physical_drive_status_9,'PHYSICAL_DRIVE_MODEL_12_9': physical_drive_model_9,'PHYSICAL_DRIVE_CAPACITY_12_9': physical_drive_capacity_9,'PHYSICAL_DRIVE_SN_12_9': physical_drive_sn_9,'PHYSICAL_DRIVE_CONFI_12_9': physical_drive_confi_9,'PHYSICAL_DRIVE_FW_12_9': physical_drive_fw_9,
    'PHYSICAL_DRIVE_LABEL_12_10': physical_drive_label_10,'PHYSICAL_DRIVE_STATUS_12_10': physical_drive_status_10,'PHYSICAL_DRIVE_MODEL_12_10': physical_drive_model_10,'PHYSICAL_DRIVE_CAPACITY_12_10': physical_drive_capacity_10, 'PHYSICAL_DRIVE_SN_12_10': physical_drive_sn_10,'PHYSICAL_DRIVE_CONFI_12_10': physical_drive_confi_10, 'PHYSICAL_DRIVE_FW_12_10': physical_drive_fw_10,
    'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update STORAGE_INFO set LOGICAL_DRIVE_12=:LOGICAL_DRIVE_12,LOGICAL_DRIVE_STATUS_12=:LOGICAL_DRIVE_STATUS_12,LOGICAL_DRIVE_CAPACITY_12=:LOGICAL_DRIVE_CAPACITY_12,LOGICAL_DRIVE_TOLERANCE_12=:LOGICAL_DRIVE_TOLERANCE_12,LOGICAL_DRIVE_TYPE_12=:LOGICAL_DRIVE_TYPE_12, \
                         PHYSICAL_DRIVE_LABEL_12_1=:PHYSICAL_DRIVE_LABEL_12_1 ,PHYSICAL_DRIVE_STATUS_12_1=:PHYSICAL_DRIVE_STATUS_12_1,PHYSICAL_DRIVE_MODEL_12_1=:PHYSICAL_DRIVE_MODEL_12_1,PHYSICAL_DRIVE_CAPACITY_12_1=:PHYSICAL_DRIVE_CAPACITY_12_1,PHYSICAL_DRIVE_SN_12_1=:PHYSICAL_DRIVE_SN_12_1,PHYSICAL_DRIVE_CONFI_12_1=:PHYSICAL_DRIVE_CONFI_12_1,PHYSICAL_DRIVE_FW_12_1=:PHYSICAL_DRIVE_FW_12_1, \
                         PHYSICAL_DRIVE_LABEL_12_2=:PHYSICAL_DRIVE_LABEL_12_2 ,PHYSICAL_DRIVE_STATUS_12_2=:PHYSICAL_DRIVE_STATUS_12_2,PHYSICAL_DRIVE_MODEL_12_2=:PHYSICAL_DRIVE_MODEL_12_2,PHYSICAL_DRIVE_CAPACITY_12_2=:PHYSICAL_DRIVE_CAPACITY_12_2,PHYSICAL_DRIVE_SN_12_2=:PHYSICAL_DRIVE_SN_12_2,PHYSICAL_DRIVE_CONFI_12_2=:PHYSICAL_DRIVE_CONFI_12_2,PHYSICAL_DRIVE_FW_12_2=:PHYSICAL_DRIVE_FW_12_2, \
                         PHYSICAL_DRIVE_LABEL_12_3=:PHYSICAL_DRIVE_LABEL_12_3 ,PHYSICAL_DRIVE_STATUS_12_3=:PHYSICAL_DRIVE_STATUS_12_3,PHYSICAL_DRIVE_MODEL_12_3=:PHYSICAL_DRIVE_MODEL_12_3,PHYSICAL_DRIVE_CAPACITY_12_3=:PHYSICAL_DRIVE_CAPACITY_12_3,PHYSICAL_DRIVE_SN_12_3=:PHYSICAL_DRIVE_SN_12_3,PHYSICAL_DRIVE_CONFI_12_3=:PHYSICAL_DRIVE_CONFI_12_3,PHYSICAL_DRIVE_FW_12_3=:PHYSICAL_DRIVE_FW_12_3, \
                         PHYSICAL_DRIVE_LABEL_12_4=:PHYSICAL_DRIVE_LABEL_12_4 ,PHYSICAL_DRIVE_STATUS_12_4=:PHYSICAL_DRIVE_STATUS_12_4,PHYSICAL_DRIVE_MODEL_12_4=:PHYSICAL_DRIVE_MODEL_12_4,PHYSICAL_DRIVE_CAPACITY_12_4=:PHYSICAL_DRIVE_CAPACITY_12_4,PHYSICAL_DRIVE_SN_12_4=:PHYSICAL_DRIVE_SN_12_4,PHYSICAL_DRIVE_CONFI_12_4=:PHYSICAL_DRIVE_CONFI_12_4,PHYSICAL_DRIVE_FW_12_4=:PHYSICAL_DRIVE_FW_12_4, \
                         PHYSICAL_DRIVE_LABEL_12_5=:PHYSICAL_DRIVE_LABEL_12_5 ,PHYSICAL_DRIVE_STATUS_12_5=:PHYSICAL_DRIVE_STATUS_12_5,PHYSICAL_DRIVE_MODEL_12_5=:PHYSICAL_DRIVE_MODEL_12_5,PHYSICAL_DRIVE_CAPACITY_12_5=:PHYSICAL_DRIVE_CAPACITY_12_5,PHYSICAL_DRIVE_SN_12_5=:PHYSICAL_DRIVE_SN_12_5,PHYSICAL_DRIVE_CONFI_12_5=:PHYSICAL_DRIVE_CONFI_12_5,PHYSICAL_DRIVE_FW_12_5=:PHYSICAL_DRIVE_FW_12_5, \
                         PHYSICAL_DRIVE_LABEL_12_6=:PHYSICAL_DRIVE_LABEL_12_6 ,PHYSICAL_DRIVE_STATUS_12_6=:PHYSICAL_DRIVE_STATUS_12_6,PHYSICAL_DRIVE_MODEL_12_6=:PHYSICAL_DRIVE_MODEL_12_6,PHYSICAL_DRIVE_CAPACITY_12_6=:PHYSICAL_DRIVE_CAPACITY_12_6,PHYSICAL_DRIVE_SN_12_6=:PHYSICAL_DRIVE_SN_12_6,PHYSICAL_DRIVE_CONFI_12_6=:PHYSICAL_DRIVE_CONFI_12_6,PHYSICAL_DRIVE_FW_12_6=:PHYSICAL_DRIVE_FW_12_6, \
                         PHYSICAL_DRIVE_LABEL_12_7=:PHYSICAL_DRIVE_LABEL_12_7 ,PHYSICAL_DRIVE_STATUS_12_7=:PHYSICAL_DRIVE_STATUS_12_7,PHYSICAL_DRIVE_MODEL_12_7=:PHYSICAL_DRIVE_MODEL_12_7,PHYSICAL_DRIVE_CAPACITY_12_7=:PHYSICAL_DRIVE_CAPACITY_12_7,PHYSICAL_DRIVE_SN_12_7=:PHYSICAL_DRIVE_SN_12_7,PHYSICAL_DRIVE_CONFI_12_7=:PHYSICAL_DRIVE_CONFI_12_7,PHYSICAL_DRIVE_FW_12_7=:PHYSICAL_DRIVE_FW_12_7, \
                         PHYSICAL_DRIVE_LABEL_12_8=:PHYSICAL_DRIVE_LABEL_12_8 ,PHYSICAL_DRIVE_STATUS_12_8=:PHYSICAL_DRIVE_STATUS_12_8,PHYSICAL_DRIVE_MODEL_12_8=:PHYSICAL_DRIVE_MODEL_12_8,PHYSICAL_DRIVE_CAPACITY_12_8=:PHYSICAL_DRIVE_CAPACITY_12_8,PHYSICAL_DRIVE_SN_12_8=:PHYSICAL_DRIVE_SN_12_8,PHYSICAL_DRIVE_CONFI_12_8=:PHYSICAL_DRIVE_CONFI_12_8,PHYSICAL_DRIVE_FW_12_8=:PHYSICAL_DRIVE_FW_12_8, \
                         PHYSICAL_DRIVE_LABEL_12_9=:PHYSICAL_DRIVE_LABEL_12_9 ,PHYSICAL_DRIVE_STATUS_12_9=:PHYSICAL_DRIVE_STATUS_12_9,PHYSICAL_DRIVE_MODEL_12_9=:PHYSICAL_DRIVE_MODEL_12_9,PHYSICAL_DRIVE_CAPACITY_12_9=:PHYSICAL_DRIVE_CAPACITY_12_9,PHYSICAL_DRIVE_SN_12_9=:PHYSICAL_DRIVE_SN_12_9,PHYSICAL_DRIVE_CONFI_12_9=:PHYSICAL_DRIVE_CONFI_12_9,PHYSICAL_DRIVE_FW_12_9=:PHYSICAL_DRIVE_FW_12_9, \
                         PHYSICAL_DRIVE_LABEL_12_10=:PHYSICAL_DRIVE_LABEL_12_10 ,PHYSICAL_DRIVE_STATUS_12_10=:PHYSICAL_DRIVE_STATUS_12_10,PHYSICAL_DRIVE_MODEL_12_10=:PHYSICAL_DRIVE_MODEL_12_10,PHYSICAL_DRIVE_CAPACITY_12_10=:PHYSICAL_DRIVE_CAPACITY_12_10,PHYSICAL_DRIVE_SN_12_10=:PHYSICAL_DRIVE_SN_12_10,PHYSICAL_DRIVE_CONFI_12_10=:PHYSICAL_DRIVE_CONFI_12_10,PHYSICAL_DRIVE_FW_12_10=:PHYSICAL_DRIVE_FW_12_10 where IP_ILO=:IP_ILO',
                         param)
    connection.commit()
    connection.close()