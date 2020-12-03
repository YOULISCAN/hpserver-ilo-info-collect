# -*- coding: utf-8 -*-
import os
import sys
sys.path.append('/opt')
import cx_Oracle
import hpilo
import database.login_database as db
import analyse_json
import database.insert_database as insert_db
import subprocess
import threading
import Queue
import time
import ssl
import re
import base64
lock = threading.Lock()

#time_info = (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
time_info = time.localtime()
q = Queue.Queue()
def input_account(login,password,time_info,ip):
    param = {'LOGIN_USERS': login, 'LOGIN_PWD': password,  'ILO_IP': ip}
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    with connection.cursor() as cursor:
        cursor.execute('UPDATE ILO_USERS SET LOGIN_USERS=:LOGIN_USERS,LOGIN_PWD=:LOGIN_PWD,EDITE_DATE=sysdate '
                       'where ILO_IP=:ILO_IP', param)
    connection.commit()
    connection.close()
def test(id, ip, new):
    # ilo = hpilo.Ilo(ip, login='MonitorTools', password='ping.p.shen@foxconn.com')
    # ilo.get_product_name()
    # login = base64.b64encode(b"MonitorTools")
    # password = base64.b64encode(b"ping.p.shen@foxconn.com")
    # input_account(login, password, time_info, ip)
    #多线程测试
    try:
       # ilo = hpilo.Ilo(ip, login='admin', password='Idpbg123.')
        ilo = hpilo.Ilo(ip, login='MonitorTools', password='ping.p.shen@foxconn.com')
        #admin
        ilo.get_product_name()
        login = base64.b64encode(b"MonitorTools")
        password = base64.b64encode(b"ping.p.shen@foxconn.com")
        input_account(login,password,time_info,ip)

    except :
        try:
            ilo = hpilo.Ilo(ip, login='admin', password='Idpbg123.')
            ilo.get_product_name()
            login = base64.b64encode(b"admin")
            password = base64.b64encode(b"Idpbg123.")
            input_account(login, password, time_info, ip)
        except :
            try:
                ilo = hpilo.Ilo(ip,login='admin',password='dpbg123.')
                ilo.get_product_name()
                login = base64.b64encode(b"admin")
                password = base64.b64encode(b"dpbg123.")
                input_account(login, password, time_info, ip)
            except :
                return

    server_name = ilo.get_server_name()  #获取主机名
    product_name = ilo.get_product_name()  # 获取产品型号
    fw_version_info = ilo.get_fw_version()
    health_info = ilo.get_embedded_health()
    serial_number = ilo.get_host_data()[1]['Serial Number']
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
    insert_db.update_check_NEW(ip)


    insert_db.update_fw_info(product_name,server_name,ilo_model,fw_version,fw_data,serial_number,ip)
    insert_db.update_server_general_info(bios_hardware,fans,temperature,power_supplies,battery,processor,memory,network,storage,ip,time_info)

        #以上是获取硬件大体信息
        #以下是获取硬件详细信息
    def fan_info(ip,fan_all,new,time_info):

        global fan_label, fan_status, fan_location, fan_speed,flag_fan
        number = 0
        number = fan_all.next()
        for i in range(1, number+1):
            try:
                fan_status, fan_speed, fan_location, fan_label= fan_all.next()
            except StopIteration:
                fan_status, fan_speed, fan_location, fan_label = ('Not Installed','0','None','None')
            finally:
                # print(fan_status, fan_speed, fan_location)  #
                if new == 1:
                    insert_db.insert_fan_info(fan_status,fan_speed,fan_location,fan_label,ip,id,i,time_info)
                else:
                    insert_db.update_fan_info(fan_status,fan_speed,fan_location,fan_label,ip,id,i,time_info)
            # insert_db.update_server_general_info(fan_status,fan_speed,fan_location)


    def network_info(ip,network_all,new,time_info):
        global network_name, network_status, network_ipaddr, network_macaddr, network_port
        number = network_all.next()
        for i in range(1, number + 1):
           try:
               network_name, network_status,network_ipaddr, network_macaddr, network_port = network_all.next()
           except StopIteration:
               network_name, network_status,network_ipaddr, network_macaddr, network_port = (None,None,None,None,None)
           finally:
               print(network_name,network_status,network_ipaddr,network_macaddr,network_port)
               if new == 1:
                 insert_db.insert_network_info(network_name, network_status, network_ipaddr, network_macaddr,
                                             network_port, ip,id,i,time_info)
               else:
                   insert_db.update_network_info(network_name, network_status, network_ipaddr, network_macaddr,
                                             network_port, ip,id,i,time_info)



    def memory_info(memory_all,ip,new,time_info):
        memory, socket, socket_status, socket_part_number, socket_type, socket_size, socket_minimum_voltage, socket_frequency =(None,None,None,None,None,None,None,None)
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
                    if new == 1:
                        insert_db.insert_memory_info(memory,socket,socket_status,socket_part_number,socket_type,socket_size,socket_frequency,socket_minimum_voltage,ip,id,i,time_info)
                    else:
                        insert_db.update_memory_info(memory,socket,socket_status,socket_part_number,socket_type,socket_size,socket_frequency,socket_minimum_voltage,ip,id,i,time_info)

    def memory_info_ilo3(memory_all,ip,new,time_info):
        socket ,socket_size, socket_speed= None,None,None
        number = memory_all.next()
        for j in range(1,number + 1):
            try:
                socket,socket_size,socket_speed = memory_all.next()
            except StopIteration:
                socket,socket_size,socket_speed = (None,None,None)
            finally:
                print(socket,socket_size,socket_speed)
                if new == 1:
                    insert_db.insert_memory_ilo3_info(socket,socket_size,socket_speed,ip,id,j,time_info)
                else:
                    insert_db.update_memory_ilo3_info(socket,socket_size,socket_speed,ip,id,j,time_info)


    def storage_info(storage_all, ip,new,time_info):
        # number = 0
        number1 = 0
        model,serial_number,status = (None,None,None)
        model,serial_number,status = storage_all.next()
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
                    print(logical_drives_label,logical_drives_status,logical_drives_capacity,logical_drives_fault_tolerance,logical_drive_type,physical_drive_label,physical_drive_status,physical_drive_capacity,physical_drive_model,physical_drive_sn,physical_drive_confi,physical_drive_fw)
                    if new == 1:
                        insert_db.insert_storage_info(model,serial_number,status,logical_drives_label,logical_drives_status,logical_drives_capacity,logical_drives_fault_tolerance,logical_drive_type,physical_drive_label,physical_drive_status,physical_drive_capacity,physical_drive_model,physical_drive_sn,physical_drive_confi,physical_drive_fw,ip,id,j,time_info)
                    else:
                        insert_db.update_storage_info(model,serial_number,status,logical_drives_label,logical_drives_status,logical_drives_capacity,logical_drives_fault_tolerance,logical_drive_type,physical_drive_label,physical_drive_status,physical_drive_capacity,physical_drive_model,physical_drive_sn,physical_drive_confi,physical_drive_fw,ip,id,j,time_info)
                        
                        
    def storage_ilo3_info(storage_all,ip,new,time_info):
        physical_drive_label,physical_drive_status,physical_drive_sn = (None,None,None)
        number = 0
        number = storage_all.next()
        for i in range(1,number + 1):
            try:
                physical_drive_label, physical_drive_status, physical_drive_sn = storage_all.next()
            except StopIteration:
                physical_drive_label, physical_drive_status, physical_drive_sn = (None,None,None)
            finally:
                if new == 1:
                    insert_db.insert_storage_ilo3_info(physical_drive_label,physical_drive_status,physical_drive_sn,ip,id,i,time_info)
                else:
                    insert_db.update_storage_ilo3_info(physical_drive_label,physical_drive_status,physical_drive_sn,ip,id,i,time_info)



    def power_info(power_all,ip,new,time_info):
        power_supplies_label, power_supplies_status, power_supplies_present,\
        power_supplies_model, power_supplies_spare, power_supplies_fw,power_supplies_capacity,\
        power_supplies_sn, power_supplies_hotplug, power_supplies_pds = (None,None,None,None,None,None,None,None,None,None)
        number = 0
        number = power_all.next()
        for i in range(1, number + 1):
            try:
                power_supplies_label,power_supplies_status,power_supplies_sn,power_supplies_capacity,power_supplies_hotplug,power_supplies_model,\
                power_supplies_present,power_supplies_spare,power_supplies_fw,power_supplies_pds = power_all.next()
            except StopIteration:
                power_supplies_label, power_supplies_status, power_supplies_sn, power_supplies_capacity, power_supplies_hotplug, power_supplies_model, \
                power_supplies_present, power_supplies_spare, power_supplies_fw, power_supplies_pds = (None,None,None,None,None,None,None,None,None,None)
            finally:
                if new == 1:
                    insert_db.insert_power_info(power_supplies_label,power_supplies_status,power_supplies_sn,power_supplies_capacity,power_supplies_hotplug,power_supplies_model,
                power_supplies_present,power_supplies_spare,power_supplies_fw,power_supplies_pds,ip,id,i,time_info)
                else:
                    insert_db.update_power_info(power_supplies_label,power_supplies_status,power_supplies_sn,power_supplies_capacity,power_supplies_hotplug,power_supplies_model,
                power_supplies_present,power_supplies_spare,power_supplies_fw,power_supplies_pds,ip,id,i,time_info)


    def power_ilo3_info(power_all,ip,new,time_info):
        power_supplies_label,power_supplies_status = (None,None)
        number = 0
        number = power_all.next()
        for i in range(1, number + 1):
            try:
                power_supplies_label,power_supplies_status = power_all.next()
            except StopIteration:
                power_supplies_label,power_supplies_status = (None,None)
            finally:
                if new == 1:
                    insert_db.insert_power_ilo3_info(power_supplies_label,power_supplies_status,ip,id,i,time_info)
                else:
                    insert_db.update_power_ilo3_info(power_supplies_label,power_supplies_status,ip,id,i,time_info)

    def power_summary_info(power_all,ip,ilo_model):
        high_efficiency_mode,power_redundancy_status,power_management_control_fw,present_power_reading,power_system_redundancy = (None,None,None,None,None)

        if ilo_model == 'iLO3':
            try:
                high_efficiency_mode,power_management_control_fw,present_power_reading = power_all.next()
            except StopIteration:
                high_efficiency_mode, power_management_control_fw, present_power_reading = (None,None,None)
            finally:
                insert_db.update_power_sum_info(high_efficiency_mode, power_redundancy_status, power_management_control_fw, present_power_reading, power_system_redundancy)
        else:
            try:
                high_efficiency_mode,  power_management_control_fw, power_redundancy_status,present_power_reading, power_system_redundancy = power_all.next()
            except StopIteration:
                high_efficiency_mode, power_redundancy_status, power_management_control_fw, present_power_reading, power_system_redundancy = (None,None,None,None,None)
            finally:
                insert_db.update_power_sum_info(high_efficiency_mode, power_redundancy_status, power_management_control_fw, present_power_reading, power_system_redundancy,ip,id)

    def processors_info(processor_all,ip,ilo_model,new,time_info):
        processor_name,processor_status,processor_label, processor_exe_tech, processor_inter_l1_cache, processor_inter_l2_cache, processor_inter_l3_cache, processor_memory_tech, processor_speed = (None,None,None,None,None,None,None,None,None)
        global flag_processor
        number = processor_all.next()
        for i in range(1, number + 1):
            if ilo_model == 'iLO3':
                try:
                    processor_label, processor_exe_tech, processor_inter_l1_cache, processor_inter_l2_cache, processor_inter_l3_cache, processor_memory_tech, processor_speed = processor_all.next()
                except StopIteration:
                    processor_label, processor_exe_tech, processor_inter_l1_cache, processor_inter_l2_cache, processor_inter_l3_cache, processor_memory_tech, processor_speed = (None,None,None,None,None,None,None)
                finally:
                    if new == 1:
                        insert_db.insert_processor_info(processor_name,processor_status,processor_label, processor_exe_tech, processor_inter_l1_cache, processor_inter_l2_cache, processor_inter_l3_cache, processor_memory_tech, processor_speed,ip,id,i,time_info)
                    else:
                        insert_db.update_processor_info(processor_name,processor_status,processor_label, processor_exe_tech, processor_inter_l1_cache, processor_inter_l2_cache, processor_inter_l3_cache, processor_memory_tech, processor_speed,ip,id,i,time_info)

            else:
                processor_name, processor_status, processor_label, processor_exe_tech, processor_inter_l1_cache, processor_inter_l2_cache, processor_inter_l3_cache, processor_memory_tech, processor_speed = processor_all.next()
                if new == 1:
                    insert_db.insert_processor_info(processor_name,processor_status,processor_label, processor_exe_tech, processor_inter_l1_cache, processor_inter_l2_cache, processor_inter_l3_cache, processor_memory_tech, processor_speed,ip,id,i,time_info)
                else:
                    insert_db.update_processor_info(processor_name,processor_status,processor_label, processor_exe_tech, processor_inter_l1_cache, processor_inter_l2_cache, processor_inter_l3_cache, processor_memory_tech, processor_speed,ip,id,i,time_info)

    fan_info(ip, fan_all,new,time_info)
    if ilo_model != 'iLO3':
        memory_all = analyse_json.get_memory_info(health_info)
        memory_info(memory_all,ip,new,time_info)
        storage_all = analyse_json.get_storage_info(health_info)
        storage_info(storage_all,ip,new,time_info)
        net_all = ilo.xmldata()
        network_all = analyse_json.get_network_info(net_all)
        network_info(ip,network_all,new,time_info)
        power_all = analyse_json.get_power_info(health_info)
        power_info(power_all,ip,new,time_info)
        power_sum_all = analyse_json.get_power_summary_info(health_info)
        power_summary_info(power_sum_all,ip,ilo_model)
        processor_all = analyse_json.get_processors_info(health_info)
        processors_info(processor_all,ip,ilo_model,new,time_info)

    else:
       memory_all = analyse_json.get_memory_info_ilo3(health_info)
       memory_info_ilo3(memory_all,ip,new,time_info)
       storage_all = analyse_json.get_storage_info_ilo3(health_info)
       try:
           storage_ilo3_info(storage_all,ip,new,time_info)
       except:
           print('over')
       power_all = analyse_json.get_power_info_ilo3(health_info)
       power_ilo3_info(power_all,ip,new,time_info)
       power_sum_all = analyse_json.get_power_summary_ilo3_info(health_info)
       power_summary_info(power_sum_all, ip, ilo_model)
       processor_all = analyse_json.get_processors_info_ilo3(health_info)
       processors_info(processor_all, ip,ilo_model,new,time_info)




if __name__ == '__main__':

    num_threads = 200
    threads = []
    sql = "select HARDWARE_ID,IP_ILO,CHECK_NEW from ILO_INFO"
    g = db.connection_database(sql)
    start = time.clock()
    def base(g):
        while True:

            try:
                lock.acquire()
                id, ip, new = g.next()
                lock.release()
                print(ip)
                test(id,ip,new)
            except StopIteration:
                lock.release()
                break


    for i in range(num_threads):
       thread = threading.Thread(target=base, args=(g,))
       thread.start()
       threads.append(thread)
    for thread in threads: thread.join()
    end = time.clock()
    print(end-start)
