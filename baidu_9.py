from selenium import webdriver
import logging

logging.basicConfig(level = logging.DEBUG)
diver = webdriver.Chrome()
diver.get('http://www.baidu.com')

diver.find_element_by_id('kw').send_keys('selenium')
diver.find_element_by_id('su').click()
diver.quit()