from selenium import webdriver
from public import Login

class LoginTest():
	
	def __init__(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(10)
		self.driver.get('http://www.126.com')
		
	def test_admin_login(self):
		username = 'admin'
		passwrod = '123'
		Login().user_login(self.driver, username, password)
		self.driver.quit()
		
	def test_guest_login(self):
		username = 'guest'
		password = '123'
		Login().user_login(self.driver, username, password)
		self.driver.quit()
		
LoginTest().test_admin_login()
LoginTest().test_guest_login()