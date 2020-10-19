# -*- coding: utf-8 -*-

import cx_Oracle
import hpilo
import analyse_json
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
        s = analyse_json.get_firmware_info(ilo.get_fw_version())# 获取FW版本信息
        ilo_model = s['management_processor']
        fw_version = s['firmware_version']
        fw_data = s['firmware_date']
        general_info = analyse_json.get_glance_info(ilo.get_embedded_health(),fw_version)
        bios_hardware = general_info['bios_hardware']
        fans = general_info['fans']
        temperature = general_info['temperature']
        power_supplies = general_info['power_supplies']
        battery = general_info['battery']
        processor = general_info['processor']
        memory = general_info['memory']
        network = general_info['network']
        storage = general_info['storage']
        insert_db.update_fw_info(product_name,server_name,ilo_model,fw_version,fw_data,ip)
        insert_db.update_server_general_info(bios_hardware,fans,temperature,power_supplies,battery,processor,memory,network,storage,ip)
            #获取硬件信息



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

    for i in range(num_threads):
        thread = threading.Thread(target=test(), args=(i,))
        thread.start()
#        threads.append(thread)
 #   for thread in threads: thread.join()
    end = time.clock()
    print(end-start)
