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

def test(id,ip):
    #多线程测试
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
    storage_all = analyse_json.get_storage_info(health_info)


#        insert_db.update_fw_info(product_name,server_name,ilo_model,fw_version,fw_data,ip)
#        insert_db.update_server_general_info(bios_hardware,fans,temperature,power_supplies,battery,processor,memory,network,storage,ip)
        #以上是获取硬件大体信息
        #以下是获取硬件详细信息
    def fan_info(ip,fan_all):

        global fan_label, fan_status, fan_location, fan_speed
        number = 0
        number = fan_all.next()
        for i in range(1, number+1):
            try:
                fan_status, fan_speed, fan_location, fan_label= fan_all.next()
            except StopIteration:
                fan_status, fan_speed, fan_location, fan_label = ('Not Installed','0','None','None')
            finally:
                # print(fan_status, fan_speed, fan_location)  #
                insert_db.insert_fan_info(fan_status,fan_speed,fan_location,fan_label,ip,id)
            # insert_db.update_server_general_info(fan_status,fan_speed,fan_location)
    #fan_info(ip,fan_all)

    def network_info(ip,network_all):
        global network_name, network_status, network_ipaddr, network_macaddr, network_port
        number = network_all.next()
        for i in range(1, number + 1):
           try:
               network_name, network_status,network_ipaddr, network_macaddr, network_port = network_all.next()
           except StopIteration:
               network_name, network_status,network_ipaddr, network_macaddr, network_port = (None,None,None,None,None)
           finally:
               print(network_name,network_status,network_ipaddr,network_macaddr,network_port)
               insert_db.insert_network_info(network_name, network_status, network_ipaddr, network_macaddr,
                                             network_port, ip,id)



    def memory_info(memory_all,ip):
        global memory, socket, socket_status, socket_part_number, socket_type, socket_size, socket_minimum_voltage, socket_frequency
        number1 = memory_all.next()
        for j in range(1,number1 + 1):
            number2 = memory_all.next()
            for i in range(1,number2 + 1):
                try:
                    memory,socket,socket_status,socket_part_number,socket_type,socket_size,socket_frequency,socket_minimum_voltage = memory_all.next()
                except StopIteration:
                    memory, socket, socket_status, socket_part_number, socket_type, socket_size, socket_frequency, socket_minimum_voltage = (None,None,None,None,None,None,None,None)
                finally:
                    print(memory,socket,socket_status,socket_part_number,socket_type,socket_size,socket_frequency,socket_minimum_voltage,ip,id)
                    insert_db.insert_memory_info(memory,socket,socket_status,socket_part_number,socket_type,socket_size,socket_frequency,socket_minimum_voltage,ip,id)

    def memory_info_ilo3(memory_all,ip):
        socket ,socket_size, socket_speed= None,None,None
        number = memory_all.next()
        for j in range(1,number + 1):
            try:
                socket,socket_size,socket_speed = memory_all.next()
            except StopIteration:
                socket,socket_size,socket_speed = (None,None,None)
            finally:
                print(socket,socket_size,socket_speed)
                insert_db.insert_memory_ilo3_info(socket,socket_size,socket_speed,ip,id)


    def storage_info(storage_all, ip):
        # number = 0
        number1 = 0
        physical_drive_label, physical_drive_status, physical_drive_capacity, physical_drive_model, physical_drive_fw, physical_drive_confi, physical_drive_sn = (None,None,None,None,None,None,None)
        number = storage_all.next()
        for i in range(1, number+1):
            try:
                logical_drives_label, logical_drives_status, logical_drives_capacity, logical_drives_fault_tolerance,logical_drive_type,number1 = storage_all.next()
            except StopIteration:
                logical_drives_label, logical_drives_status, logical_drives_capacity, logical_drives_fault_tolerance,logical_drive_type = (None, None, None, None,None)
            for j in range(1, number1 + 1):
                # try:
                #     physical_drive_label, physical_drive_status,  physical_drive_capacity,physical_drive_model, physical_drive_fw,physical_drive_confi, physical_drive_sn= storage_all.next()
                # except StopIteration:
                #     physical_drive_label, physical_drive_status, physical_drive_model, physical_drive_capacity, physical_drive_sn, physical_drive_confi, physical_drive_fw = (None,None,None,None,None,None,None)
                try:
                    physical_drive_label, physical_drive_status, physical_drive_capacity, physical_drive_model, physical_drive_fw_, physical_drive_confi, physical_drive_sn = storage_all.next()
                except StopIteration:
                    physical_drive_label, physical_drive_status, physical_drive_capacity, physical_drive_model, physical_drive_fw , physical_drive_confi, physical_drive_sn = (None, None, None, None, None, None, None)
                finally:
                    insert_db.insert_storage_info(logical_drives_label,logical_drives_status,logical_drives_capacity,logical_drives_fault_tolerance,logical_drive_type,physical_drive_label,physical_drive_status,physical_drive_capacity,physical_drive_model,physical_drive_sn,physical_drive_confi,physical_drive_fw,ip,id)
    def storage_ilo3_info(storage_all,ip):
        physical_drive_label,physical_drive_status,physical_drive_sn = (None,None,None)
        number = 0
        number = storage_all.next()
        for i in range(1,number + 1):
            try:
                physical_drive_label, physical_drive_status, physical_drive_sn = storage_all.next()
            except StopIteration:
                physical_drive_label, physical_drive_status, physical_drive_sn = (None,None,None)
            finally:
                insert_db.insert_storage_ilo3_info(physical_drive_label,physical_drive_status,physical_drive_sn,ip,id)



    def power_info(power_all):
        power_supplies_label, power_supplies_status, power_supplies_present,\
        power_supplies_model, power_supplies_spare, power_supplies_fw,power_supplies_capacity,\
        power_supplies_sn, power_supplies_hotplug, power_supplies_pds = (None,None,None,None,None,None,None,None,None,None)
        number = 0
        for i in (1, number + 1):
            if i == 1:
                try:
                    power_supplies_label,power_supplies_status,power_supplies_present,power_supplies_model,\
                    power_supplies_spare,power_supplies_fw,power_supplies_capacity,power_supplies_sn = power_all.next()







    def power_ilo3_info():


    if ilo_model != 'iLO3':
        memory_all = analyse_json.get_memory_info(health_info)
        memory_info(memory_all,ip)
        storage_all = analyse_json.get_storage_info(health_info)
        storage_info(storage_all,ip)
        #net_all = ilo.xmldata()
        # network_all = analyse_json.get_network_info(net_all)
        # network_info(ip,network_all)
        # power_all = analyse_json.get_power_info(health_info)
        # power_info(storage_all,ip)


    else:
       memory_all = analyse_json.get_memory_info_ilo3(health_info)
       memory_info_ilo3(memory_all,ip)
       storage_all = analyse_json.get_storage_info_ilo3(health_info)
       storage_ilo3_info(storage_all,ip)
       #power_all = analyse_json.get_power_info_ilo3(health_info)
       #power_info(storage_all,ip)





            


if __name__ == '__main__':

    sql = "select HARDWARE_ID,IP_ILO from ILO_INFO"
    g = db.connection_database(sql)
    start = time.clock()
    try:
        while True:
            id,ip = g.next()
            print(ip)
            test(id,ip)
    except StopIteration:
        print("ip加载完成")
    finally:
        pass

    # for i in range(num_threads):
    #     thread = threading.Thread(target=test(), args=(i,))
    #     thread.start()
#        threads.append(thread)
 #   for thread in threads: thread.join()
#    end = time.clock()
 #   print(end-start)
