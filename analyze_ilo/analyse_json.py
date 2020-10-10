# -*- coding: utf-8 -*-
import hpilo

class iLo_info():

    def get_firmware_info(self,all_info):
        firmware = all_info['firmware_information']
        for i in firmware.items():
            print(i)


    def get_storage_info_ilo3(self,all_info):
        storage = all_info['drives_backplanes']
        for i in storage:
            print("firmware_version: {}; enclosure: {};".format(i['firmware_version'],i['enclosure_addr']))
            for j in i['drive_bays'].items():
                print("addr:{}; status:{}; product_id:{}; uid_led:{}".format(j[0],j[1]['status'],j[1]['product_id'],j[1]['uid_led']))

    def get_storage_info(self,all_info):
        storage = all_info['storage']
        Controller_on_System_Board = storage['Controller on System Board']
        print("Controller on System Board_status:{}; controller_status:{}; cache_module_memory:{};".format(Controller_on_System_Board['status'],Controller_on_System_Board['controller_status'],Controller_on_System_Board['cache_module_memory']))
        print('drive_enclosures:')
        for i in Controller_on_System_Board['drive_enclosures']:
            print("     {}".format(i))
        logical_drives = Controller_on_System_Board['logical_drives']
        print('logical_drives:')
        print("   status: {}; capacity: {}; fault_tolerance: {}; logical_drive_type: {}".format(logical_drives[0]['status'],logical_drives[0]['capacity'],logical_drives[0]['fault_tolerance'],logical_drives[0]['logical_drive_type']))
        physical_drives = logical_drives[0]['physical_drives']
        for i in physical_drives:
            print(i)

    def get_memory_info(self,all_info):
        memory = all_info['memory']
        details = memory["memory_details"]
        print("{}:".format('memory'))
        for i in details.keys():
            for j in details[i].values():
                if j['status'] == 'Not Present':
                    continue
                else:
                    print("status:{}; hp_smart_memory:{}; socket:{}; part:{}; type:{}; size:{}; frequency:{}".format(j['status'], j['hp_smart_memory'], j['socket'], j['part'], j['type'], j['size'], j['frequency']))

    def get_memory_info_ilo3(self,all_info):
        memory = all_info['memory']
        print("{}:".format('memory'))
        for i in memory.values()[0]:
            if i[1][1]['value'] == "Not Installed":
                pass
            else:
                print("memory_location:{}; memory_size:{}; memory_speed:{}".format(i[0][1]['value'],i[1][1]['value'],i[2][1]['value']))

    def get_network_info_ilo3(self,xmldata):
        network = xmldata['hsi']['nics']
        print("network:")
        for i in network:
            if i['status'] != 'Unknown' and i['status'] != 'Disabled' :
                print("description: {}; status: {}; ipaddr: {}; macaddr: {}; port: {}".format(i['description'],i['status'],i['ipaddr'],i['macaddr'],i['port']))
    def get_network_info(self,xmldata):
        network = xmldata['hsi']['nics']
        print("network:")
        for i in network:
            if i['status'] != 'Unknown' and i['status'] != 'Disabled':
                print("description: {}; status: {}; ipaddr: {}; macaddr: {}; port: {}".format(i['description'],
                                                                                              i['status'], i['ipaddr'],
                                                                                              i['macaddr'], i['port']))

    def get_processors_info_ilo3(self,all_info):
        proces = all_info['processors']
        for i in proces:
            print("{}: ;speed:{}; execution_technology:{}".format(i,proces[i]['speed'],proces[i]['execution_technology']))

    def get_processors_info(self,all_info):
        proces = all_info['processors']
        for i in proces:
            print("{}: name:{}; status:{}; speed:{}".format(i,proces[i]['name'],proces[i]['status'],proces[i]['speed']))

    def get_fan_info(self,all_info):

        fan = all_info['fans']
        for i in range(1,len(fan)+1):
            print("风扇{2}状态：{0},风扇{2}速度：{1}".format(fan["Fan %d"%i]["status"],fan["Fan %d"%i]["speed"],i))

    def get_fan_info_ilo3(self,all_info):
        fan = all_info['fans']
        for i in fan.items():
            print("{}: status:{}; speed:{}".format(i[0],i[1]['status'],i[1]['speed']))


    def get_power_info(self,all_info):
        power_supplies = all_info['power_supplies']
        for i in power_supplies:
            print("{}: 'status: {}; capacity: {}".format(i,power_supplies[i]['status'],power_supplies[i]['capacity']))

        power_supply_summary = all_info['power_supply_summary']
        print("present_power_reading: {};\
               power_management_controller_firmware_version: {};\
               power_system_redundancy: {};\
               high_efficiency_mode: {}".format(power_supply_summary['present_power_reading'],
                                                power_supply_summary['power_management_controller_firmware_version'],
                                                power_supply_summary['power_system_redundancy'],
                                                power_supply_summary['high_efficiency_mode']))


    def get_power_info_ilo3(self,all_info):
        power = all_info['power_supplies']
        for i in power:
            print("{}: 'status: {}".format(i, power[i]['status']))

    def get_temperature_info(self,all_info):
        temper = all_info['temperature']
        for i in temper:
            print("{}: currentreading:{} caution:{}".format(i,temper[i]['currentreading'],temper[i]['caution']))

    def get_temperature_info_ilo3(self,all_info):
        temper = all_info['temperature']
        for i in temper:
            print("{}: currentreading:{} caution:{}".format(i,temper[i]['currentreading'],temper[i]['caution']),temper[i]['location'])

    def get_glance_info(self,all_info):
        glance = all_info['health_at_a_glance']
        print("bios_hardware:\
              fans status:{}\
              temperature status:{}\
              power_supplies status:{}\
              battery status:{}\
              processor status:{}\
              memory status:{}\
              network status:{}\
              storage status:{}".format(glance['bios_hardware']['status'],
                                        glance['fans']['status'],
                                        glance['temperature']['status'],
                                        glance['power_supplies']['status'],
                                        glance['battery']['status'],
                                        glance['processor']['status'],
                                        glance['memory']['status'],
                                        glance['network']['status'],
                                        glance['storage']['status']))


    def get_glance_info_ilo3(self,all_info):
        glance = all_info['health_at_a_glance']
        print("bios_hardware:\
                      fans status:{}\
                      temperature status:{}\
                      power_supplies status:{}\
                      drive status:{}".format(
                                                glance['fans']['status'],
                                                glance['temperature']['status'],
                                                glance['power_supplies']['status'],
                                                glance['drive']['status']))
    def get_glance_info_ilo4(self,all_info):
        glance = all_info['health_at_a_glance']
        print("bios_hardware:\
                      fans status:{}\
                      temperature status:{}\
                      power_supplies status:{}\
                      processor status:{}\
                      memory status:{}\
                      network status:{}\
                      storage status:{}".format(glance['bios_hardware']['status'],
                                                glance['fans']['status'],
                                                glance['temperature']['status'],
                                                glance['power_supplies']['status'],
                                                glance['processor']['status'],
                                                glance['memory']['status'],
                                                glance['network']['status'],
                                                glance['storage']['status']))

    def get_log_info(self,ilo):
        server_event = ilo.get_server_event_log()
        with open('server_event.txt','w+') as f:
            f.write(str(server_event))
        log_event = ilo.get_ilo_event_log()
        with open('ilo_log.txt','w+') as f:
            f.write(str(log_event))

