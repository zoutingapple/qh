#coding=utf-8
'''
Created on 2016年5月17日

@author: zou_yanping
'''

'''截图保存'''
import sys
sys.path.append('F:\workspace\qh')
import os
import time

from appium import webdriver

from test_case.page_obj.base_page import BasePage


sys.path.append('F:\workspace\qh')

local_time = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))

day = time.strftime('%Y-%m-%d', time.localtime(time.time()))

def insert_screen_img(driver, file_name):
    '''
        os.path.dirname（）返回文件路径
    '''
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    print(base_dir)
    print(base_dir.split('/test_case'))
    print('=================')
    base = base_dir.split('/test_case')[0]
    file_path = base + '/report/image/' + day 
    filename = file_path + '/' + local_time + file_name
    if(os.path.exists(file_path)):
        return driver.get_screenshot_as_file(filename)
    else:
        os.makedirs(file_path)
        return driver.get_screenshot_as_file(filename)
        
    
if __name__ == "__main__":
    print('yoyoyo')
    driver = webdriver.Remote('http://localhost:4723/wd/hub', BasePage.desired_caps)
    
    insert_screen_img(driver, '_error.png')
    time.sleep(15)
#     saveScreenshot(driver, '_error.png')
    driver.quit()