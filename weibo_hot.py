# 微博热搜监控脚本
# 使用说明：将下面的部分数据修改为你的，然后挂在腾讯云函数即可
# 本程序基于python3.6开发,仅做技术交流
# 更新时间：2020.07.15
# 作者；ck
import requests
import re
import json
import imaplib
import smtplib

######以下为需要修改的信息##########
#1：修改为你的发件邮箱地址,请使用QQ邮箱
email='15f5@qq.com'
#2：发件邮箱的授权码(需开启POP3/IMAP/SMTP)等服务
password_key='tffh'
#收件人邮箱
take_email= ['1f2@qq.com']

######通用信息，全局调用######
def sendEmail(data):
    from email.mime.text import MIMEText
    # email 用于构建邮件内容
    from email.header import Header
    # 用于构建邮件头
    # 发信方的信息：发信邮箱，QQ 邮箱授权码
    from_addr = email
    password = password_key
    # 收信方邮箱
    to_addr = ','.join(take_email)
    # 发信服务器
    smtp_server = 'smtp.qq.com'
    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    msg = MIMEText(data, 'plain', 'utf-8')
    # 邮件头信息
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header('微博热搜前十排行榜')
    # 开启发信服务，这里使用的是加密传输
    server = smtplib.SMTP_SSL(smtp_server)
    server.connect(smtp_server, 465)
    # 登录发信邮箱
    server.login(from_addr, password)
    # 发送邮件
    server.sendmail(from_addr, to_addr.split(','), msg.as_string())
    # 关闭服务器
    server.quit()
url = 'https://s.weibo.com/ajax/jsonp/gettopsug'
html = requests.get(url).text
pattern = re.compile('(?<=try{window.&\({"data":{"list":).*(?=,"top")')
json_list = pattern.findall(html)[0]
json =json.loads(json_list)
data = "热搜排行榜"+'\n\n'+\
       '第1为：'+json[0]['note']+'\n'+'吃瓜链接：'+'https://s.weibo.com/weibo?q=%23'+json[0]['note']+'%23&Refer=top'+'\n\n'+\
       '第2为：'+json[1]['note']+'\n'+'吃瓜链接：'+'https://s.weibo.com/weibo?q=%23'+json[1]['note']+'%23&Refer=top'+'\n\n'+\
       '第3为：'+json[2]['note']+'\n'+'吃瓜链接：'+'https://s.weibo.com/weibo?q=%23'+json[2]['note']+'%23&Refer=top'+'\n\n'+\
       '第4为：'+json[3]['note']+'\n'+'吃瓜链接：'+'https://s.weibo.com/weibo?q=%23'+json[3]['note']+'%23&Refer=top'+'\n\n'+\
       '第5为：'+json[4]['note']+'\n'+'吃瓜链接：'+'https://s.weibo.com/weibo?q=%23'+json[4]['note']+'%23&Refer=top'+'\n\n'+\
       '第6为：'+json[5]['note']+'\n'+'吃瓜链接：'+'https://s.weibo.com/weibo?q=%23'+json[5]['note']+'%23&Refer=top'+'\n\n'+\
       '第7为：'+json[6]['note']+'\n'+'吃瓜链接：'+'https://s.weibo.com/weibo?q=%23'+json[6]['note']+'%23&Refer=top'+'\n\n'+\
       '第8为：'+json[7]['note']+'\n'+'吃瓜链接：'+'https://s.weibo.com/weibo?q=%23'+json[7]['note']+'%23&Refer=top'+'\n\n'+\
       '第9为：'+json[8]['note']+'\n'+'吃瓜链接：'+'https://s.weibo.com/weibo?q=%23'+json[8]['note']+'%23&Refer=top'+'\n\n'+\
       '第10为：'+json[9]['note']+'\n'+'吃瓜链接：'+'https://s.weibo.com/weibo?q=%23'+json[9]['note']+'%23&Refer=top'
sendEmail(data)

