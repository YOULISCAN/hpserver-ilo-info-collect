import pymysql,nmap
connection = pymysql.connect(host='10.172.108.229', port=3306, user='SM', passwd='SM-dpbg123.',db='hpilo_info_collect', charset='utf8')

with connection.cursor() as cursor:
    sql = "select IP from using_IP"
    cursor.execute(sql)
    a = cursor.fetchall()
  #  cursor.fetchall()
    for ip in a:
        ip = str(ip).lstrip("(").rstrip(")").rstrip(",").strip("/'").strip()
        print("----------------开始扫描指定IP--------------------")
        nm = nmap.PortScanner()
        print("----------------扫描（22）端口--------------------")
        print(ip)
        portinfo = nm.scan(ip, '22')
        a = nm.csv()
        a = a.split(';')
        strr = 'HP Integrated Lights-Out mpSSH'
        for i in a:
            if i == strr:
                print("该IP用于ilo口")
                continue;
        #print(portinfo['scan'][ip]['tcp'][22]['product'])

