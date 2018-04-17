from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os

def send_mail(file_new):
	f = open(file_new, 'rb')
	mail_body = f.read()
	f.close()
	
	msg = MIMEText(mail_body, 'html', 'utf-8')
	msg['Subject'] = Header('Selenium Report', 'utf-8')
	
	smtp = smtplib.SMTP()
	smtp.connect('smtp.126.com')
	smtp.login('username@126.com', '123456')
	smtp.sendmail('username@126.com', 'receive@126.com', msg.as_string())
	smtp.quit()
	print('email has send out')
	
	def new_report(testreport):
		lists = os.listdir(testreport)
		lists.sort(key = lambda fn: os.path.getmtime(testreport + '\\' +fn))
		file_new = os.path.join(testreport, lists[-1])
		print(file_new)
		return file_new
		
	if __name__ == '__main__':
		test_dir = 'D:\\testpro\\test_case'
		test_report = 'D:\\testpro\\report'
		
		discover = unittest.defaultTesetLoader.discover(test_dir, pattern = 'test_*.py')
		
		now = time.strftime('%Y-%m-%d_%H_%M_%S')
		filename = test_report + '\\' + now + 'result.html'
		fp = openm(filename, 'wb')
		runner = HTMLTestRunner(stream = fp, title = 'Testing report', description = 'Details: ')
		
		runner.run(discover)
		fp.close()
		
		new_report  new_report(test_report)
		send_mail(new_report)