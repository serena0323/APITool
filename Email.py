# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import datetime


def send_report(from_addrs, from_pwd, host, to_addrs, subject, plainText, htmlText):
    # from_addrs = 'serena.luo@wesoft.com'
    # from_pwd = "xxxxxx"
    # host = "10.200.1.28"

    ctime = datetime.datetime.now()
    subject = ctime.strftime("%Y-%m-%d %H:%M:%S") + subject

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = subject
    msgRoot['From'] = from_addrs
    msgRoot['To'] = to_addrs

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    # 设定纯文本信息
    msgText = MIMEText(plainText, 'plain', 'utf-8')
    msgAlternative.attach(msgText)

    # 设定HTML信息
    msgHTML = MIMEText(htmlText, 'html', 'utf-8')
    msgAlternative.attach(msgHTML)

    try:
        server = smtplib.SMTP(host)
        server.login(from_addrs, from_pwd)
        server.sendmail(from_addrs, to_addrs, msgRoot.as_string())
        print
        "邮件发送成功"
    except smtplib.SMTPException:
        print
        "Error: 无法发送邮件"