class ilo4_info():
    pass



class ilo3_info():
    pass



if __name__ == '__main__':
    ip = str(input("请输入IP:"))
    login = str(input("请输入用户名:"))
    password = str(input("请输入密码:"))
    ilo = hpilo.Ilo(ip,login=login,password=password)

    #获取基本信息
    server = ilo.get_product_name() #获得服务器型号
    hostname = ilo.get_server_name() #获得主机名称
    all_info = ilo.get_embedded_health()
    a = iLo_info()
    xmldata = ilo.xmldata()
    version = ilo.get_fw_version()
    if version['management_processor'] == 'iLO3':
        a.get_glance_info_ilo3(all_info)
        a.get_fan_info_ilo3(all_info)
        a.get_temperature_info_ilo3(all_info)
        a.get_power_info_ilo3(all_info)
        a.get_processors_info_ilo3(all_info)
        a.get_memory_info_ilo3(all_info)
        a.get_network_info_ilo3(xmldata)
        a.get_storage_info_ilo3(all_info)
        a.get_firmware_info(all_info)
    elif version['management_processor'] == 'iLO4':
        a.get_log_info(ilo)
        a.get_glance_info_ilo4(all_info)
        a.get_fan_info(all_info)
        a.get_temperature_info(all_info)
        a.get_processors_info(all_info)
        a.get_memory_info(all_info)
        a.get_network_info(xmldata)
        a.get_power_info(all_info)
        a.get_storage_info(all_info)
        a.get_firmware_info(all_info)
    else:
        a.get_log_info(ilo)
        a.get_glance_info(all_info)
        a.get_fan_info(all_info)
        a.get_temperature_info(all_info)
        a.get_processors_info(all_info)
        a.get_memory_info(all_info)
        a.get_network_info(xmldata)
        a.get_power_info(all_info)
        a.get_storage_info(all_info)
        a.get_firmware_info(all_info)