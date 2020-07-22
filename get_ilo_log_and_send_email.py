#!/usr/bin/python
# coding=utf-8

import hpilo
import multiprocessing
# import servers
import os
import ConfigParser
import smtplib
from email.header import Header
from email.mime.text import MIMEText

newlogfile_url = '/root/hpilo/newlog'
configfile_url = '/root/hpilo/.ilo.conf'

# mail information
email_server = "ip"
port = 25
email_user = "user"
email_password = "passwd"
sender = "sender"
receivers = ["2073665763@qq.com", "18260067809@163.com"]


def get_all_ilos():
    return [
        '192.168.130.38', 
        '192.168.130.44', 
        '192.168.130.45', 
        '192.168.130.43', 
        '192.168.130.55', 
        '192.168.130.59', 
        '192.168.130.51', 
        '192.168.130.52', 
        '192.168.130.60', 
        '192.168.130.61', 
        '192.168.130.53', 
        '192.168.130.54'
    ]


def CheckIfExist(file_url, log_str):
    with open(file_url, 'r') as file:
        for line in file.readlines():
            if log_str in line:
                return True
    return False


def GetIloLogs(args):
    ilo_ip, username, password = args
    ilo = hpilo.Ilo(ilo_ip, username, password)
    iml_logs = ilo.get_server_event_log()
    logfile_url = "/data/hpilo_log/" + ilo_ip
    with open(logfile_url, 'a+') as logfile:
        for iml_log in iml_logs:
            format_log = iml_log['last_update'] + ' ' + ilo_ip + ' ' + iml_log['severity'] + \
                ' ' + iml_log['class'] + ' ' + iml_log['description'] + '\n'
            if not CheckIfExist(logfile_url, format_log):
                logfile.write(format_log)
                with open(newlogfile_url, 'a') as newlog:
                    iml_log['host'] = ilo_ip
                    newlog.write(str(iml_log) + '\n')


def ConvertToHTML(file):
    with open(file, 'r') as f:
        newlogs = [eval(line.rstrip('\n')) for line in f.readlines()]
    mail_msg = '''
        <!DOCTYPE html>
        <html>
        <body>
            <table style="border-collapse:collapse;width:100%;text-align:left;">
                <tr>
                    <th style="text-align:left;padding:6px;background-color:#9FBCDE;color:white;">编号</th>
                    <th style="text-align:left;padding:6px;background-color:#9FBCDE;color:white;">管理口IP</th>
                    <th style="text-align:left;padding:6px;background-color:#9FBCDE;color:white;">严重级别</th>
                    <th style="text-align:left;padding:6px;background-color:#9FBCDE;color:white;">描述</th>
                    <th style="text-align:left;padding:6px;background-color:#9FBCDE;color:white;">发生时间</th>
                    <th style="text-align:left;padding:6px;background-color:#9FBCDE;color:white;">最后更新时间</th>
                </tr>
            '''
    i = 0
    for newlog in newlogs:
        i += 1
        if not i % 2:
            mail_msg += '''<tr style="background-color:#f2f2f2">'''
        else:
            mail_msg += "<tr>"
        mail_msg += '''<td style="text-align:left;padding:6px;">''' + \
            str(i) + "</td>"
        mail_msg += '''<td style="text-align:left;padding:6px;">''' + \
            newlog['host'] + "</td>"
        mail_msg += '''<td style="text-align:left;padding:6px;">''' + \
            newlog['severity'] + "</td>"
        mail_msg += '''<td style="text-align:left;padding:6px;">''' + \
            newlog['description'] + "</td>"
        mail_msg += '''<td style="text-align:left;padding:6px;">''' + \
            newlog['initial_update'] + "</td>"
        mail_msg += '''<td style="text-align:left;padding:6px;">''' + \
            newlog['last_update'] + "</td>"
        mail_msg += "</tr>"

    mail_msg += '''
            </table>
        </body>
        </html>
        '''
    return mail_msg


def send_email(server, port, user, password, sender, receivers, content):
    smtpObj = smtplib.SMTP()
    message = MIMEText(content, 'html', 'utf-8')
    message['To'] = Header(','.join(receivers))
    subject = 'NGCC HP服务器巡检报告'
    message['Subject'] = Header(subject, 'utf-8')
    smtpObj.connect(server, port)
    smtpObj.login(user, password)
    smtpObj.sendmail(sender, receivers, message.as_string())


if __name__ == '__main__':
    config = ConfigParser.ConfigParser()
    config.read(configfile_url)
    username = None
    password = None
    if config.has_option('ilo', 'username'):
        username = config.get('ilo', 'username')
    if config.has_option('ilo', 'password'):
        password = config.get('ilo', 'password')
    if not username or not password:
        print "Please provide ilo login details"

    ilos_ip = get_all_ilos()
    ilos_config = [(ilo_ip, username, password) for ilo_ip in ilos_ip]
    with open(newlogfile_url, 'r+') as f:
        f.truncate()
    multiprocessing.Pool().map(GetIloLogs, ilos_config)

    html = ConvertToHTML(newlogfile_url)
    send_email(email_server, port, email_user, email_password, sender, receivers, html)
