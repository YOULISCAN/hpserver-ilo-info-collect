# -*- coding: utf-8 -*-
import hpilo



def get_firmware_info(all_info):
    return {'firmware_date':all_info['firmware_date'],
            'firmware_version':all_info['firmware_version'],
            'management_processor':all_info['management_processor']}



def get_storage_info_ilo3(all_info):
    storage = all_info['drives_backplanes']
    yield(len(storage))
    for i in storage:
        print("firmware_version: {}; enclosure: {};".format(i['firmware_version'],i['enclosure_addr']))
        for j in i['drive_bays'].items():
            yield(str(j[0]),j[1]['status'],j[1]['product_id'])

def get_storage_info(all_info):
    storage = all_info['storage']
    Controller_on_System_Board = storage['Controller on System Board']
    logical_drives = Controller_on_System_Board['logical_drives']
    yield (len(logical_drives))
    for i in range(0,len(logical_drives)):
        try:
            print(logical_drives[i]['label'],logical_drives[i]['status'],logical_drives[i]['capacity'],logical_drives[i]['fault_tolerance'],logical_drives[i]['logical_drive_type'])
        except :
            logical_drives[i]['logical_drive_type']=None
        finally:
            yield(logical_drives[i]['label'],logical_drives[i]['status'],logical_drives[i]['capacity'],logical_drives[i]['fault_tolerance'],logical_drives[i]['logical_drive_type'],len(logical_drives[i]['physical_drives']))
            for j in range(0,len(logical_drives[i]['physical_drives'])):
                print(logical_drives[i]['physical_drives'][j]['label'],logical_drives[i]['physical_drives'][j]['status'],
                      logical_drives[i]['physical_drives'][j]['capacity'],logical_drives[i]['physical_drives'][j]['model'],
                      logical_drives[i]['physical_drives'][j]['fw_version'],logical_drives[i]['physical_drives'][j]['drive_configuration'],
                      logical_drives[i]['physical_drives'][j]['serial_number'])
                yield(logical_drives[i]['physical_drives'][j]['label'],logical_drives[i]['physical_drives'][j]['status'],
                      logical_drives[i]['physical_drives'][j]['capacity'],logical_drives[i]['physical_drives'][j]['model'],
                      logical_drives[i]['physical_drives'][j]['fw_version'],logical_drives[i]['physical_drives'][j]['drive_configuration'],
                      logical_drives[i]['physical_drives'][j]['serial_number'])




def get_memory_info(all_info):
    memory = all_info['memory']
    details = memory["memory_details"]
    yield(len(details))
    for i in details.keys():
        yield(len(details[i]))
        for j in details[i].values():
            yield (i,j['socket'],j['status'], j['part']['number'], j['type'], j['size'], j['frequency'],j['minimum_voltage'])
            # if j['status'] == 'Not Present':
            #     continue
            # else:
            #     print("status:{}; hp_smart_memory:{}; socket:{}; part:{}; type:{}; size:{}; frequency:{}".format(j['status'], j['hp_smart_memory'], j['socket'], j['part']['number'], j['type'], j['size'], j['frequency']))

def get_memory_info_ilo3(all_info):
    memory = all_info['memory']
    yield (len(memory))
    for i in memory.values()[0]:
        yield(i[0][1]['value'],i[1][1]['value'],i[2][1]['value'])
 #       print("memory_location:{}; memory_size:{}; memory_speed:{}".format(i[0][1]['value'],i[1][1]['value'],i[2][1]['value']))

# def get_network_info_ilo3(xmldata):
#     network = xmldata['hsi']['nics']
#     print("network:")
#     for i in network:
#         if i['status'] != 'Unknown' and i['status'] != 'Disabled' :
#             print("description: {}; status: {}; ipaddr: {}; macaddr: {}; port: {}".format(i['description'],i['status'],i['ipaddr'],i['macaddr'],i['port']))
def get_network_info(xmldata):
    network = xmldata['hsi']['nics']
    print("network:")
    yield(len(network))
    for i in network:
        # if i['status'] != 'Unknown' and i['status'] != 'Disabled':
        #print("description: {}; status: {}; ipaddr: {}; macaddr: {}; port: {}".format(i['description'],i['status'], i['ipaddr'],i['macaddr'], i['port']))
        yield (i['description'],i['status'], i['ipaddr'],i['macaddr'], i['port'])



def get_processors_info_ilo3(all_info):
    proces = all_info['processors']
    for i in proces:
        print("{}: ;speed:{}; execution_technology:{}".format(i,proces[i]['speed'],proces[i]['execution_technology']))

def get_processors_info(all_info):
    proces = all_info['processors']
    for i in proces:
        print("{}: name:{}; status:{}; speed:{}".format(i,proces[i]['name'],proces[i]['status'],proces[i]['speed']))

def get_fan_info(ilo_model,all_info):
    dict_fan = {}
    fan = all_info['fans']
    #for i in range(1, len(fan) + 1):
    yield (len(fan))
    for i in fan.items():
        i[1]["speed"] = list(i[1]["speed"])
#        speed =
        print(len(fan),i[1],i[1]['speed'][0],i[1]['zone'])
        yield(i[1]["status"],i[1]['speed'][0],i[1]["zone"],i[1]["label"])
#        print("风扇{2}状态：{0},风扇{2}速度：{1},风扇{2}位置：{3}".format(fan["Fan %d"%i]["status"],fan["Fan %d"%i]["speed"],i,fan["Fan %d"%i]['zone']))


# def get_fan_info_ilo3(all_info):
#     fan = all_info['fans']
#     for i in fan.items():
#         print("{}: status:{}; speed:{}".format(i[0],i[1]['status'],i[1]['speed']))


