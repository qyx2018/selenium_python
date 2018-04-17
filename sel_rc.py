from selenium import selenium

sel = selenium('localhost', 4444, '*Chrome', 'http://www.baidu.com')

sel.open('/')
sel.type('id = kw', 'selenium grid')
sel.click('id = su')
sel.wait_for_page_to_load('30000')

sel.stop()