# -*- coding: utf-8 -*-
'''
存在DBA只提供查询账号给我们，SM的设备仍然需要创建统一的账号密码 遂使用try语句加上生成器完成
'''
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
            ip = g.next().lstrip("'").rstrip("'")
            try:
                ilo = hpilo.Ilo(ip,login='admin',password='iL0!@#123')
                ilo.add_user(user_login='MonitorTools',user_name='MonitorTools',password='ping.p.shen@foxconn.com',remote_cons_priv=False,config_ilo_priv=False)
            except hpilo.IloLoginFailed :
                print("该IP {} 为DBA设备".format(ip))
            except hpilo.IloError:
                print("该IP {} 账号已存在".format(ip))
            finally:
                pass
    except StopIteration:
        pass
    finally:
        pass
