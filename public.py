class Login():

	def user_login(self, driver):
		driver.find_element_by_id('auto-id-1513836365962').clear()
		driver.find_element_by_id('auto-id-1513836365962').send_keys('username')
		driver.find_element_by_id('pwdInput').clear()
		driver.find_element_by_id('pwdInput').send_keys('password')
		driver.find_element_by_id('loginBtn').click()
		
	def user_logout(self, driver):
		driver.find_element_by_link_text('退出').click()
		driver.quit()

