from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.youdao.com')

cookie = driver.get_cookies()
print(cookie)

driver.quit()