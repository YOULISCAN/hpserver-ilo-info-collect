import hpilo
ilo = hpilo.Ilo('10.172.100.235','admin','iL0!@#123',delayed=True)
ilo1 = hpilo.IloWarning('10.172.100.236','admin','iL0!@#123',delayed=True)
print(ilo.get_fw_version())
print(ilo.get_uid_status())

print(ilo.call_delayed())
