import hpilo

ilo = hpilo.Ilo('10.172.100.178',login='admin',password='password')

all_info = ilo.get_embedded_health()

fan = all_info['fans']

temperature = all_info['temperature']

power_supplies = all_info['power_supplies']

power_supply_summary = all_info['power_supply_summary']

processors = all_info['processors']

memory = all_info['memory']

nim_information = all_info['nic_information']

storage = all_info['storage']

firmware_information = all_info['firmware_information']

health_at_a_glance = all_info['health_at_a_glance']
