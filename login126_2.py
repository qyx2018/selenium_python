from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.126.com')

print('Before login ==========================')

title = driver.title
print(title)

now_url = driver.current_url
print(now_url)

driver.find_element_by_id('idInput').clear()
driver.find_element_by_id('idInput').send_keys('username')
driver.find_element_by_id('pwdInput').clear()
driver.find_element_by_id('pwdInput').send_keys('password')
driver.find_element_by_id('loginBtn').click()
time.sleep(5)

print('After login ===========================')

title = driver.title
print(title)

now_url = driver.current_url
print(now_url)

user = driver.find_element_by_id('spnUid').text
print(user)

driver.quit()