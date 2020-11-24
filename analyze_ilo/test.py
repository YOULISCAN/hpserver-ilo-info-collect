# -*- coding: utf-8 -*-

import re

list = ['Battery 1','Battery 2','Power Supply 1','Power Supply 2']

for i in list:
    print(re.match('Battery',i))