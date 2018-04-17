from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.youdao.com')

driver.add_cookie({'name': 'key-aaaaaaa', 'value': 'value-bbbbbb'})

for cookie in driver.get_cookies():
	print('%s -> %s' %(cookie['name'], cookie['value']))
	
driver.quit()