from selenium.webdriver import remote

lists = {'http://127.0.0.1:4444/wd/hub': 'chrome',
		'http://127.0.0.1:5555/wd/hub': 'firefox',
		'http://127.0.0.1:6666/wd/hub': 'internet explorer'}

for host, browser in lists.items():
	print(host, browser)
	driver = Remote(command_executor = host, 
				desired_capabilities = {'platform': 'ANY',
										'btowserNmae': browser,
										'version': '',
										'javascriptEnabled': True
										}
				)
				
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('remote')
driver.find_element_by_id('su').click()

driver.close()