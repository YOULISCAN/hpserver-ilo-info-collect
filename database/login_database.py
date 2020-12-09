# -*- coding: utf-8 -*-

import cx_Oracle


def connection_database(sql):  #返回数据库中的ILO IP
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    with connection.cursor() as cursor:
        for i in cursor.execute(sql):
            yield (i[0],str(i[1]).lstrip('(').rstrip(")").strip(","),int(i[2]),str(i[3]))




