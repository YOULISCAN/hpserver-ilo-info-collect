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



# def insert_memory_info(memory=None,socket=None,socket_status=None,socket_part_number=None,socket_type=None,socket_size=None,socket_frequency=None,socket_minimum_voltage=None,ip=None,id=None):
#     connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
#     param = {'MEMORY': memory, 'SOCKET': socket, 'SOCKET_STATUS': socket_status,
#              'SOCKET_PART_NUMBER': socket_part_number, 'SOCKET_TYPE': socket_type, 'SOCKET_SIZE': socket_size,'SOCKET_FREQUENCY': socket_frequency,'SOCKET_MINIMUM_VOLTAGE': socket_minimum_voltage,'IP_ILO': ip,'HARDWARD_ID': id}
#     with connection.cursor() as cursor:
#         cursor.execute(
#             'update MEMORY_INFO set MEMORY=:memory,SOCKET=:socket,SOCKET_STATUS=:socket_status,SOCKET_PART_NUMBER=:socket_part_number,SOCKET_TYPE=:socket_type,SOCKET_SIZE=:socket_size,SOCKET_FREQUENCY=:socket_frequency,SOCKET_MINIMUM_VOLTAGE=:socket_minimum_voltage where IP_ILO=:IP_ILO',
#             param)
#     connection.commit()
#     connection.close()

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



# def update_memory_ilo3_info(socket=None,socket_status=None,socket_size=None,ip=None):
#     connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
#     param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,'SOCKET_SIZE': socket_size,'IP_ILO': ip}
#     with connection.cursor() as cursor:
#         cursor.execute(
#             'update MEMORY_INFO set SOCKET=:socket,SOCKET_STATUS=:socket_status,SOCKET_SIZE=:socket_size where IP_ILO=:IP_ILO',param)
#     connection.commit()
#     connection.close()

def insert_memory_ilo3_info(socket=None,socket_status=None,socket_size=None,ip=None,id=None):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,'SOCKET_SIZE': socket_size,'IP_ILO': ip,'HARDWARE_ID': id}
    with connection.cursor() as cursor:
        cursor.execute(
            'INSERT INTO MEMORY_INFO(SOCKET,SOCKET_STATUS,SOCKET_SIZE,IP_ILO,HARDWARE_ID) values (:SOCKET,:SOCKET_STATUS,:SOCKET_SIZE,:IP_ILO,:HARDWARE_ID)',param)
    connection.commit()
    connection.close()


