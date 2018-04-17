from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

driver.set_window_size(700, 600)

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()

js = "window.scrollTo(100, 100)"
driver.execute_script(js)
sleep(3)

driver.quit()