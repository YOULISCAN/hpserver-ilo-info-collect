# -*- coding: utf-8 -*-

import cx_Oracle
import hpilo
import database.login_database as db
import analyse_json
import database.insert_database as insert_db
import subprocess
import threading
import queue
import time
import ssl
import re


q = queue.Queue()

def test():
    #多线程测试
    while not q.empty():
        ip = q.get()
        ip = ip.lstrip("'").rstrip("'")
        print(ip)
        ilo = hpilo.Ilo(ip, login='MonitorTools', password='ping.p.shen@foxconn.com')
        server_name = ilo.get_server_name()  #获取主机名
        product_name = ilo.get_product_name()  # 获取产品型号
        fw_version_info = ilo.get_fw_version()
        health_info = ilo.get_embedded_health()
        s = analyse_json.get_firmware_info(fw_version_info)# 获取FW版本信息
        ilo_model = s['management_processor']
        fw_version = s['firmware_version']
        fw_data = s['firmware_date']
        general_info = analyse_json.get_glance_info(health_info,fw_version)
        bios_hardware = general_info['bios_hardware']
        fans = general_info['fans']
        temperature = general_info['temperature']
        power_supplies = general_info['power_supplies']
        battery = general_info['battery']
        processor = general_info['processor']
        memory = general_info['memory']
        network = general_info['network']
        storage = general_info['storage']

        fan_all = analyse_json.get_fan_info(ilo_model, health_info)