# def update_storage_info(logical_drive=None,logical_drive_status=None,logical_drive_capacity=None,logical_drive_tolerance=None,logical_drive_type=None,physical_drive_label_1=None,physical_drive_status_1=None,physical_drive_capacity_1=None,physical_drive_model_1=None,physical_drive_sn_1=None,physical_drive_confi_1=None,physical_drive_fw_1=None,
#                                                                                                                                physical_drive_label_2=None,physical_drive_status_2=None,physical_drive_capacity_2=None,physical_drive_model_2=None,physical_drive_sn_2=None,physical_drive_confi_2=None,physical_drive_fw_2=None,
#                                                                                                                                physical_drive_label_3=None,physical_drive_status_3=None,physical_drive_capacity_3=None,physical_drive_model_3=None,physical_drive_sn_3=None,physical_drive_confi_3=None,physical_drive_fw_3=None,
#                                                                                                                                physical_drive_label_4=None,physical_drive_status_4=None,physical_drive_capacity_4=None,physical_drive_model_4=None,physical_drive_sn_4=None,physical_drive_confi_4=None,physical_drive_fw_4=None,
#                                                                                                                                physical_drive_label_5=None,physical_drive_status_5=None,physical_drive_capacity_5=None,physical_drive_model_5=None,physical_drive_sn_5=None,physical_drive_confi_5=None,physical_drive_fw_5=None,
#                                                                                                                                physical_drive_label_6=None,physical_drive_status_6=None,physical_drive_capacity_6=None,physical_drive_model_6=None,physical_drive_sn_6=None,physical_drive_confi_6=None,physical_drive_fw_6=None,
#                                                                                                                                physical_drive_label_7=None,physical_drive_status_7=None,physical_drive_capacity_7=None,physical_drive_model_7=None,physical_drive_sn_7=None,physical_drive_confi_7=None,physical_drive_fw_7=None,
#                                                                                                                                physical_drive_label_8=None,physical_drive_status_8=None,physical_drive_capacity_8=None,physical_drive_model_8=None,physical_drive_sn_8=None,physical_drive_confi_8=None,physical_drive_fw_8=None,
#                                                                                                                                physical_drive_label_9=None,physical_drive_status_9=None,physical_drive_capacity_9=None,physical_drive_model_9=None,physical_drive_sn_9=None,physical_drive_confi_9=None,physical_drive_fw_9=None,
#                                                                                                                                physical_drive_label_10=None,physical_drive_status_10=None,physical_drive_capacity_10=None,physical_drive_model_10=None,physical_drive_sn_10=None,physical_drive_confi_10=None,physical_drive_fw_10=None,
#                                                                                                                                physical_drive_label_11=None,physical_drive_status_11=None,physical_drive_capacity_11=None,physical_drive_model_11=None,physical_drive_sn_11=None,physical_drive_confi_11=None,physical_drive_fw_11=None,
#                                                                                                                                physical_drive_label_12=None,physical_drive_status_12=None,physical_drive_capacity_12=None,physical_drive_model_12=None,physical_drive_sn_12=None,physical_drive_confi_12=None,physical_drive_fw_12=None,
#                                                                                                                                physical_drive_label_13=None,physical_drive_status_13=None,physical_drive_capacity_13=None,physical_drive_model_13=None,physical_drive_sn_13=None,physical_drive_confi_13=None,physical_drive_fw_13=None,
#                                                                                                                                physical_drive_label_14=None,physical_drive_status_14=None,physical_drive_capacity_14=None,physical_drive_model_14=None,physical_drive_sn_14=None,physical_drive_confi_14=None,physical_drive_fw_14=None,
#                                                                                                                                ip=None):
#     connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
#     param = {'LOGICAL_DRIVE_1': logical_drive, 'LOGICAL_DRIVE_STATUS_1': logical_drive_status, 'LOGICAL_DRIVE_CAPACITY_1': logical_drive_capacity,'LOGICAL_DRIVE_TOLERANCE_1': logical_drive_tolerance,'LOGICAL_DRIVE_TYPE_1': logical_drive_type,
#     'PHYSICAL_DRIVE_LABEL_1_1': physical_drive_label_1,'PHYSICAL_DRIVE_STATUS_1_1': physical_drive_status_1,'PHYSICAL_DRIVE_MODEL_1_1': physical_drive_model_1,'PHYSICAL_DRIVE_CAPACITY_1_1': physical_drive_capacity_1,'PHYSICAL_DRIVE_SN_1_1': physical_drive_sn_1,'PHYSICAL_DRIVE_CONFI_1_1': physical_drive_confi_1,'PHYSICAL_DRIVE_FW_1_1': physical_drive_fw_1,
#     'PHYSICAL_DRIVE_LABEL_1_2': physical_drive_label_2,'PHYSICAL_DRIVE_STATUS_1_2': physical_drive_status_2,'PHYSICAL_DRIVE_MODEL_1_2': physical_drive_model_2,'PHYSICAL_DRIVE_CAPACITY_1_2': physical_drive_capacity_2,'PHYSICAL_DRIVE_SN_1_2': physical_drive_sn_2,'PHYSICAL_DRIVE_CONFI_1_2': physical_drive_confi_2,'PHYSICAL_DRIVE_FW_1_2': physical_drive_fw_2,
#     'PHYSICAL_DRIVE_LABEL_1_3': physical_drive_label_3,'PHYSICAL_DRIVE_STATUS_1_3': physical_drive_status_3,'PHYSICAL_DRIVE_MODEL_1_3': physical_drive_model_3,'PHYSICAL_DRIVE_CAPACITY_1_3': physical_drive_capacity_3,'PHYSICAL_DRIVE_SN_1_3': physical_drive_sn_3,'PHYSICAL_DRIVE_CONFI_1_3': physical_drive_confi_3,'PHYSICAL_DRIVE_FW_1_3': physical_drive_fw_3,
#     'PHYSICAL_DRIVE_LABEL_1_4': physical_drive_label_4,'PHYSICAL_DRIVE_STATUS_1_4': physical_drive_status_4,'PHYSICAL_DRIVE_MODEL_1_4': physical_drive_model_4,'PHYSICAL_DRIVE_CAPACITY_1_4': physical_drive_capacity_4,'PHYSICAL_DRIVE_SN_1_4': physical_drive_sn_4,'PHYSICAL_DRIVE_CONFI_1_4': physical_drive_confi_4,'PHYSICAL_DRIVE_FW_1_4': physical_drive_fw_4,
#     'PHYSICAL_DRIVE_LABEL_1_5': physical_drive_label_5,'PHYSICAL_DRIVE_STATUS_1_5': physical_drive_status_5,'PHYSICAL_DRIVE_MODEL_1_5': physical_drive_model_5,'PHYSICAL_DRIVE_CAPACITY_1_5': physical_drive_capacity_5,'PHYSICAL_DRIVE_SN_1_5': physical_drive_sn_5,'PHYSICAL_DRIVE_CONFI_1_5': physical_drive_confi_5,'PHYSICAL_DRIVE_FW_1_5': physical_drive_fw_5,
#     'PHYSICAL_DRIVE_LABEL_1_6': physical_drive_label_6,'PHYSICAL_DRIVE_STATUS_1_6': physical_drive_status_6,'PHYSICAL_DRIVE_MODEL_1_6': physical_drive_model_6,'PHYSICAL_DRIVE_CAPACITY_1_6': physical_drive_capacity_6,'PHYSICAL_DRIVE_SN_1_6': physical_drive_sn_6,'PHYSICAL_DRIVE_CONFI_1_6': physical_drive_confi_6,'PHYSICAL_DRIVE_FW_1_6': physical_drive_fw_6,
#     'PHYSICAL_DRIVE_LABEL_1_7': physical_drive_label_7,'PHYSICAL_DRIVE_STATUS_1_7': physical_drive_status_7,'PHYSICAL_DRIVE_MODEL_1_7': physical_drive_model_7,'PHYSICAL_DRIVE_CAPACITY_1_7': physical_drive_capacity_7,'PHYSICAL_DRIVE_SN_1_7': physical_drive_sn_7,'PHYSICAL_DRIVE_CONFI_1_7': physical_drive_confi_7,'PHYSICAL_DRIVE_FW_1_7': physical_drive_fw_7,
#     'PHYSICAL_DRIVE_LABEL_1_8': physical_drive_label_8,'PHYSICAL_DRIVE_STATUS_1_8': physical_drive_status_8,'PHYSICAL_DRIVE_MODEL_1_8': physical_drive_model_8,'PHYSICAL_DRIVE_CAPACITY_1_8': physical_drive_capacity_8,'PHYSICAL_DRIVE_SN_1_8': physical_drive_sn_8,'PHYSICAL_DRIVE_CONFI_1_8': physical_drive_confi_8,'PHYSICAL_DRIVE_FW_1_8': physical_drive_fw_8,
#     'PHYSICAL_DRIVE_LABEL_1_9': physical_drive_label_9,'PHYSICAL_DRIVE_STATUS_1_9': physical_drive_status_9,'PHYSICAL_DRIVE_MODEL_1_9': physical_drive_model_9,'PHYSICAL_DRIVE_CAPACITY_1_9': physical_drive_capacity_9,'PHYSICAL_DRIVE_SN_1_9': physical_drive_sn_9,'PHYSICAL_DRIVE_CONFI_1_9': physical_drive_confi_9,'PHYSICAL_DRIVE_FW_1_9': physical_drive_fw_9,
#     'PHYSICAL_DRIVE_LABEL_1_10': physical_drive_label_10,'PHYSICAL_DRIVE_STATUS_1_10': physical_drive_status_10,'PHYSICAL_DRIVE_MODEL_1_10': physical_drive_model_10,'PHYSICAL_DRIVE_CAPACITY_1_10': physical_drive_capacity_10, 'PHYSICAL_DRIVE_SN_1_10': physical_drive_sn_10,'PHYSICAL_DRIVE_CONFI_1_10': physical_drive_confi_10, 'PHYSICAL_DRIVE_FW_1_10': physical_drive_fw_10,
#     'PHYSICAL_DRIVE_LABEL_1_11': physical_drive_label_11,'PHYSICAL_DRIVE_STATUS_1_11': physical_drive_status_11,'PHYSICAL_DRIVE_MODEL_1_11': physical_drive_model_11,'PHYSICAL_DRIVE_CAPACITY_1_11': physical_drive_capacity_11, 'PHYSICAL_DRIVE_SN_1_11': physical_drive_sn_11,'PHYSICAL_DRIVE_CONFI_1_11': physical_drive_confi_11, 'PHYSICAL_DRIVE_FW_1_11': physical_drive_fw_11,
#     'PHYSICAL_DRIVE_LABEL_1_12': physical_drive_label_12,'PHYSICAL_DRIVE_STATUS_1_12': physical_drive_status_12,'PHYSICAL_DRIVE_MODEL_1_12': physical_drive_model_12,'PHYSICAL_DRIVE_CAPACITY_1_12': physical_drive_capacity_12, 'PHYSICAL_DRIVE_SN_1_12': physical_drive_sn_12,'PHYSICAL_DRIVE_CONFI_1_12': physical_drive_confi_12, 'PHYSICAL_DRIVE_FW_1_12': physical_drive_fw_12,
#     'PHYSICAL_DRIVE_LABEL_1_13': physical_drive_label_13,'PHYSICAL_DRIVE_STATUS_1_13': physical_drive_status_13,'PHYSICAL_DRIVE_MODEL_1_13': physical_drive_model_13,'PHYSICAL_DRIVE_CAPACITY_1_13': physical_drive_capacity_13, 'PHYSICAL_DRIVE_SN_1_13': physical_drive_sn_13,'PHYSICAL_DRIVE_CONFI_1_13': physical_drive_confi_13, 'PHYSICAL_DRIVE_FW_1_13': physical_drive_fw_13,
#     'PHYSICAL_DRIVE_LABEL_1_14': physical_drive_label_14,'PHYSICAL_DRIVE_STATUS_1_14': physical_drive_status_14,'PHYSICAL_DRIVE_MODEL_1_14': physical_drive_model_14,'PHYSICAL_DRIVE_CAPACITY_1_14': physical_drive_capacity_14, 'PHYSICAL_DRIVE_SN_1_14': physical_drive_sn_14,'PHYSICAL_DRIVE_CONFI_1_14': physical_drive_confi_14, 'PHYSICAL_DRIVE_FW_1_14': physical_drive_fw_14,
#     'IP_ILO': ip}
#     with connection.cursor() as cursor:
#         cursor.execute(
#             'update STORAGE_INFO set LOGICAL_DRIVE_1=:LOGICAL_DRIVE_1,LOGICAL_DRIVE_STATUS_1=:LOGICAL_DRIVE_STATUS_1,LOGICAL_DRIVE_CAPACITY_1=:LOGICAL_DRIVE_CAPACITY_1,LOGICAL_DRIVE_TOLERANCE_1=:LOGICAL_DRIVE_TOLERANCE_1,LOGICAL_DRIVE_TYPE_1=:LOGICAL_DRIVE_TYPE_1, \
#              PHYSICAL_DRIVE_LABEL_1_1=:PHYSICAL_DRIVE_LABEL_1_1 ,PHYSICAL_DRIVE_STATUS_1_1=:PHYSICAL_DRIVE_STATUS_1_1,PHYSICAL_DRIVE_MODEL_1_1=:PHYSICAL_DRIVE_MODEL_1_1,PHYSICAL_DRIVE_CAPACITY_1_1=:PHYSICAL_DRIVE_CAPACITY_1_1,PHYSICAL_DRIVE_SN_1_1=:PHYSICAL_DRIVE_SN_1_1,PHYSICAL_DRIVE_CONFI_1_1=:PHYSICAL_DRIVE_CONFI_1_1,PHYSICAL_DRIVE_FW_1_1=:PHYSICAL_DRIVE_FW_1_1, \
#              PHYSICAL_DRIVE_LABEL_1_2=:PHYSICAL_DRIVE_LABEL_1_2 ,PHYSICAL_DRIVE_STATUS_1_2=:PHYSICAL_DRIVE_STATUS_1_2,PHYSICAL_DRIVE_MODEL_1_2=:PHYSICAL_DRIVE_MODEL_1_2,PHYSICAL_DRIVE_CAPACITY_1_2=:PHYSICAL_DRIVE_CAPACITY_1_2,PHYSICAL_DRIVE_SN_1_2=:PHYSICAL_DRIVE_SN_1_2,PHYSICAL_DRIVE_CONFI_1_2=:PHYSICAL_DRIVE_CONFI_1_2,PHYSICAL_DRIVE_FW_1_2=:PHYSICAL_DRIVE_FW_1_2, \
#              PHYSICAL_DRIVE_LABEL_1_3=:PHYSICAL_DRIVE_LABEL_1_3 ,PHYSICAL_DRIVE_STATUS_1_3=:PHYSICAL_DRIVE_STATUS_1_3,PHYSICAL_DRIVE_MODEL_1_3=:PHYSICAL_DRIVE_MODEL_1_3,PHYSICAL_DRIVE_CAPACITY_1_3=:PHYSICAL_DRIVE_CAPACITY_1_3,PHYSICAL_DRIVE_SN_1_3=:PHYSICAL_DRIVE_SN_1_3,PHYSICAL_DRIVE_CONFI_1_3=:PHYSICAL_DRIVE_CONFI_1_3,PHYSICAL_DRIVE_FW_1_3=:PHYSICAL_DRIVE_FW_1_3, \
#              PHYSICAL_DRIVE_LABEL_1_4=:PHYSICAL_DRIVE_LABEL_1_4 ,PHYSICAL_DRIVE_STATUS_1_4=:PHYSICAL_DRIVE_STATUS_1_4,PHYSICAL_DRIVE_MODEL_1_4=:PHYSICAL_DRIVE_MODEL_1_4,PHYSICAL_DRIVE_CAPACITY_1_4=:PHYSICAL_DRIVE_CAPACITY_1_4,PHYSICAL_DRIVE_SN_1_4=:PHYSICAL_DRIVE_SN_1_4,PHYSICAL_DRIVE_CONFI_1_4=:PHYSICAL_DRIVE_CONFI_1_4,PHYSICAL_DRIVE_FW_1_4=:PHYSICAL_DRIVE_FW_1_4, \
#              PHYSICAL_DRIVE_LABEL_1_5=:PHYSICAL_DRIVE_LABEL_1_5 ,PHYSICAL_DRIVE_STATUS_1_5=:PHYSICAL_DRIVE_STATUS_1_5,PHYSICAL_DRIVE_MODEL_1_5=:PHYSICAL_DRIVE_MODEL_1_5,PHYSICAL_DRIVE_CAPACITY_1_5=:PHYSICAL_DRIVE_CAPACITY_1_5,PHYSICAL_DRIVE_SN_1_5=:PHYSICAL_DRIVE_SN_1_5,PHYSICAL_DRIVE_CONFI_1_5=:PHYSICAL_DRIVE_CONFI_1_5,PHYSICAL_DRIVE_FW_1_5=:PHYSICAL_DRIVE_FW_1_5, \
#              PHYSICAL_DRIVE_LABEL_1_6=:PHYSICAL_DRIVE_LABEL_1_6 ,PHYSICAL_DRIVE_STATUS_1_6=:PHYSICAL_DRIVE_STATUS_1_6,PHYSICAL_DRIVE_MODEL_1_6=:PHYSICAL_DRIVE_MODEL_1_6,PHYSICAL_DRIVE_CAPACITY_1_6=:PHYSICAL_DRIVE_CAPACITY_1_6,PHYSICAL_DRIVE_SN_1_6=:PHYSICAL_DRIVE_SN_1_6,PHYSICAL_DRIVE_CONFI_1_6=:PHYSICAL_DRIVE_CONFI_1_6,PHYSICAL_DRIVE_FW_1_6=:PHYSICAL_DRIVE_FW_1_6, \
#              PHYSICAL_DRIVE_LABEL_1_7=:PHYSICAL_DRIVE_LABEL_1_7 ,PHYSICAL_DRIVE_STATUS_1_7=:PHYSICAL_DRIVE_STATUS_1_7,PHYSICAL_DRIVE_MODEL_1_7=:PHYSICAL_DRIVE_MODEL_1_7,PHYSICAL_DRIVE_CAPACITY_1_7=:PHYSICAL_DRIVE_CAPACITY_1_7,PHYSICAL_DRIVE_SN_1_7=:PHYSICAL_DRIVE_SN_1_7,PHYSICAL_DRIVE_CONFI_1_7=:PHYSICAL_DRIVE_CONFI_1_7,PHYSICAL_DRIVE_FW_1_7=:PHYSICAL_DRIVE_FW_1_7, \
#              PHYSICAL_DRIVE_LABEL_1_8=:PHYSICAL_DRIVE_LABEL_1_8 ,PHYSICAL_DRIVE_STATUS_1_8=:PHYSICAL_DRIVE_STATUS_1_8,PHYSICAL_DRIVE_MODEL_1_8=:PHYSICAL_DRIVE_MODEL_1_8,PHYSICAL_DRIVE_CAPACITY_1_8=:PHYSICAL_DRIVE_CAPACITY_1_8,PHYSICAL_DRIVE_SN_1_8=:PHYSICAL_DRIVE_SN_1_8,PHYSICAL_DRIVE_CONFI_1_8=:PHYSICAL_DRIVE_CONFI_1_8,PHYSICAL_DRIVE_FW_1_8=:PHYSICAL_DRIVE_FW_1_8, \
#              PHYSICAL_DRIVE_LABEL_1_9=:PHYSICAL_DRIVE_LABEL_1_9 ,PHYSICAL_DRIVE_STATUS_1_9=:PHYSICAL_DRIVE_STATUS_1_9,PHYSICAL_DRIVE_MODEL_1_9=:PHYSICAL_DRIVE_MODEL_1_9,PHYSICAL_DRIVE_CAPACITY_1_9=:PHYSICAL_DRIVE_CAPACITY_1_9,PHYSICAL_DRIVE_SN_1_9=:PHYSICAL_DRIVE_SN_1_9,PHYSICAL_DRIVE_CONFI_1_9=:PHYSICAL_DRIVE_CONFI_1_9,PHYSICAL_DRIVE_FW_1_9=:PHYSICAL_DRIVE_FW_1_9, \
#              PHYSICAL_DRIVE_LABEL_1_10=:PHYSICAL_DRIVE_LABEL_1_10 ,PHYSICAL_DRIVE_STATUS_1_10=:PHYSICAL_DRIVE_STATUS_1_10,PHYSICAL_DRIVE_MODEL_1_10=:PHYSICAL_DRIVE_MODEL_1_10,PHYSICAL_DRIVE_CAPACITY_1_10=:PHYSICAL_DRIVE_CAPACITY_1_10,PHYSICAL_DRIVE_SN_1_10=:PHYSICAL_DRIVE_SN_1_10,PHYSICAL_DRIVE_CONFI_1_10=:PHYSICAL_DRIVE_CONFI_1_10,PHYSICAL_DRIVE_FW_1_10=:PHYSICAL_DRIVE_FW_1_10, \
#              PHYSICAL_DRIVE_LABEL_1_11=:PHYSICAL_DRIVE_LABEL_1_11 ,PHYSICAL_DRIVE_STATUS_1_11=:PHYSICAL_DRIVE_STATUS_1_11,PHYSICAL_DRIVE_MODEL_1_11=:PHYSICAL_DRIVE_MODEL_1_11,PHYSICAL_DRIVE_CAPACITY_1_11=:PHYSICAL_DRIVE_CAPACITY_1_11,PHYSICAL_DRIVE_SN_1_11=:PHYSICAL_DRIVE_SN_1_11,PHYSICAL_DRIVE_CONFI_1_11=:PHYSICAL_DRIVE_CONFI_1_11,PHYSICAL_DRIVE_FW_1_11=:PHYSICAL_DRIVE_FW_1_11, \
#              PHYSICAL_DRIVE_LABEL_1_12=:PHYSICAL_DRIVE_LABEL_1_12 ,PHYSICAL_DRIVE_STATUS_1_12=:PHYSICAL_DRIVE_STATUS_1_12,PHYSICAL_DRIVE_MODEL_1_12=:PHYSICAL_DRIVE_MODEL_1_12,PHYSICAL_DRIVE_CAPACITY_1_12=:PHYSICAL_DRIVE_CAPACITY_1_12,PHYSICAL_DRIVE_SN_1_12=:PHYSICAL_DRIVE_SN_1_12,PHYSICAL_DRIVE_CONFI_1_12=:PHYSICAL_DRIVE_CONFI_1_12,PHYSICAL_DRIVE_FW_1_12=:PHYSICAL_DRIVE_FW_1_12, \
#              PHYSICAL_DRIVE_LABEL_1_13=:PHYSICAL_DRIVE_LABEL_1_13 ,PHYSICAL_DRIVE_STATUS_1_13=:PHYSICAL_DRIVE_STATUS_1_13,PHYSICAL_DRIVE_MODEL_1_13=:PHYSICAL_DRIVE_MODEL_1_13,PHYSICAL_DRIVE_CAPACITY_1_13=:PHYSICAL_DRIVE_CAPACITY_1_13,PHYSICAL_DRIVE_SN_1_13=:PHYSICAL_DRIVE_SN_1_13,PHYSICAL_DRIVE_CONFI_1_13=:PHYSICAL_DRIVE_CONFI_1_13,PHYSICAL_DRIVE_FW_1_13=:PHYSICAL_DRIVE_FW_1_13, \
#              PHYSICAL_DRIVE_LABEL_1_14=:PHYSICAL_DRIVE_LABEL_1_14 ,PHYSICAL_DRIVE_STATUS_1_14=:PHYSICAL_DRIVE_STATUS_1_14,PHYSICAL_DRIVE_MODEL_1_14=:PHYSICAL_DRIVE_MODEL_1_14,PHYSICAL_DRIVE_CAPACITY_1_14=:PHYSICAL_DRIVE_CAPACITY_1_14,PHYSICAL_DRIVE_SN_1_14=:PHYSICAL_DRIVE_SN_1_14,PHYSICAL_DRIVE_CONFI_1_14=:PHYSICAL_DRIVE_CONFI_1_14,PHYSICAL_DRIVE_FW_1_14=:PHYSICAL_DRIVE_FW_1_14 where IP_ILO=:IP_ILO',
#              param)
#     connection.commit()
#     connection.close()


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
            , param)
    connection.commit()
    connection.close()



def insert_power_info():
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    param = {'SOCKET': socket, 'SOCKET_STATUS': socket_status,
             'SOCKET_PART_NUMBER': socket_part_number, 'SOCKET_TYPE': socket_type, 'SOCKET_SIZE': socket_size,
             'SOCKET_FREQUENCY': socket_frequency, 'SOCKET_MINIMUM_VOLTAGE': socket_minimum_voltage, 'IP_ILO': ip}
    with connection.cursor() as cursor:
        cursor.execute(
            'update MEMORY_INFO set SOCKET_8=:socket,SOCKET_8_STATUS=:socket_status,SOCKET_8_PART_NUMBER=:socket_part_number,SOCKET_8_TYPE=:socket_type,SOCKET_8_SIZE=:socket_size,SOCKET_8_FREQUENCY=:socket_frequency,SOCKET_8_MINIMUM_VOLTAGE=:socket_minimum_voltage where IP_ILO=:IP_ILO',
            param)
    connection.commit()
    connection.close()
