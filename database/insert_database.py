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
    param = {'BIOS_HARDWARE_STATUS': bios_hardware, 'FANS_STATUS': fans, 'TEMPERATURE_STATUS': temperature,
             'POWER_SUPPLIES_STATUS': power_supplies, 'BATTERY_STATUS': battery, 'PROCESSOR_STATUS': processor,
             'MEMORY_STATUS': memory, 'NETWORK_STATUS':network,'STORAGE_STATUS':storage,'IP_ILO':ip}
    print(param)
    with connection.cursor() as cursor:
        cursor.execute('update ILO_INFO set BIOS_HARDWARE_STATUS=:BIOS_HARDWARE_STATUS,FANS_STATUS=:FANS_STATUS,TEMPERATURE_STATUS=:TEMPERATURE_STATUS,POWER_SUPPLIES_STATUS=:POWER_SUPPLIES_STATUS,BATTERY_STATUS=:BATTERY_STATUS,PROCESSOR_STATUS=:PROCESSOR_STATUS,MEMORY_STATUS=:MEMORY_STATUS,NETWORK_STATUS=:NETWORK_STATUS,STORAGE_STATUS=:STORAGE_STATUS where IP_ILO=:IP_ILO',param)
    connection.commit()
    connection.close()

def insert_fan_info(fan_status=None,fan_speed=None,fan_location=None,fan_label=None,ip=None,id=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'HARDWARE_ID': id,'FAN_STATUS': fan_status,'FAN_SPEED': fan_speed,'FAN_LOCATION': fan_location,'FAN_LABEL': fan_label,'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute('INSERT INTO FANS_INFO(HARDWARE_ID,IP_ILO,FAN_STATUS,FAN_SPEED,FAN_LOCATION,FAN_LABEL) values(:HARDWARE_ID,:IP_ILO,:FAN_STATUS,:FAN_SPEED,:FAN_LOCATION,:FAN_LABEL)',param)
    connection.commit()
    connection.close()
#


def insert_network_info(network_name=None,network_status=None,network_ipaddr=None,network_macaddr=None,network_port=None, ip=None, id=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'NETWORK_NAME': network_name,'NETWORK_STATUS': network_status, 'NETWORK_IPADDR': network_ipaddr, 'NETWORK_MACADDR': network_macaddr,
             'NETWORK_PORT': network_port, 'IP_ILO': ip, 'HARDWARE_ID': id}
    with connection.cursor() as cursor:
        cursor.execute(
            'INSERT INTO NETWORK_INFO(NETWORK,NETWORK_STATUS,NETWORK_IPADDR,NETWORK_MACADDR,NETWORK_PORT,IP_ILO,HARDWARE_ID) values(:NETWORK_NAME,:NETWORK_STATUS,:NETWORK_IPADDR,:NETWORK_MACADDR,:NETWORK_PORT,:IP_ILO,:HARDWARE_ID)',param)
    connection.commit()
    connection.close()


def insert_memory_info(memory=None,socket=None,socket_status=None,socket_part_number=None,socket_type=None,socket_size=None,socket_frequency=None,socket_minimum_voltage=None,ip=None,id=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'MEMORY': memory, 'SOCKET': socket, 'SOCKET_STATUS': socket_status,
             'SOCKET_PART_NUMBER': socket_part_number, 'SOCKET_TYPE': socket_type, 'SOCKET_SIZE': socket_size,'SOCKET_FREQUENCY': socket_frequency,'SOCKET_MINIMUM_VOLTAGE': socket_minimum_voltage,'IP_ILO': ip,'HARDWARE_ID': id}
    with connection.cursor() as cursor:
        cursor.execute(
            'INSERT INTO MEMORY_INFO(MEMORY,SOCKET,SOCKET_STATUS,SOCKET_PART_NUMBER,SOCKET_TYPE,SOCKET_SIZE,SOCKET_FREQUENCY,SOCKET_MINIMUM_VOLTAGE,IP_ILO,HARDWARE_ID) values(:MEMORY,:SOCKET,:SOCKET_STATUS,:SOCKET_PART_NUMBER,:SOCKET_TYPE,:SOCKET_SIZE,:SOCKET_FREQUENCY,:SOCKET_MINIMUM_VOLTAGE,:IP_ILO,:HARDWARE_ID)'
            ,param)
    connection.commit()
    connection.close()


def insert_memory_ilo3_info(socket=None,socket_status=None,socket_size=None,ip=None,id=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,'SOCKET_SIZE': socket_size,'IP_ILO': ip,'HARDWARE_ID': id}
    with connection.cursor() as cursor:
        cursor.execute(
            'INSERT INTO MEMORY_INFO(SOCKET,SOCKET_STATUS,SOCKET_SIZE,IP_ILO,HARDWARE_ID) values (:SOCKET,:SOCKET_STATUS,:SOCKET_SIZE,:IP_ILO,:HARDWARE_ID)',param)
    connection.commit()
    connection.close()



def insert_storage_info(logical_drive=None,logical_drive_status=None,logical_drive_capacity=None,logical_drive_tolerance=None,logical_drive_type=None,physical_drive_label=None,physical_drive_status=None,physical_drive_capacity=None,physical_drive_model=None,physical_drive_sn=None,physical_drive_confi=None,physical_drive_fw=None,ip=None,id=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'LOGICAL_DRIVE': logical_drive, 'LOGICAL_DRIVE_STATUS': logical_drive_status, 'LOGICAL_DRIVE_CAPACITY': logical_drive_capacity,'LOGICAL_DRIVE_TOLERANCE': logical_drive_tolerance,'LOGICAL_DRIVE_TYPE': logical_drive_type,
    'PHYSICAL_DRIVE_LABEL': physical_drive_label,'PHYSICAL_DRIVE_STATUS': physical_drive_status,'PHYSICAL_DRIVE_MODEL': physical_drive_model,'PHYSICAL_DRIVE_CAPACITY': physical_drive_capacity,'PHYSICAL_DRIVE_SN': physical_drive_sn,'PHYSICAL_DRIVE_CONFI': physical_drive_confi,'PHYSICAL_DRIVE_FW': physical_drive_fw,
    'IP_ILO': ip,'HARDWARE_ID': id}
    with connection.cursor() as cursor:
        cursor.execute(
            'INSERT INTO STORAGE_INFO(LOGICAL_DRIVE,LOGICAL_DRIVE_STATUS,LOGICAL_DRIVE_CAPACITY,LOGICAL_DRIVE_TOLERANCE,LOGICAL_DRIVE_TYPE, \
             PHYSICAL_DRIVE_LABEL,PHYSICAL_DRIVE_STATUS,PHYSICAL_DRIVE_MODEL,PHYSICAL_DRIVE_CAPACITY,PHYSICAL_DRIVE_SN,PHYSICAL_DRIVE_CONFI,PHYSICAL_DRIVE_FW,IP_ILO,HARDWARE_ID) values(:LOGICAL_DRIVE,:LOGICAL_DRIVE_STATUS,:LOGICAL_DRIVE_CAPACITY,:LOGICAL_DRIVE_TOLERANCE,:LOGICAL_DRIVE_TYPE,\
             :PHYSICAL_DRIVE_LABEL,:PHYSICAL_DRIVE_STATUS,:PHYSICAL_DRIVE_MODEL,:PHYSICAL_DRIVE_CAPACITY,:PHYSICAL_DRIVE_SN,:PHYSICAL_DRIVE_CONFI,:PHYSICAL_DRIVE_FW,:IP_ILO,:HARDWARE_ID)'
             ,param)
    connection.commit()
    connection.close()

def insert_storage_ilo3_info(physical_drive_label,physical_drive_status,physical_drive_sn,ip,id):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {
             'PHYSICAL_DRIVE_LABEL': physical_drive_label, 'PHYSICAL_DRIVE_STATUS': physical_drive_status,
             'PHYSICAL_DRIVE_SN': physical_drive_sn,
             'IP_ILO': ip, 'HARDWARE_ID': id}
    with connection.cursor() as cursor:
        cursor.execute(
            'INSERT INTO STORAGE_INFO(PHYSICAL_DRIVE_LABEL,PHYSICAL_DRIVE_STATUS,PHYSICAL_DRIVE_SN,IP_ILO,HARDWARE_ID) values(:PHYSICAL_DRIVE_LABEL,:PHYSICAL_DRIVE_STATUS,:PHYSICAL_DRIVE_SN,:IP_ILO,:HARDWARE_ID)'
            ,param)
    connection.commit()
    connection.close()

def insert_power_info(power_supplies_label=None,power_supplies_status=None,power_supplies_sn=None,power_supplies_capacity=None,power_supplies_hotplug=None,power_supplies_model=None,
                      power_supplies_present=None,power_supplies_spare=None,power_supplies_fw=None,power_supplies_pds=None,ip=None,id=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param= {
               'POWER_SUPPLY': power_supplies_label, 'POWER_SUPPLY_STATUS': power_supplies_status, 'POWER_SUPPLY_CAPACITY': power_supplies_capacity,
               'POWER_SUPPLY_PRESENT': power_supplies_present,'POWER_SUPPLY_MODEL': power_supplies_model,'POWER_SUPPLY_SPARE': power_supplies_spare,
               'POWER_SUPPLY_HOTPLUG': power_supplies_hotplug,'POWER_SUPPLY_SN': power_supplies_sn,'POWER_SUPPLY_PDS': power_supplies_pds,'POWER_SUPPLY_FW': power_supplies_fw,
               'IP_ILO': ip,'HARDWARE_ID': id
    }
    with connection.cursor() as cursor:
        cursor.execute(
            'INSERT INTO BATTERY_INFO(POWER_SUPPLY,POWER_SUPPLY_STATUS,POWER_SUPPLY_CAPACITY,POWER_SUPPLY_PRESENT,POWER_SUPPLY_MODEL,POWER_SUPPLY_SPARE,POWER_SUPPLY_FW,POWER_SUPPLY_HOTPLUG,POWER_SUPPLY_SN,POWER_SUPPLY_PDS,IP_ILO,HARDWARE_ID) values(:POWER_SUPPLY,:POWER_SUPPLY_STATUS,:POWER_SUPPLY_CAPACITY,:POWER_SUPPLY_PRESENT,:POWER_SUPPLY_MODEL,:POWER_SUPPLY_SPARE,:POWER_SUPPLY_FW,:POWER_SUPPLY_HOTPLUG,:POWER_SUPPLY_SN,:POWER_SUPPLY_PDS,:IP_ILO,:HARDWARE_ID)'
            ,param)
    connection.commit()
    connection.close()

def insert_power_ilo3_info(power_supplies_label=None,power_supplies_status=None,ip=None,id=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param= {
               'POWER_SUPPLY': power_supplies_label, 'POWER_SUPPLY_STATUS': power_supplies_status,
               'IP_ILO': ip,'HARDWARE_ID': id
    }
    with connection.cursor() as cursor:
        cursor.execute(
            'INSERT INTO BATTERY_INFO(POWER_SUPPLY,POWER_SUPPLY_STATUS,IP_ILO,HARDWARE_ID) values(:POWER_SUPPLY,:POWER_SUPPLY_STATUS,:IP_ILO,:HARDWARE_ID)'
            ,param)
    connection.commit()
    connection.close()

def update_power_sum_info(high_efficiency_mode=None, power_redundancy_status=None, power_management_control_fw=None, present_power_reading=None, power_system_redundancy=None,ip=None,id=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {
        'HIGH_EFFICIENCY_MODE': high_efficiency_mode, 'POWER_REDUNDANCY_STATUS': power_redundancy_status,'POWER_MANAGEMENT_CONTROL_FW': power_management_control_fw,'PRESENT_POWER_READING': present_power_reading,'POWER_SYSTEM_REDUNDANCY': power_system_redundancy,
        'IP_ILO': ip
    }
    with connection.cursor() as cursor:
        cursor.execute(
            'UPDATE BATTERY_INFO SET HIGH_EFFICIENCY_MODE=:HIGH_EFFICIENCY_MODE,POWER_REDUNDANCY_STATUS=:POWER_REDUNDANCY_STATUS,POWER_MANAGEMENT_CONTROL_FW=:POWER_MANAGEMENT_CONTROL_FW,PRESENT_POWER_READING=:PRESENT_POWER_READING,POWER_SYSTEM_REDUNDANCY=:POWER_SYSTEM_REDUNDANCY where IP_ILO=:IP_ILO'
            ,param)
    connection.commit()
    connection.close()


def insert_processor_info(processor_name=None,processor_status=None,processor_label=None,processor_execution_technology=None,processor_internal_l1_cache=None,processor_internal_l2_cache=None,processor_internal_l3_cache=None,processor_memory_technology=None,processor_speed=None,ip=None,id=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param= {
               'PROCESSOR_NAME': processor_name,'PROCESSOR_STATUS': processor_status,'PROCESSOR_LABEL': processor_label, 'PROCESSOR_EXE_TECH': processor_execution_technology, 'PROCESSOR_INTER_L1_CACHE': processor_internal_l1_cache,'PROCESSOR_INTER_L2_CACHE': processor_internal_l2_cache,
               'PROCESSOR_INTER_L3_CACHE': processor_internal_l3_cache, 'PROCESSOR_MEMORY_TECH': processor_memory_technology, 'PROCESSOR_SPEED': processor_speed,
               'IP_ILO': ip,'HARDWARE_ID': id}
    with connection.cursor() as cursor:
        cursor.execute(
            'INSERT INTO PROCESSOR_INFO(PROCESSOR_NAME,PROCESSOR_STATUS,PROCESSOR_LABEL,PROCESSOR_EXE_TECH,PROCESSOR_INTER_L1_CACHE,PROCESSOR_INTER_L2_CACHE,PROCESSOR_INTER_L3_CACHE,PROCESSOR_MEMORY_TECH,PROCESSOR_SPEED,IP_ILO,HARDWARE_ID) values(:PROCESSOR_NAME,:PROCESSOR_STATUS,:PROCESSOR_LABEL,:PROCESSOR_EXE_TECH,:PROCESSOR_INTER_L1_CACHE,:PROCESSOR_INTER_L2_CACHE,:PROCESSOR_INTER_L3_CACHE,:PROCESSOR_MEMORY_TECH,:PROCESSOR_SPEED,:IP_ILO,:HARDWARE_ID)'
            ,param)
    connection.commit()
    connection.close()


