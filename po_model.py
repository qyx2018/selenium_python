from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Page(object):
	'''
	基础类， 用于页面对象类的继承
	'''
	
#	login_url = 'http://www.126.com'
	login_url = 'http://www.baidu.com'
	
	def __init__(self, selenium_driver, base_url = login_url):
		self.base_url = base_url
		self.driver = selenium_driver
		self.timeout = 30
		
	def on_page(self):
		return self.driver.current_url == (self.base_url + self.url)     #将当前的页面与http://www.126.com进行比较。
		
	def _open(self, url):
		url = self.base_url + url
		self.driver.get(url)
#		assert self.on_page(), 'Did not land on %s' % url
		
	def open(self):
		self._open(self.url)
		
	def find_element(self, *loc):
		return self.driver.find_element(*loc)
		

class LoginPage(Page):
	'''
	126邮箱登录页面模型
	'''
	url = '/'
	
#	username_loc = (By.ID, "auto-id-1515396667310")
#	password_loc = (By.ID, 'auto-id-1515396667311')
#	submit_loc = (By.ID, 'dologin')
#	username_loc = (By.ID, 'kw')
	username_loc = (By.ID, 'kw')
	submit_loc = (By.ID, 'su')
	
	def type_username(self, username):
		self.find_element(*self.username_loc).send_keys(username)
		
#	def type_password(self, password):
#		self.find_element(*self.password_loc).send_keys(password)
		
	def submit(self):
		self.find_element(*self.submit_loc).click()
		

#def test_user_login(driver, username, password):
def test_user_login(driver, username):
	'''
	测试获取的用户名/密码是否可以登录
	'''
	login_page = LoginPage(driver)
	login_page.open()
	login_page.type_username(username)
#	login_page.type_password(password)
	login_page.submit()
	
def main():
	try:
		driver = webdriver.Chrome()
#		username = 'username'
#		password = '123456'
#		driver.switch_to_frame('x-URS-iframe')
		username = webdriver
#		test_user_login(driver, username, password)
		test_user_login(driver, username)
		sleep(3)
#		text = deriver.find_element_by_xpath("//span[@id='spnUid']").text
#		assert(text == 'username@126.com'), '用户名称不匹配，登录失败！'
		title = driver.title
		assertEqual(title, 'webdriver_百度搜索')
	finally:
		driver.close()
		
if __name__ == '__main__':
	main()