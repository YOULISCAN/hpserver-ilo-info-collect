# -*- coding: utf-8 -*-

import cx_Oracle
import hpilo
import analyse_json
#import login
import database.login_database as db



if __name__ == '__main__':
    sql = 'select IP_ILO from ILO_INFO'

    g = db.connection_database(sql)
    try:
        while g.next():
            print(g.next())
    except StopIteration:
        pass
    finally:
        pass