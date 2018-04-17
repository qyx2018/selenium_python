from selenium import webdriver
from public import Login

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.126.com')

Login.user_login(driver)

Login.user_logout(driver)