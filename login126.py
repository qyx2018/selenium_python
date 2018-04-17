from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.126.com')

driver.find_element_by_xpath(".//*[@id='auto-id-1512119385760']").clear()
driver.find_element_by_xpath(".//*[@id='auto-id-1512119385760']").send_keys('username')
driver.find_element_by_id('auto-id-1512119385761').clear()
driver.find_element_by_id('auto-id-1512119385761').send_keys('password')
driver.find_element_by_id('dologin').click()

#driver.quit()