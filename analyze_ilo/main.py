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
        fan_info(ip)
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
