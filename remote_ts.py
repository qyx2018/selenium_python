from selenium.webdriver import remote

driver = Remote(command_executor = 'http://127.0.0.1:4444/wb/hub', 
				desired_capabilities = {'platform': 'ANY',
										'btowserNmae': 'chrome',
										'version': '',
										'javascriptEnabled': True
										}
				)
				
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('remote')
driver.find_element_by_id('su').click()

driver.quit()