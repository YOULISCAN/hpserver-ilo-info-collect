# -*- coding: utf-8 -*-

import cx_Oracle


def connection_database(sql):
    connection = cx_Oracle.connect('gl_sm/gl_sm@10.195.227.244/db244d')
    with connection.cursor() as cursor:
        for i in cursor.execute(sql):
            yield (str(i).lstrip('(').rstrip(")").strip(","))




