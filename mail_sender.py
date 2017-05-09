#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header


mail_host = "smtp.163.com"  # 设置服务器
mail_user = ""  # 用户名
mail_pass = ""  # 口令

sender = ''
receiver = ''
receivers = [receiver]  #

message = MIMEText("""Thank""", 'plain', 'utf-8')
message['From'] = Header(mail_user, 'utf-8')
message['To'] = Header(receiver)

subject = 'Python project!'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  #
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "Send email!"
except smtplib.SMTPException,e:
    print e
    print "Error: Can't send the email"
