#coding=utf-8
'''
Created on 2016年5月17日

@author: zou_yanping

'''
'''定义驱动文件'''

import sys
sys.path.append('F:\workspace\qh')

#启动连接appium驱动
from appium import webdriver
from test_case.page_obj.base_page import BasePage 

def connect_appium():
    host = '127.0.0.1:4723'
    url = 'http://' + host + '/wd/hub'
    driver = webdriver.Remote(url, BasePage.desired_caps)
    print('------------>driver.py %s' %driver)
    return driver
