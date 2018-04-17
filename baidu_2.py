from selenium import webdriver

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys('selenium')

driver.find_element_by_id('kw').send_keys('Keys.BACK_SPACE')

driver.find_element_by_id('kw').send_keys(Keys.SPACE)
driver.find_element_by_id('kw').send_keys('教程')

driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')

driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')

driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'v')

driver.find_element_by_id('su').send_keys(Keys.ENTER)

driver.quit()
