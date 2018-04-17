from selenium import webdriver
import time
import os

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('frame.html')
driver.get(file_path)

driver.switch_to.frame('if')

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
time.sleep(3)

driver.quit()
