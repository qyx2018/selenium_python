from selenium import webdriver
import os, time

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('checkbox.html')
driver.get(file_path)

checkboxes = driver.find_elements_by_css_selector('input[type = checkbox]')
for checkbox in checkboxes:
	checkbox.click()
	time.sleep(1)
	
print(len(checkboxes))

driver.find_elements_by_css_selector('input[type = checkbox]').pop().click()

driver.quit()