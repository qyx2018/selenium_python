import unittest
import time
from HTMLTestRunner import HTMLTestRunner 
import test_baidu
import test_youdao

testunit = unittest.TestSuite()
testunit.addTest(test_baidu.MyTest('test_baidu'))
testunit.addTest(test_youdao.MyTest('test_youdao'))

now = time.strftime('%Y-%m-%d %H_%M_%S')

filename = './' + now + 'result.html'

fp = open(filename, 'wb')
runner = HTMLTestRunner(stream = fp, title = '测试报告', description = '用例执行情况: ')

runner.run(testunit)
fp.close()