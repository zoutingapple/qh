#coding=utf-8

import os
import sys
sys.path.append('F:\workspace\qh')
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
# from test_case import login_test 

case_path = "./test_case"
result = "./report/"
 

def Creatsuite():
    #定义单元测试容器
    testunit = unittest.TestSuite()
    #定搜索用例文件的方法
    discover = unittest.defaultTestLoader.discover(case_path, pattern='*_test.py', top_level_dir=None)
    #将测试用例加入测试容器中
    for test_suite in discover:
        for casename in test_suite:
            testunit.addTests(casename)
    return testunit
 
test_case = Creatsuite()
 
#获取系统当前时间
now = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
  
#定义个报告存放路径，支持相对路径
tdresult = result + day
if os.path.exists(tdresult):
    filename = tdresult + "/" + now + "_result.html"
    fp = open(filename, 'wb')
    #定义测试报告
    runner = HTMLTestRunner(stream=fp, title='Appium测试报告', description='用例详情：')
    #运行测试用例
    runner.run(test_case)
    fp.close()  #关闭报告文件
else:
    os.mkdir(tdresult)
    filename = tdresult + "/" + now + "_result.html"
    fp = open(filename, 'wb')
    #定义测试报告
    runner = HTMLTestRunner(stream=fp, title='Appium测试报告', description='用例详情：')
    #运行测试用例
    runner.run(test_case)
    fp.close()  #关闭报告文件



