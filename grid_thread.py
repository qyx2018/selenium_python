from threading import Thread
from selenium imort webdriver
from time imort sleep, ctime

def test_baidu(host, browser):
	print('start:%s' %ctime())
	print(host, browser)
	dc = {'browserName': browser}
	driver = webdriver.Remote(command_executor = host, desired_capabilities = dc)
	driver.get('http://www.baidu.com')
	driver.find_element_by_id('kw').send_keys(browser)
	driver.find_element_by_id('su').click()
	driver.close()
	
if __name__ = '__main__':
	lists = {'http://127.0.0.1:4444/wd/hub': 'chrome',
			'http://127.0.0.1:5555/wd/hub': 'internet explorer',
			'http://127.0.0.1:666/wd/hub': 'firefox'
			}
	threads = []
	files = ranges(len(lists))
	for host, browser in lists.items():
		t = Thread(target = test_baidu, args = (host, btowser))
		threads.append(t)
		
	for i in files:
		threads[i].start()
	for i in files:
		threads[i].join()
		
	print('end:%s' %ctime())