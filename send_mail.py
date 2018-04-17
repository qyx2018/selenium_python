import smtplib
import email.mime.text import MIMEText
import email.header import Header

smtpserver = 'smtp.sina.com'
user = 'username@sina.com'
password = '123456'
sender = 'username@sina.com'
receiver = 'receive@126.com'
subject = 'Python email test'

msg = MIMEText('<html><h1>你好!</h1></html>', 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()