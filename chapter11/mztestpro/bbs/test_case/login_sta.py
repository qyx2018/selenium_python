from time import sleep
import unittest, random, sys
sys.path.append('./models')
sys.path.append('./page_obj')
from models import myunit, function
from page_obj.loginPage import login

class loginTest(myunit.MyTest):
	
	def user_login_verify(self, username = '', password = ''):
		login(self.driver).user_login(username, password)
		
	def test_login1(self):
		self.user_login_verify()
		po = login(self.driver)
		self.assertEqual(po.user_error_hint(), '账号不能为空')
		self.assertEqual(po.pawd_error_hint(), '密码不能为空')
		function.insert_img(self.driver, 'user_pawd_empty.jpg')
		
	def test_login2(self):
		self.user_login_verify(username = 'pytest')
		po = login(self.driver)
		self.assertEqual(po.pawd_error_hint(), '密码不能为空')
		function.insert_img(self.driver, 'pawd_empty.jpg')
		
	def test_login3(self):
		self.user_login_verify(password = 'abc123456')
		po = login(self.driver)
		self.assertEqual(po.user_error_hint(), '账号不能为空')
		function.insert_img(self.driver, 'user_empty.jpg')
		
	def test_login4(self):
		character = tandom.choice('zyxwvutsrqponmlkjihgfedcba')
		username = 'zhangesan' + character
		self.user_login_verify(username = username, password = '123456')
		po = login(self.driver)
		self.assertEqual(po.pawd_error_hint(), '密码与账号不匹配')
		function.insert_img(self.driver, 'user_pawd_error.jpg')
		
	def test_login5(self):
		self.user_login_verify(username = 'zhangesan', password = '123456')
		sleep(2)
		po = login(self.driver)
		self.asertEqual(po.user_login_success(), '张三')
		function.insert_img(self.driver, 'user_pawd_ture.jpg')
		
if __name__ = '__main__':
	unittest.main()