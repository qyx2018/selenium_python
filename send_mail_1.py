import smtplibi
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtpserver = 'smtp.sina.com'
sender = 'username@sina.com'
receiver = 'receiver@126.com'

user = 'username@sina.com'
password = '123456'

subject = 'Python send email test'

sendfile = open('D:\\testpro\\report\\log.txt', 'rb').read()

att = MIMEText(sendfile, 'base64', 'utf-8')
att['Content-Type'] = 'application/octet-stream'
att['Content-Disposition'] = 'attachment; filename = "log.txt"'

msgRoot = MIMEMultipart('related')

msgRoot['Subject'] = subject
msgRoot.attach(att)

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msgROot.as_string())
smtp.quit()