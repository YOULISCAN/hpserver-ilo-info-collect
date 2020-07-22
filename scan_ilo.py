
#网段扫描
import hpilo
import subprocess
import os



file = open("IP.txt",'r',encoding='utf-8')

class collect_IP():
    for i in file:
        i = i.strip()
        info = subprocess.call('ping -n 2 -w 5 %s' % '{0}'.format(i),stdout=subprocess.PIPE)
        if info == 1:
            print(i,"------>该IP正在使用中")

        else:
            print(i,"------>该IP闲置中")


