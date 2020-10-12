import pymysql
import hpilo



def connetion_database(): #连接数据库拖出所有ilo IP
    connection = pymysql.connect(host='10.172.108.229',
                                 port=3306,
                                 user='SM',
                                 passwd='SM-dpbg123.',
                                 db='hpilo_info_collect',
                                 charset='utf8')
    try:
        with connection.cursor() as cursor:
            sql = "select IP from ilo_IP"
            cursor.execute(sql)
            all_ilo = cursor.fetchall()
    finally:
        connection.close()
    return all_ilo


def get_server_info(ip):
    health = ip.get_embedded_health()

def get_fw_version():
    pass
def get_product_name():
    pass
def get_server_name():
    pass
def get_uid_status():
    pass
def get_network_settings():
    pass
def get_all_users():
    pass
def get_server_health():
    pass
    #get_embedded_health()
def get_host_power_status():
    pass
def get_power_readings():
    pass
def get_ilo_event_log():
    pass
def get_server_event_log():
    pass


if __name__ == '__main__':
    all_ilo = []
    cannot_connection = []
    all_ip = connetion_database()
    for ip in all_ip:
        ip = str(ip).lstrip("(").rstrip(")").rstrip(",").strip("/'").strip()
        all_ilo.append(ip)
    for ip in all_ilo:
        try:
            ip = hpilo.Ilo(ip,login="admin",password="iL0!@#123")
            print(ip.get_fw_version())
        except:
            cannot_connection.append(ip)
            print("账号密码不对")
        else:
            print(get_server_info(ip))