#        insert_db.update_fw_info(product_name,server_name,ilo_model,fw_version,fw_data,ip)
#        insert_db.update_server_general_info(bios_hardware,fans,temperature,power_supplies,battery,processor,memory,network,storage,ip)
            #以上是获取硬件大体信息
            #以下是获取硬件详细信息
        def fan_info(ip):
            for i in range(1, 9):
                try:
                    fan_status, fan_speed, fan_location, fan_label= fan_all.next()
                except StopIteration:
                    fan_status, fan_speed, fan_location = ('Not Installed','0','None')
                print(fan_status, fan_speed, fan_location)  #
                if i == 1:
                    insert_db.update_fan1_info(fan_status,fan_speed,fan_location,fan_label,ip)
                elif i == 2:
                    insert_db.update_fan2_info(fan_status,fan_speed,fan_location,fan_label,ip)
                elif i == 3:
                    insert_db.update_fan3_info(fan_status,fan_speed,fan_location,fan_label,ip)
                elif i == 4:
                    insert_db.update_fan4_info(fan_status,fan_speed,fan_location,fan_label,ip)
                elif i == 5:
                    insert_db.update_fan5_info(fan_status,fan_speed,fan_location,fan_label,ip)
                elif i == 6:
                    insert_db.update_fan6_info(fan_status,fan_speed,fan_location,fan_label,ip)
                # insert_db.update_server_general_info(fan_status,fan_speed,fan_location)
        #fan_info(ip)
        def network_info(ip):
           for i in range(1,11):
               try:
                    network_name, network_status,network_ipaddr, network_macaddr, network_port = network_all.next()
               except StopIteration:
                   network_name, network_status,network_ipaddr, network_macaddr, network_port = (None,None,None,None,None)
               print(network_name,network_status,network_ipaddr,network_macaddr,network_port)
               if i == 1:
                   insert_db.update_network1_info(network_name,network_status,network_ipaddr,network_macaddr,network_port,ip)
               elif i == 2:
                   insert_db.update_network2_info(network_name,network_status,network_ipaddr,network_macaddr,network_port,ip)
               elif i == 3:
                   insert_db.update_network3_info(network_name,network_status,network_ipaddr,network_macaddr,network_port,ip)
               elif i == 4:
                   insert_db.update_network4_info(network_name,network_status,network_ipaddr,network_macaddr,network_port,ip)
               elif i == 5:
                   insert_db.update_network5_info(network_name,network_status,network_ipaddr,network_macaddr,network_port,ip)
               elif i == 6:
                   insert_db.update_network6_info(network_name,network_status,network_ipaddr,network_macaddr,network_port,ip)
               elif i == 7:
                   insert_db.update_network7_info(network_name,network_status,network_ipaddr,network_macaddr,network_port,ip)
               elif i == 8:
                   insert_db.update_network8_info(network_name,network_status,network_ipaddr,network_macaddr,network_port,ip)
               elif i == 9:
                   insert_db.update_network9_info(network_name,network_status,network_ipaddr,network_macaddr,network_port,ip)
               elif i == 10:
                   insert_db.update_network10_info(network_name,network_status,network_ipaddr,network_macaddr,network_port,ip)

        if ilo_model != 'iLO3':
            network_xml = ilo.xmldata()
            network_all = analyse_json.get_network_info(network_xml)
            network_info(ip)

        def memory_info(memory_all,ip):
            for j in range(0,2):
                for i in range(0,12):
                    try:
                        memory,socket,socket_status,socket_part_number,socket_type,socket_size,socket_frequency,socket_minimum_voltage = memory_all.next()
                    except StopIteration:
                        memory, socket, socket_status, socket_part_number, socket_type, socket_size, socket_frequency, socket_minimum_voltage = (None,None,None,None,None,None,None,None)
                    print(memory,socket,socket_status,socket_part_number,socket_type,socket_size,socket_frequency,socket_minimum_voltage)
                    if memory == 'CPU_1':
                        if i == 1:
                            insert_db.update_memory1_info(memory,socket,socket_status,socket_part_number,socket_type,socket_size,socket_frequency,socket_minimum_voltage,ip)
                        elif i == 2:
                            insert_db.update_memory2_info(memory,socket,socket_status,socket_part_number,socket_type,socket_size,socket_frequency,socket_minimum_voltage,ip)
                        elif i == 3:
                            insert_db.update_memory3_info(memory,socket,socket_status,socket_part_number,socket_type,socket_size,socket_frequency,socket_minimum_voltage,ip)
                        elif i == 4:
                            insert_db.update_memory4_info(memory,socket,socket_status,socket_part_number,socket_type,socket_size,socket_frequency,socket_minimum_voltage,ip)
                        elif i == 5:
                            insert_db.update_memory5_info(memory,socket,socket_status,socket_part_number,socket_type,socket_size,socket_frequency,socket_minimum_voltage,ip)
                        elif i == 6:
                            insert_db.update_memory6_info(memory,socket,socket_status,socket_part_number,socket_type,socket_size,socket_frequency,socket_minimum_voltage,ip)
                        elif i == 7:
                            insert_db.update_memory7_info(memory,socket,socket_status,socket_part_number,socket_type,socket_size,socket_frequency,socket_minimum_voltage,ip)
                        elif i == 8:
                            insert_db.update_memory8_info(memory,socket,socket_status,socket_part_number,socket_type,socket_size,socket_frequency,socket_minimum_voltage,ip)
                        elif i == 9:
                            insert_db.update_memory9_info(memory,socket,socket_status,socket_part_number,socket_type,socket_size,socket_frequency,socket_minimum_voltage,ip)
                        elif i == 10:
                            insert_db.update_memory10_info(memory,socket,socket_status,socket_part_number,socket_type,socket_size,socket_frequency,socket_minimum_voltage,ip)
                        elif i == 11:
                            insert_db.update_memory11_info(memory,socket,socket_status,socket_part_number,socket_type,socket_size,socket_frequency,socket_minimum_voltage,ip)
                        elif i == 12:
                            insert_db.update_memory12_info(memory,socket,socket_status,socket_part_number,socket_type,socket_size,socket_frequency,socket_minimum_voltage,ip)
                    else:
                        if i == 1:
                            insert_db.update_memory2_1_info(memory, socket, socket_status,
                                                          socket_part_number, socket_type, socket_size, socket_frequency,socket_minimum_voltage,ip)
                        elif i == 2:
                            insert_db.update_memory2_2_info(memory, socket, socket_status,
                                                          socket_part_number, socket_type, socket_size, socket_frequency,socket_minimum_voltage,ip)
                        elif i == 3:
                            insert_db.update_memory2_3_info(memory, socket, socket_status,
                                                          socket_part_number, socket_type, socket_size, socket_frequency,socket_minimum_voltage,ip)
                        elif i == 4:
                            insert_db.update_memory2_4_info(memory, socket, socket_status,
                                                          socket_part_number, socket_type, socket_size, socket_frequency,socket_minimum_voltage,ip)
                        elif i == 5:
                            insert_db.update_memory2_5_info(memory, socket, socket_status,
                                                          socket_part_number, socket_type, socket_size, socket_frequency,socket_minimum_voltage,ip)
                        elif i == 6:
                            insert_db.update_memory2_6_info(memory, socket, socket_status,
                                                          socket_part_number, socket_type, socket_size, socket_frequency,socket_minimum_voltage,ip)
                        elif i == 7:
                            insert_db.update_memory2_7_info(memory, socket, socket_status,
                                                          socket_part_number, socket_type, socket_size, socket_frequency,socket_minimum_voltage,ip)
                        elif i == 8:
                            insert_db.update_memory2_8_info(memory, socket, socket_status,
                                                          socket_part_number, socket_type, socket_size, socket_frequency,socket_minimum_voltage,ip)
                        elif i == 9:
                            insert_db.update_memory2_9_info(memory, socket, socket_status,
                                                          socket_part_number, socket_type, socket_size, socket_frequency,socket_minimum_voltage,ip)
                        elif i == 10:
                            insert_db.update_memory2_10_info(memory, socket, socket_status,
                                                           socket_part_number, socket_type, socket_size, socket_frequency,socket_minimum_voltage,ip)
                        elif i == 11:
                            insert_db.update_memory2_11_info(memory, socket, socket_status,
                                                           socket_part_number, socket_type, socket_size, socket_frequency,socket_minimum_voltage,ip)
                        elif i == 12:
                            insert_db.update_memory2_12_info(memory, socket, socket_status,
                                                           socket_part_number, socket_type, socket_size, socket_frequency,socket_minimum_voltage,ip)
        def memory_info_ilo3(memory_all,ip):
            for i in range(0,2):
                for j in range(0,9):
                    try:
                        socket,socket_size,socket_speed = memory_all.next()
                    except StopIteration:
                        socket,socket_size,socket_speed = (None,None,None)
                    print(socket,socket_size,socket_speed)
                    if str(socket)[5] == 1:
                        if j == 1:
                            insert_db.update_memory1_ilo3_info(socket,socket_size,socket_speed,ip)
                        elif j == 2:
                            insert_db.update_memory2_ilo3_info(socket,socket_size,socket_speed,ip)
                        elif j == 3:
                            insert_db.update_memory3_ilo3_info(socket,socket_size,socket_speed,ip)
                        elif j == 4:
                            insert_db.update_memory4_ilo3_info(socket,socket_size,socket_speed,ip)
                        elif j == 5:
                            insert_db.update_memory5_ilo3_info(socket,socket_size,socket_speed,ip)
                        elif j == 6:
                            insert_db.update_memory6_ilo3_info(socket,socket_size,socket_speed,ip)
                        elif j == 7:
                            insert_db.update_memory7_ilo3_info(socket,socket_size,socket_speed,ip)
                        elif j == 8:
                            insert_db.update_memory8_ilo3_info(socket,socket_size,socket_speed,ip)
                        elif j == 9:
                            insert_db.update_memory9_ilo3_info(socket,socket_size,socket_speed,ip)
                    elif str(socket)[5] == 2:
                        if j == 1:
                            insert_db.update_memory2_1_ilo3_info(socket,socket_size,socket_speed,ip)
                        elif j == 2:
                            insert_db.update_memory2_2_ilo3_info(socket,socket_size,socket_speed,ip)
                        elif j == 3:
                            insert_db.update_memory2_3_ilo3_info(socket,socket_size,socket_speed,ip)
                        elif j == 4:
                            insert_db.update_memory2_4_ilo3_info(socket,socket_size,socket_speed,ip)
                        elif j == 5:
                            insert_db.update_memory2_5_ilo3_info(socket,socket_size,socket_speed,ip)
                        elif j == 6:
                            insert_db.update_memory2_6_ilo3_info(socket,socket_size,socket_speed,ip)
                        elif j == 7:
                            insert_db.update_memory2_7_ilo3_info(socket,socket_size,socket_speed,ip)
                        elif j == 8:
                            insert_db.update_memory2_8_ilo3_info(socket,socket_size,socket_speed,ip)
                        elif j == 9:
                            insert_db.update_memory2_9_ilo3_info(socket,socket_size,socket_speed,ip)

        def storage_info(storage_all, ip):
            physical_drive_label_1, physical_drive_status_1, physical_drive_capacity_1, physical_drive_model_1, physical_drive_fw_1, physical_drive_confi_1, physical_drive_sn_1 = (None,None,None,None,None,None,None)
            physical_drive_label_2, physical_drive_status_2, physical_drive_capacity_2, physical_drive_model_2, physical_drive_fw_2, physical_drive_confi_2, physical_drive_sn_2 = (None, None, None, None, None, None, None)
            physical_drive_label_3, physical_drive_status_3, physical_drive_capacity_3, physical_drive_model_3, physical_drive_fw_3, physical_drive_confi_3, physical_drive_sn_3 = (None, None, None, None, None, None, None)
            physical_drive_label_4, physical_drive_status_4, physical_drive_capacity_4, physical_drive_model_4, physical_drive_fw_4, physical_drive_confi_4, physical_drive_sn_4 = (None, None, None, None, None, None, None)
            physical_drive_label_5, physical_drive_status_5, physical_drive_capacity_5, physical_drive_model_5, physical_drive_fw_5, physical_drive_confi_5, physical_drive_sn_5 = (None, None, None, None, None, None, None)
            physical_drive_label_6, physical_drive_status_6, physical_drive_capacity_6, physical_drive_model_6, physical_drive_fw_6, physical_drive_confi_6, physical_drive_sn_6 = (None, None, None, None, None, None, None)
            physical_drive_label_7, physical_drive_status_7, physical_drive_capacity_7, physical_drive_model_7, physical_drive_fw_7, physical_drive_confi_7, physical_drive_sn_7 = (None, None, None, None, None, None, None)
            physical_drive_label_8, physical_drive_status_8, physical_drive_capacity_8, physical_drive_model_8, physical_drive_fw_8, physical_drive_confi_8, physical_drive_sn_8 = (None, None, None, None, None, None, None)
            physical_drive_label_9, physical_drive_status_9, physical_drive_capacity_9, physical_drive_model_9, physical_drive_fw_9, physical_drive_confi_9, physical_drive_sn_9 = (None, None, None, None, None, None, None)
            physical_drive_label_10, physical_drive_status_10, physical_drive_capacity_10, physical_drive_model_10, physical_drive_fw_10, physical_drive_confi_10, physical_drive_sn_10 = (None, None, None, None, None, None, None)

            for i in range(1, 13):

                try:
                    logical_drives_label, logical_drives_status, logical_drives_capacity, logical_drives_fault_tolerance,logical_drive_type = storage_all.next()
                except StopIteration:
                    logical_drives_label, logical_drives_status, logical_drives_capacity, logical_drives_fault_tolerance,logical_drive_type = (None, None, None, None,None)
                for j in range(1, 11):
                    # try:
                    #     physical_drive_label, physical_drive_status,  physical_drive_capacity,physical_drive_model, physical_drive_fw,physical_drive_confi, physical_drive_sn= storage_all.next()
                    # except StopIteration:
                    #     physical_drive_label, physical_drive_status, physical_drive_model, physical_drive_capacity, physical_drive_sn, physical_drive_confi, physical_drive_fw = (None,None,None,None,None,None,None)
                    if j == 1:
                        try:
                            physical_drive_label_1, physical_drive_status_1, physical_drive_capacity_1, physical_drive_model_1, physical_drive_fw_1, physical_drive_confi_1, physical_drive_sn_1 = storage_all.next()
                        except StopIteration:
                            physical_drive_label_1, physical_drive_status_1, physical_drive_capacity_1, physical_drive_model_1, physical_drive_fw_1, physical_drive_confi_1, physical_drive_sn_1 = (
                                None, None, None, None, None, None, None)
                        # insert_db.update_storage_1_info(logical_drives_label, logical_drives_status,logical_drive_capacity, logical_drives_fault_tolerance,physical_drive_label, physical_drive_status,  physical_drive_capacity,physical_drive_model, physical_drive_fw,physical_drive_confi, physical_drive_sn)
                    elif j == 2:
                        try:
                            physical_drive_label_2, physical_drive_status_2, physical_drive_capacity_2, physical_drive_model_2, physical_drive_fw_2, physical_drive_confi_2, physical_drive_sn_2 = storage_all.next()
                        except StopIteration:
                            physical_drive_label_2, physical_drive_status_2, physical_drive_capacity_2, physical_drive_model_2, physical_drive_fw_2, physical_drive_confi_2, physical_drive_sn_2 = (
                                None, None, None, None, None, None, None)
                    elif j == 3:
                        try:
                            physical_drive_label_3, physical_drive_status_3, physical_drive_capacity_3, physical_drive_model_3, physical_drive_fw_3, physical_drive_confi_3, physical_drive_sn_3 = storage_all.next()
                        except StopIteration:
                            physical_drive_label_3, physical_drive_status_3, physical_drive_capacity_3, physical_drive_model_3, physical_drive_fw_3, physical_drive_confi_3, physical_drive_sn_3 = (
                                None, None, None, None, None, None, None)
                    elif j == 4:
                        try:
                            physical_drive_label_4, physical_drive_status_4, physical_drive_capacity_4, physical_drive_model_4, physical_drive_fw_4, physical_drive_confi_4, physical_drive_sn_4 = storage_all.next()
                        except StopIteration:
                            physical_drive_label_4, physical_drive_status_4, physical_drive_capacity_4, physical_drive_model_4, physical_drive_fw_4, physical_drive_confi_4, physical_drive_sn_4 = (
                                None, None, None, None, None, None, None)

                    elif j == 5:
                        try:
                            physical_drive_label_5, physical_drive_status_5, physical_drive_capacity_5, physical_drive_model_5, physical_drive_fw_5, physical_drive_confi_5, physical_drive_sn_5 = storage_all.next()
                        except StopIteration:
                            physical_drive_label_5, physical_drive_status_5, physical_drive_capacity_5, physical_drive_model_5, physical_drive_fw_5, physical_drive_confi_5, physical_drive_sn_5 = (
                                None, None, None, None, None, None, None)

                    elif j == 6:
                        try:
                            physical_drive_label_6, physical_drive_status_6, physical_drive_capacity_6, physical_drive_model_6, physical_drive_fw_6, physical_drive_confi_6, physical_drive_sn_6 = storage_all.next()
                        except StopIteration:
                            physical_drive_label_6, physical_drive_status_6, physical_drive_capacity_6, physical_drive_model_6, physical_drive_fw_6, physical_drive_confi_6, physical_drive_sn_6 = (
                                None, None, None, None, None, None, None)
                    elif j == 7:
                        try:
                            physical_drive_label_7, physical_drive_status_7, physical_drive_capacity_7, physical_drive_model_7, physical_drive_fw_7, physical_drive_confi_7, physical_drive_sn_7 = storage_all.next()
                        except StopIteration:
                            physical_drive_label_7, physical_drive_status_7, physical_drive_capacity_7, physical_drive_model_7, physical_drive_fw_7, physical_drive_confi_7, physical_drive_sn_7 = (
                                None, None, None, None, None, None, None)
                    elif j == 8:
                        try:
                            physical_drive_label_8, physical_drive_status_8, physical_drive_capacity_8, physical_drive_model_8, physical_drive_fw_8, physical_drive_confi_8, physical_drive_sn_8 = storage_all.next()
                        except StopIteration:
                            physical_drive_label_8, physical_drive_status_8, physical_drive_capacity_8, physical_drive_model_8, physical_drive_fw_8, physical_drive_confi_8, physical_drive_sn_8 = (
                                None, None, None, None, None, None, None)
                    elif j == 9:
                        try:
                            physical_drive_label_9, physical_drive_status_9, physical_drive_capacity_9, physical_drive_model_9, physical_drive_fw_9, physical_drive_confi_9, physical_drive_sn_9 = storage_all.next()
                        except StopIteration:
                            physical_drive_label_9, physical_drive_status_9, physical_drive_capacity_9, physical_drive_model_9, physical_drive_fw_9, physical_drive_confi_9, physical_drive_sn_9 = (
                                None, None, None, None, None, None, None)
                    elif j == 10:
                        try:
                            physical_drive_label_10, physical_drive_status_10, physical_drive_capacity_10, physical_drive_model_10, physical_drive_fw_10, physical_drive_confi_10, physical_drive_sn_10 = storage_all.next()
                        except StopIteration:
                            physical_drive_label_10, physical_drive_status_10, physical_drive_capacity_10, physical_drive_model_10, physical_drive_fw_10, physical_drive_confi_10, physical_drive_sn_10 = (
                                None, None, None, None, None, None, None)
                print(logical_drives_label, logical_drives_status, logical_drives_capacity,logical_drives_fault_tolerance,logical_drive_type,
                                                    physical_drive_label_1, physical_drive_status_1,physical_drive_capacity_1, physical_drive_model_1,physical_drive_fw_1, physical_drive_confi_1, physical_drive_sn_1,
                                                    physical_drive_label_2, physical_drive_status_2,physical_drive_capacity_2, physical_drive_model_2,physical_drive_fw_2, physical_drive_confi_2, physical_drive_sn_2,
                                                    physical_drive_label_3, physical_drive_status_3,physical_drive_capacity_3, physical_drive_model_3,physical_drive_fw_3, physical_drive_confi_3, physical_drive_sn_3,
                                                    physical_drive_label_4, physical_drive_status_4,physical_drive_capacity_4, physical_drive_model_4,physical_drive_fw_4, physical_drive_confi_4, physical_drive_sn_4,
                                                    physical_drive_label_5, physical_drive_status_5,physical_drive_capacity_5, physical_drive_model_5,physical_drive_fw_5, physical_drive_confi_5, physical_drive_sn_5,
                                                    physical_drive_label_6, physical_drive_status_6,physical_drive_capacity_6, physical_drive_model_6,physical_drive_fw_6, physical_drive_confi_6, physical_drive_sn_6,
                                                    physical_drive_label_7, physical_drive_status_7,physical_drive_capacity_7, physical_drive_model_7,physical_drive_fw_7, physical_drive_confi_7, physical_drive_sn_7,
                                                    physical_drive_label_8, physical_drive_status_8,physical_drive_capacity_8, physical_drive_model_8,physical_drive_fw_8, physical_drive_confi_8, physical_drive_sn_8,
                                                    physical_drive_label_9, physical_drive_status_9,physical_drive_capacity_9, physical_drive_model_9,physical_drive_fw_9, physical_drive_confi_9, physical_drive_sn_9,
                                                    physical_drive_label_10, physical_drive_status_10,physical_drive_capacity_10, physical_drive_model_10,physical_drive_fw_10, physical_drive_confi_10, physical_drive_sn_10,
                                                    ip)
                if i == 1:
                    print(logical_drives_label, logical_drives_status, logical_drives_capacity,logical_drives_fault_tolerance,
                                                    ip)
                    insert_db.update_storage_1_info(logical_drives_label, logical_drives_status, logical_drives_capacity,logical_drives_fault_tolerance,
                                                    ip)
                elif i == 2:
                    insert_db.update_storage_2_info(logical_drives_label, logical_drives_status, logical_drives_capacity,
                                                    logical_drives_fault_tolerance,logical_drive_type,
                                                    physical_drive_label_1, physical_drive_status_1,
                                                    physical_drive_capacity_1, physical_drive_model_1,
                                                    physical_drive_fw_1, physical_drive_confi_1, physical_drive_sn_1,
                                                    physical_drive_label_2, physical_drive_status_2,
                                                    physical_drive_capacity_2, physical_drive_model_2,
                                                    physical_drive_fw_2, physical_drive_confi_2, physical_drive_sn_2,
                                                    physical_drive_label_3, physical_drive_status_3,
                                                    physical_drive_capacity_3, physical_drive_model_3,
                                                    physical_drive_fw_3, physical_drive_confi_3, physical_drive_sn_3,
                                                    physical_drive_label_4, physical_drive_status_4,
                                                    physical_drive_capacity_4, physical_drive_model_4,
                                                    physical_drive_fw_4, physical_drive_confi_4, physical_drive_sn_4,
                                                    physical_drive_label_5, physical_drive_status_5,
                                                    physical_drive_capacity_5, physical_drive_model_5,
                                                    physical_drive_fw_5, physical_drive_confi_5, physical_drive_sn_5,
                                                    physical_drive_label_6, physical_drive_status_6,
                                                    physical_drive_capacity_6, physical_drive_model_6,
                                                    physical_drive_fw_6, physical_drive_confi_6, physical_drive_sn_6,
                                                    physical_drive_label_7, physical_drive_status_7,
                                                    physical_drive_capacity_7, physical_drive_model_7,
                                                    physical_drive_fw_7, physical_drive_confi_7, physical_drive_sn_7,
                                                    physical_drive_label_8, physical_drive_status_8,
                                                    physical_drive_capacity_8, physical_drive_model_8,
                                                    physical_drive_fw_8, physical_drive_confi_8, physical_drive_sn_8,
                                                    physical_drive_label_9, physical_drive_status_9,
                                                    physical_drive_capacity_9, physical_drive_model_9,
                                                    physical_drive_fw_9, physical_drive_confi_9, physical_drive_sn_9,
                                                    physical_drive_label_10, physical_drive_status_10,
                                                    physical_drive_capacity_10, physical_drive_model_10,
                                                    physical_drive_fw_10, physical_drive_confi_10, physical_drive_sn_10,
                                                    ip)
                elif i == 3:
                    insert_db.update_storage_3_info(logical_drives_label, logical_drives_status, logical_drives_capacity,
                                                    logical_drives_fault_tolerance,logical_drive_type,
                                                    physical_drive_label_1, physical_drive_status_1,
                                                    physical_drive_capacity_1, physical_drive_model_1,
                                                    physical_drive_fw_1, physical_drive_confi_1, physical_drive_sn_1,
                                                    physical_drive_label_2, physical_drive_status_2,
                                                    physical_drive_capacity_2, physical_drive_model_2,
                                                    physical_drive_fw_2, physical_drive_confi_2, physical_drive_sn_2,
                                                    physical_drive_label_3, physical_drive_status_3,
                                                    physical_drive_capacity_3, physical_drive_model_3,
                                                    physical_drive_fw_3, physical_drive_confi_3, physical_drive_sn_3,
                                                    physical_drive_label_4, physical_drive_status_4,
                                                    physical_drive_capacity_4, physical_drive_model_4,
                                                    physical_drive_fw_4, physical_drive_confi_4, physical_drive_sn_4,
                                                    physical_drive_label_5, physical_drive_status_5,
                                                    physical_drive_capacity_5, physical_drive_model_5,
                                                    physical_drive_fw_5, physical_drive_confi_5, physical_drive_sn_5,
                                                    physical_drive_label_6, physical_drive_status_6,
                                                    physical_drive_capacity_6, physical_drive_model_6,
                                                    physical_drive_fw_6, physical_drive_confi_6, physical_drive_sn_6,
                                                    physical_drive_label_7, physical_drive_status_7,
                                                    physical_drive_capacity_7, physical_drive_model_7,
                                                    physical_drive_fw_7, physical_drive_confi_7, physical_drive_sn_7,
                                                    physical_drive_label_8, physical_drive_status_8,
                                                    physical_drive_capacity_8, physical_drive_model_8,
                                                    physical_drive_fw_8, physical_drive_confi_8, physical_drive_sn_8,
                                                    physical_drive_label_9, physical_drive_status_9,
                                                    physical_drive_capacity_9, physical_drive_model_9,
                                                    physical_drive_fw_9, physical_drive_confi_9, physical_drive_sn_9,
                                                    physical_drive_label_10, physical_drive_status_10,
                                                    physical_drive_capacity_10, physical_drive_model_10,
                                                    physical_drive_fw_10, physical_drive_confi_10, physical_drive_sn_10,
                                                    ip)
                elif i == 4:
                    insert_db.update_storage_4_info(logical_drives_label, logical_drives_status, logical_drives_capacity,
                                                    logical_drives_fault_tolerance,logical_drive_type,
                                                    physical_drive_label_1, physical_drive_status_1,
                                                    physical_drive_capacity_1, physical_drive_model_1,
                                                    physical_drive_fw_1, physical_drive_confi_1, physical_drive_sn_1,
                                                    physical_drive_label_2, physical_drive_status_2,
                                                    physical_drive_capacity_2, physical_drive_model_2,
                                                    physical_drive_fw_2, physical_drive_confi_2, physical_drive_sn_2,
                                                    physical_drive_label_3, physical_drive_status_3,
                                                    physical_drive_capacity_3, physical_drive_model_3,
                                                    physical_drive_fw_3, physical_drive_confi_3, physical_drive_sn_3,
                                                    physical_drive_label_4, physical_drive_status_4,
                                                    physical_drive_capacity_4, physical_drive_model_4,
                                                    physical_drive_fw_4, physical_drive_confi_4, physical_drive_sn_4,
                                                    physical_drive_label_5, physical_drive_status_5,
                                                    physical_drive_capacity_5, physical_drive_model_5,
                                                    physical_drive_fw_5, physical_drive_confi_5, physical_drive_sn_5,
                                                    physical_drive_label_6, physical_drive_status_6,
                                                    physical_drive_capacity_6, physical_drive_model_6,
                                                    physical_drive_fw_6, physical_drive_confi_6, physical_drive_sn_6,
                                                    physical_drive_label_7, physical_drive_status_7,
                                                    physical_drive_capacity_7, physical_drive_model_7,
                                                    physical_drive_fw_7, physical_drive_confi_7, physical_drive_sn_7,
                                                    physical_drive_label_8, physical_drive_status_8,
                                                    physical_drive_capacity_8, physical_drive_model_8,
                                                    physical_drive_fw_8, physical_drive_confi_8, physical_drive_sn_8,
                                                    physical_drive_label_9, physical_drive_status_9,
                                                    physical_drive_capacity_9, physical_drive_model_9,
                                                    physical_drive_fw_9, physical_drive_confi_9, physical_drive_sn_9,
                                                    physical_drive_label_10, physical_drive_status_10,
                                                    physical_drive_capacity_10, physical_drive_model_10,
                                                    physical_drive_fw_10, physical_drive_confi_10, physical_drive_sn_10,
                                                    ip)
                elif i == 5:
                    insert_db.update_storage_5_info(logical_drives_label, logical_drives_status, logical_drives_capacity,
                                                    logical_drives_fault_tolerance,logical_drive_type,
                                                    physical_drive_label_1, physical_drive_status_1,
                                                    physical_drive_capacity_1, physical_drive_model_1,
                                                    physical_drive_fw_1, physical_drive_confi_1, physical_drive_sn_1,
                                                    physical_drive_label_2, physical_drive_status_2,
                                                    physical_drive_capacity_2, physical_drive_model_2,
                                                    physical_drive_fw_2, physical_drive_confi_2, physical_drive_sn_2,
                                                    physical_drive_label_3, physical_drive_status_3,
                                                    physical_drive_capacity_3, physical_drive_model_3,
                                                    physical_drive_fw_3, physical_drive_confi_3, physical_drive_sn_3,
                                                    physical_drive_label_4, physical_drive_status_4,
                                                    physical_drive_capacity_4, physical_drive_model_4,
                                                    physical_drive_fw_4, physical_drive_confi_4, physical_drive_sn_4,
                                                    physical_drive_label_5, physical_drive_status_5,
                                                    physical_drive_capacity_5, physical_drive_model_5,
                                                    physical_drive_fw_5, physical_drive_confi_5, physical_drive_sn_5,
                                                    physical_drive_label_6, physical_drive_status_6,
                                                    physical_drive_capacity_6, physical_drive_model_6,
                                                    physical_drive_fw_6, physical_drive_confi_6, physical_drive_sn_6,
                                                    physical_drive_label_7, physical_drive_status_7,
                                                    physical_drive_capacity_7, physical_drive_model_7,
                                                    physical_drive_fw_7, physical_drive_confi_7, physical_drive_sn_7,
                                                    physical_drive_label_8, physical_drive_status_8,
                                                    physical_drive_capacity_8, physical_drive_model_8,
                                                    physical_drive_fw_8, physical_drive_confi_8, physical_drive_sn_8,
                                                    physical_drive_label_9, physical_drive_status_9,
                                                    physical_drive_capacity_9, physical_drive_model_9,
                                                    physical_drive_fw_9, physical_drive_confi_9, physical_drive_sn_9,
                                                    physical_drive_label_10, physical_drive_status_10,
                                                    physical_drive_capacity_10, physical_drive_model_10,
                                                    physical_drive_fw_10, physical_drive_confi_10, physical_drive_sn_10,
                                                    ip)
                elif i == 6:
                    insert_db.update_storage_6_info(logical_drives_label, logical_drives_status, logical_drives_capacity,
                                                    logical_drives_fault_tolerance,logical_drive_type,
                                                    physical_drive_label_1, physical_drive_status_1,
                                                    physical_drive_capacity_1, physical_drive_model_1,
                                                    physical_drive_fw_1, physical_drive_confi_1, physical_drive_sn_1,
                                                    physical_drive_label_2, physical_drive_status_2,
                                                    physical_drive_capacity_2, physical_drive_model_2,
                                                    physical_drive_fw_2, physical_drive_confi_2, physical_drive_sn_2,
                                                    physical_drive_label_3, physical_drive_status_3,
                                                    physical_drive_capacity_3, physical_drive_model_3,
                                                    physical_drive_fw_3, physical_drive_confi_3, physical_drive_sn_3,
                                                    physical_drive_label_4, physical_drive_status_4,
                                                    physical_drive_capacity_4, physical_drive_model_4,
                                                    physical_drive_fw_4, physical_drive_confi_4, physical_drive_sn_4,
                                                    physical_drive_label_5, physical_drive_status_5,
                                                    physical_drive_capacity_5, physical_drive_model_5,
                                                    physical_drive_fw_5, physical_drive_confi_5, physical_drive_sn_5,
                                                    physical_drive_label_6, physical_drive_status_6,
                                                    physical_drive_capacity_6, physical_drive_model_6,
                                                    physical_drive_fw_6, physical_drive_confi_6, physical_drive_sn_6,
                                                    physical_drive_label_7, physical_drive_status_7,
                                                    physical_drive_capacity_7, physical_drive_model_7,
                                                    physical_drive_fw_7, physical_drive_confi_7, physical_drive_sn_7,
                                                    physical_drive_label_8, physical_drive_status_8,
                                                    physical_drive_capacity_8, physical_drive_model_8,
                                                    physical_drive_fw_8, physical_drive_confi_8, physical_drive_sn_8,
                                                    physical_drive_label_9, physical_drive_status_9,
                                                    physical_drive_capacity_9, physical_drive_model_9,
                                                    physical_drive_fw_9, physical_drive_confi_9, physical_drive_sn_9,
                                                    physical_drive_label_10, physical_drive_status_10,
                                                    physical_drive_capacity_10, physical_drive_model_10,
                                                    physical_drive_fw_10, physical_drive_confi_10, physical_drive_sn_10,
                                                    ip)
                elif i == 7:
                    insert_db.update_storage_7_info(logical_drives_label, logical_drives_status, logical_drives_capacity,
                                                    logical_drives_fault_tolerance,logical_drive_type,
                                                    physical_drive_label_1, physical_drive_status_1,
                                                    physical_drive_capacity_1, physical_drive_model_1,
                                                    physical_drive_fw_1, physical_drive_confi_1, physical_drive_sn_1,
                                                    physical_drive_label_2, physical_drive_status_2,
                                                    physical_drive_capacity_2, physical_drive_model_2,
                                                    physical_drive_fw_2, physical_drive_confi_2, physical_drive_sn_2,
                                                    physical_drive_label_3, physical_drive_status_3,
                                                    physical_drive_capacity_3, physical_drive_model_3,
                                                    physical_drive_fw_3, physical_drive_confi_3, physical_drive_sn_3,
                                                    physical_drive_label_4, physical_drive_status_4,
                                                    physical_drive_capacity_4, physical_drive_model_4,
                                                    physical_drive_fw_4, physical_drive_confi_4, physical_drive_sn_4,
                                                    physical_drive_label_5, physical_drive_status_5,
                                                    physical_drive_capacity_5, physical_drive_model_5,
                                                    physical_drive_fw_5, physical_drive_confi_5, physical_drive_sn_5,
                                                    physical_drive_label_6, physical_drive_status_6,
                                                    physical_drive_capacity_6, physical_drive_model_6,
                                                    physical_drive_fw_6, physical_drive_confi_6, physical_drive_sn_6,
                                                    physical_drive_label_7, physical_drive_status_7,
                                                    physical_drive_capacity_7, physical_drive_model_7,
                                                    physical_drive_fw_7, physical_drive_confi_7, physical_drive_sn_7,
                                                    physical_drive_label_8, physical_drive_status_8,
                                                    physical_drive_capacity_8, physical_drive_model_8,
                                                    physical_drive_fw_8, physical_drive_confi_8, physical_drive_sn_8,
                                                    physical_drive_label_9, physical_drive_status_9,
                                                    physical_drive_capacity_9, physical_drive_model_9,
                                                    physical_drive_fw_9, physical_drive_confi_9, physical_drive_sn_9,
                                                    physical_drive_label_10, physical_drive_status_10,
                                                    physical_drive_capacity_10, physical_drive_model_10,
                                                    physical_drive_fw_10, physical_drive_confi_10, physical_drive_sn_10,
                                                    ip)
                elif i == 8:
                    insert_db.update_storage_8_info(logical_drives_label, logical_drives_status, logical_drives_capacity,
                                                    logical_drives_fault_tolerance,logical_drive_type,
                                                    physical_drive_label_1, physical_drive_status_1,
                                                    physical_drive_capacity_1, physical_drive_model_1,
                                                    physical_drive_fw_1, physical_drive_confi_1, physical_drive_sn_1,
                                                    physical_drive_label_2, physical_drive_status_2,
                                                    physical_drive_capacity_2, physical_drive_model_2,
                                                    physical_drive_fw_2, physical_drive_confi_2, physical_drive_sn_2,
                                                    physical_drive_label_3, physical_drive_status_3,
                                                    physical_drive_capacity_3, physical_drive_model_3,
                                                    physical_drive_fw_3, physical_drive_confi_3, physical_drive_sn_3,
                                                    physical_drive_label_4, physical_drive_status_4,
                                                    physical_drive_capacity_4, physical_drive_model_4,
                                                    physical_drive_fw_4, physical_drive_confi_4, physical_drive_sn_4,
                                                    physical_drive_label_5, physical_drive_status_5,
                                                    physical_drive_capacity_5, physical_drive_model_5,
                                                    physical_drive_fw_5, physical_drive_confi_5, physical_drive_sn_5,
                                                    physical_drive_label_6, physical_drive_status_6,
                                                    physical_drive_capacity_6, physical_drive_model_6,
                                                    physical_drive_fw_6, physical_drive_confi_6, physical_drive_sn_6,
                                                    physical_drive_label_7, physical_drive_status_7,
                                                    physical_drive_capacity_7, physical_drive_model_7,
                                                    physical_drive_fw_7, physical_drive_confi_7, physical_drive_sn_7,
                                                    physical_drive_label_8, physical_drive_status_8,
                                                    physical_drive_capacity_8, physical_drive_model_8,
                                                    physical_drive_fw_8, physical_drive_confi_8, physical_drive_sn_8,
                                                    physical_drive_label_9, physical_drive_status_9,
                                                    physical_drive_capacity_9, physical_drive_model_9,
                                                    physical_drive_fw_9, physical_drive_confi_9, physical_drive_sn_9,
                                                    physical_drive_label_10, physical_drive_status_10,
                                                    physical_drive_capacity_10, physical_drive_model_10,
                                                    physical_drive_fw_10, physical_drive_confi_10, physical_drive_sn_10,
                                                    ip)

                elif i == 9:
                    insert_db.update_storage_1_info(logical_drives_label, logical_drives_status, logical_drives_capacity,
                                                    logical_drives_fault_tolerance,logical_drive_type,
                                                    physical_drive_label_1, physical_drive_status_1,
                                                    physical_drive_capacity_1, physical_drive_model_1,
                                                    physical_drive_fw_1, physical_drive_confi_1, physical_drive_sn_1,
                                                    physical_drive_label_2, physical_drive_status_2,
                                                    physical_drive_capacity_2, physical_drive_model_2,
                                                    physical_drive_fw_2, physical_drive_confi_2, physical_drive_sn_2,
                                                    physical_drive_label_3, physical_drive_status_3,
                                                    physical_drive_capacity_3, physical_drive_model_3,
                                                    physical_drive_fw_3, physical_drive_confi_3, physical_drive_sn_3,
                                                    physical_drive_label_4, physical_drive_status_4,
                                                    physical_drive_capacity_4, physical_drive_model_4,
                                                    physical_drive_fw_4, physical_drive_confi_4, physical_drive_sn_4,
                                                    physical_drive_label_5, physical_drive_status_5,
                                                    physical_drive_capacity_5, physical_drive_model_5,
                                                    physical_drive_fw_5, physical_drive_confi_5, physical_drive_sn_5,
                                                    physical_drive_label_6, physical_drive_status_6,
                                                    physical_drive_capacity_6, physical_drive_model_6,
                                                    physical_drive_fw_6, physical_drive_confi_6, physical_drive_sn_6,
                                                    physical_drive_label_7, physical_drive_status_7,
                                                    physical_drive_capacity_7, physical_drive_model_7,
                                                    physical_drive_fw_7, physical_drive_confi_7, physical_drive_sn_7,
                                                    physical_drive_label_8, physical_drive_status_8,
                                                    physical_drive_capacity_8, physical_drive_model_8,
                                                    physical_drive_fw_8, physical_drive_confi_8, physical_drive_sn_8,
                                                    physical_drive_label_9, physical_drive_status_9,
                                                    physical_drive_capacity_9, physical_drive_model_9,
                                                    physical_drive_fw_9, physical_drive_confi_9, physical_drive_sn_9,
                                                    physical_drive_label_10, physical_drive_status_10,
                                                    physical_drive_capacity_10, physical_drive_model_10,
                                                    physical_drive_fw_10, physical_drive_confi_10, physical_drive_sn_10,
                                                    ip)
                elif i == 10:
                    insert_db.update_storage_10_info(logical_drives_label, logical_drives_status, logical_drives_capacity,
                                                    logical_drives_fault_tolerance,logical_drive_type,
                                                    physical_drive_label_1, physical_drive_status_1,
                                                    physical_drive_capacity_1, physical_drive_model_1,
                                                    physical_drive_fw_1, physical_drive_confi_1, physical_drive_sn_1,
                                                    physical_drive_label_2, physical_drive_status_2,
                                                    physical_drive_capacity_2, physical_drive_model_2,
                                                    physical_drive_fw_2, physical_drive_confi_2, physical_drive_sn_2,
                                                    physical_drive_label_3, physical_drive_status_3,
                                                    physical_drive_capacity_3, physical_drive_model_3,
                                                    physical_drive_fw_3, physical_drive_confi_3, physical_drive_sn_3,
                                                    physical_drive_label_4, physical_drive_status_4,
                                                    physical_drive_capacity_4, physical_drive_model_4,
                                                    physical_drive_fw_4, physical_drive_confi_4, physical_drive_sn_4,
                                                    physical_drive_label_5, physical_drive_status_5,
                                                    physical_drive_capacity_5, physical_drive_model_5,
                                                    physical_drive_fw_5, physical_drive_confi_5, physical_drive_sn_5,
                                                    physical_drive_label_6, physical_drive_status_6,
                                                    physical_drive_capacity_6, physical_drive_model_6,
                                                    physical_drive_fw_6, physical_drive_confi_6, physical_drive_sn_6,
                                                    physical_drive_label_7, physical_drive_status_7,
                                                    physical_drive_capacity_7, physical_drive_model_7,
                                                    physical_drive_fw_7, physical_drive_confi_7, physical_drive_sn_7,
                                                    physical_drive_label_8, physical_drive_status_8,
                                                    physical_drive_capacity_8, physical_drive_model_8,
                                                    physical_drive_fw_8, physical_drive_confi_8, physical_drive_sn_8,
                                                    physical_drive_label_9, physical_drive_status_9,
                                                    physical_drive_capacity_9, physical_drive_model_9,
                                                    physical_drive_fw_9, physical_drive_confi_9, physical_drive_sn_9,
                                                    physical_drive_label_10, physical_drive_status_10,
                                                    physical_drive_capacity_10, physical_drive_model_10,
                                                    physical_drive_fw_10, physical_drive_confi_10, physical_drive_sn_10,
                                                    ip)
                elif i == 11:
                    insert_db.update_storage_11_info(logical_drives_label, logical_drives_status, logical_drives_capacity,
                                                    logical_drives_fault_tolerance,logical_drive_type,
                                                    physical_drive_label_1, physical_drive_status_1,
                                                    physical_drive_capacity_1, physical_drive_model_1,
                                                    physical_drive_fw_1, physical_drive_confi_1, physical_drive_sn_1,
                                                    physical_drive_label_2, physical_drive_status_2,
                                                    physical_drive_capacity_2, physical_drive_model_2,
                                                    physical_drive_fw_2, physical_drive_confi_2, physical_drive_sn_2,
                                                    physical_drive_label_3, physical_drive_status_3,
                                                    physical_drive_capacity_3, physical_drive_model_3,
                                                    physical_drive_fw_3, physical_drive_confi_3, physical_drive_sn_3,
                                                    physical_drive_label_4, physical_drive_status_4,
                                                    physical_drive_capacity_4, physical_drive_model_4,
                                                    physical_drive_fw_4, physical_drive_confi_4, physical_drive_sn_4,
                                                    physical_drive_label_5, physical_drive_status_5,
                                                    physical_drive_capacity_5, physical_drive_model_5,
                                                    physical_drive_fw_5, physical_drive_confi_5, physical_drive_sn_5,
                                                    physical_drive_label_6, physical_drive_status_6,
                                                    physical_drive_capacity_6, physical_drive_model_6,
                                                    physical_drive_fw_6, physical_drive_confi_6, physical_drive_sn_6,
                                                    physical_drive_label_7, physical_drive_status_7,
                                                    physical_drive_capacity_7, physical_drive_model_7,
                                                    physical_drive_fw_7, physical_drive_confi_7, physical_drive_sn_7,
                                                    physical_drive_label_8, physical_drive_status_8,
                                                    physical_drive_capacity_8, physical_drive_model_8,
                                                    physical_drive_fw_8, physical_drive_confi_8, physical_drive_sn_8,
                                                    physical_drive_label_9, physical_drive_status_9,
                                                    physical_drive_capacity_9, physical_drive_model_9,
                                                    physical_drive_fw_9, physical_drive_confi_9, physical_drive_sn_9,
                                                    physical_drive_label_10, physical_drive_status_10,
                                                    physical_drive_capacity_10, physical_drive_model_10,
                                                    physical_drive_fw_10, physical_drive_confi_10, physical_drive_sn_10,
                                                    ip)
                elif i == 12:
                    insert_db.update_storage_12_info(logical_drives_label, logical_drives_status, logical_drives_capacity,
                                                    logical_drives_fault_tolerance,logical_drive_type,
                                                    physical_drive_label_1, physical_drive_status_1,
                                                    physical_drive_capacity_1, physical_drive_model_1,
                                                    physical_drive_fw_1, physical_drive_confi_1, physical_drive_sn_1,
                                                    physical_drive_label_2, physical_drive_status_2,
                                                    physical_drive_capacity_2, physical_drive_model_2,
                                                    physical_drive_fw_2, physical_drive_confi_2, physical_drive_sn_2,
                                                    physical_drive_label_3, physical_drive_status_3,
                                                    physical_drive_capacity_3, physical_drive_model_3,
                                                    physical_drive_fw_3, physical_drive_confi_3, physical_drive_sn_3,
                                                    physical_drive_label_4, physical_drive_status_4,
                                                    physical_drive_capacity_4, physical_drive_model_4,
                                                    physical_drive_fw_4, physical_drive_confi_4, physical_drive_sn_4,
                                                    physical_drive_label_5, physical_drive_status_5,
                                                    physical_drive_capacity_5, physical_drive_model_5,
                                                    physical_drive_fw_5, physical_drive_confi_5, physical_drive_sn_5,
                                                    physical_drive_label_6, physical_drive_status_6,
                                                    physical_drive_capacity_6, physical_drive_model_6,
                                                    physical_drive_fw_6, physical_drive_confi_6, physical_drive_sn_6,
                                                    physical_drive_label_7, physical_drive_status_7,
                                                    physical_drive_capacity_7, physical_drive_model_7,
                                                    physical_drive_fw_7, physical_drive_confi_7, physical_drive_sn_7,
                                                    physical_drive_label_8, physical_drive_status_8,
                                                    physical_drive_capacity_8, physical_drive_model_8,
                                                    physical_drive_fw_8, physical_drive_confi_8, physical_drive_sn_8,
                                                    physical_drive_label_9, physical_drive_status_9,
                                                    physical_drive_capacity_9, physical_drive_model_9,
                                                    physical_drive_fw_9, physical_drive_confi_9, physical_drive_sn_9,
                                                    physical_drive_label_10, physical_drive_status_10,
                                                    physical_drive_capacity_10, physical_drive_model_10,
                                                    physical_drive_fw_10, physical_drive_confi_10, physical_drive_sn_10,
                                                    ip)

        if ilo_model != 'iLO3':
            #memory_all = analyse_json.get_memory_info(health_info)
            #memory_info(memory_all,ip)
            storage_all = analyse_json.get_storage_info(health_info)
            storage_info(storage_all,ip)

        # else:
        #     memory_all = analyse_json.get_memory_info_ilo3(health_info)
        #     memory_info_ilo3(memory_all,ip)
        





            


if __name__ == '__main__':

    num_threads = 8
    threads = []
    sql = "select IP_ILO from ILO_INFO"
    g = db.connection_database(sql)
    start = time.clock()
    try:
        while True:
            ip = g.next().lstrip("'").rstrip("'")
            q.put(ip)
    except StopIteration:
        print("ip加载完成")
    finally:
        pass
    test()
    # for i in range(num_threads):
    #     thread = threading.Thread(target=test(), args=(i,))
    #     thread.start()
#        threads.append(thread)
 #   for thread in threads: thread.join()
#    end = time.clock()
 #   print(end-start)
