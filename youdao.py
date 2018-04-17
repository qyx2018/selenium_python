from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.youdao.com')

driver.find_element_by_id('translateContent').send_keys('hello')

driver.find_element_by_id('translateContent').submit()

#driver.quit()