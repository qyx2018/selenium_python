from selenium import webdriver

driver = webdriver.Chrome()

first_url = 'http://www.baidu.com'
print('Now access %s' %(first_url))
driver.get(first_url)

second_url = 'http://news.baidu.com'
print('Now access %s' %(second_url))
driver.get(second_url)

print('Back to %s' %(first_url))
driver.back()

print('Forward to %s' %(second_url))
driver.forward()
#driver.quit()