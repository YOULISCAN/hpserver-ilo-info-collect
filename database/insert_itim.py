# -*- coding: utf-8 -*-

import cx_Oracle

connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')

sql = 'select IP_ILO from ILO_INFO'

with connection.cursor() as cursor:
    for row in cursor.execute(sql):
        print(row)