def get_power_info(all_info):
    power_supplies = all_info['power_supplies']
    number = len(power_supplies)
    yield (number)
    for i in power_supplies:
        if i == 'Battery 1':
            yield(power_supplies[i]['label'],power_supplies[i]['status'],power_supplies[i]['present'],power_supplies[i]['model'],
                  power_supplies[i]['spare'],power_supplies[i]['firmware_version'],power_supplies[i]['capacity'],power_supplies[i]['serial_number'])
            print(power_supplies[i]['label'],power_supplies[i]['status'],power_supplies[i]['present'],power_supplies[i]['model'],
                  power_supplies[i]['spare'],power_supplies[i]['firmware_version'],power_supplies[i]['capacity'],power_supplies[i]['serial_number'])

        else:
            yield(power_supplies[i]['label'],power_supplies[i]['status'],power_supplies[i]['serial_number'],power_supplies[i]['capacity'],
                  power_supplies[i]['hotplug_capable'],power_supplies[i]['model'],power_supplies[i]['present'],power_supplies[i]['spare'],
                  power_supplies[i]['firmware_version'],power_supplies[i]['pds'])
            print(power_supplies[i]['label'],power_supplies[i]['status'],power_supplies[i]['serial_number'],power_supplies[i]['capacity'],
                  power_supplies[i]['hotplug_capable'],power_supplies[i]['model'],power_supplies[i]['present'],power_supplies[i]['spare'],
                  power_supplies[i]['firmware_version'],power_supplies[i]['pds'])

    power_supply_summary = all_info['power_supply_summary']
    yield(power_supply_summary['high_efficiency_mode'],power_supply_summary['power_management_controller_firmware_version'],
          power_supply_summary['present_power_reading'],power_supply_summary['power_system_redundancy'],
          power_supply_summary['hp_power_discovery_services_redundancy_status'])
    print("present_power_reading: {};\
           power_management_controller_firmware_version: {};\
           power_system_redundancy: {};\
           high_efficiency_mode: {}".format(power_supply_summary['present_power_reading'],
                                            power_supply_summary['power_management_controller_firmware_version'],
                                            power_supply_summary['power_system_redundancy'],
                                            power_supply_summary['high_efficiency_mode']))


def get_power_info_ilo3(all_info):
    power = all_info['power_supplies']
    for i in power:
        yield(i, power[i]['status'])
    power_supply_summary = all_info['power_supply_summary']
    yield (power_supply_summary['high_efficiency_mode'], power_supply_summary['power_management_controller_firmware_version'],
           power_supply_summary['present_power_reading'])

def get_temperature_info(all_info):
    temper = all_info['temperature']
    for i in temper:
        print("{}: currentreading:{} caution:{}".format(i,temper[i]['currentreading'],temper[i]['caution']))

def get_temperature_info_ilo3(all_info):
    temper = all_info['temperature']
    for i in temper:
        print("{}: currentreading:{} caution:{}".format(i,temper[i]['currentreading'],temper[i]['caution']),temper[i]['location'])

def get_glance_info(all_info,fw_version):
    glance = all_info['health_at_a_glance']
 #   if fw_version == 'iLO5':
    try:
        try:
            print(glance['bios_hardware']['status'])
        except KeyError:
            glance['bios_hardware'] = {'status': 'None'}
        finally:
            pass

        try:
            print(glance['processor']['status'])
        except KeyError:
            glance['processor'] = {'status': 'None'}
        finally:
            pass

        try:
            print(glance['memory']['status'])
        except KeyError:
            glance['memory'] = {'status': 'None'}
        finally:
            pass

        try:
            print(glance['network']['status'])
        except KeyError:
            glance['network'] = {'status': 'None'}
        finally:
            pass

        try:
            print(glance['storage']['status'])
        except KeyError:
            glance['storage'] = glance.pop('drive')
        finally:
            pass

        print(glance['battery']['status'])
    except KeyError:
        glance['battery']={'status': 'None'}

   #     glance['battery']['status'] = None
    finally:
        return ({"bios_hardware": glance['bios_hardware']['status'],
                 "fans": glance['fans']['status'],
                 "temperature": glance['temperature']['status'],
                 "power_supplies": glance['power_supplies']['status'],
                 "battery": glance['battery']['status'],
                 "processor": glance['processor']['status'],
                 "memory": glance['memory']['status'],
                 "network": glance['network']['status'],
                 "storage": glance["storage"]['status']
                 })
"""
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
"""
    # elif fw_version == "iLO3":
    #     glance = all_info['health_at_a_glance']
    #     return({'fans': glance['fans']['status'],
    #             'temperature': glance['temperature']['status'],
    #             'power_supplies': glance['power_supplies']['status'],
    #             'drive': glance['drive']['status'],
    #
    #             })


"""
        print("bios_hardware:\
                          fans status:{}\
                          temperature status:{}\
                          power_supplies status:{}\
                          drive status:{}".format(
            glance['fans']['status'],
            glance['temperature']['status'],
            glance['power_supplies']['status'],
            glance['drive']['status']))
        
"""
    # else:
    #     glance = all_info['health_at_a_glance']
    #     return({"bios_hardware": glance["bios_hardware"]['status'],
    #             "fans": glance["fans"]['status'],
    #             "temperature": glance["temperature"]['status'],
    #             "power_supplies": glance["power_supplies"]['status'],
    #             "processor": glance["processor"]['status'],
    #             "memory": glance["memory"]['status'],
    #             "network": glance["network"]['status'],
    #             "storage": glance["storage"]['status']
    #             })
"""
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
"""


def get_log_info(ilo):
    server_event = ilo.get_server_event_log()
    with open('server_event.txt','w+') as f:
        f.write(str(server_event))
    log_event = ilo.get_ilo_event_log()
    with open('ilo_log.txt','w+') as f:
        f.write(str(log_event))


