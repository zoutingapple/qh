#coding=utf-8
'''
Created on 2016-5-16

@author: zou_yanping
'''
import os
import time
import sys
from asyncio.log import logger
sys.path.append('F:\workspace\qh')
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from test_case.models.log import FinalLogger

class BasePage(object):
    '''
          页面基础类，用于所有页面的继承
    '''
    desired_caps = {'platformName' : 'Android',
                    'platformVersion' : '4.3',
                    'deviceName' : '5fd2f4af',
                    'appPackage' : 'com.royal.qh',
                    'appActivity' :'com.royal.qh.activity.SplashActivity',
                    'unicodeKeyboard': True,
                    'resetKeyboard': True              
    }
    
    def __init__(self, appium_driver):
        self.driver = appium_driver
    
        
    #重新封装单个元素定位方法
    def find_element(self, *loc):
        try:
            return self.driver.find_element(*loc)
        except AttributeError as e:
            logger.error(str(e))
            print('页面找不到 %s' %e)
    
    #定位封装一组元素的方法
    def find_elements(self, *loc):
        try:
            if len(self.driver.find_elemnts(*loc)):
                return self.driver.find_elemnts(*loc)
        except AttributeError as e:
            logger.error(str(e))
            print('页面找不到 %s' %e)


    #重新封装按钮点击方法
    def click_button(self, *loc):
        try:
            self.find_element(*loc).click()
        except AttributeError as e:
            logger.error(str(e))
            print('页面找不到 %s' %e)
            
            
    def wait_activity(self, *loc):
        try:
            return self.driver.wait_activity(*loc)
        except AttributeError as e:
            logger.error(str(e))
            print('页面找不到 %s' %e)
            
    def execute_script(self, *loc):
        try:
            return self.driver.execute_script(*loc)
        except AttributeError as e:
            logger.error(str(e))
            print('execute_script %s' %e)
            
    def swipe(self, *loc):
        try:
            return self.driver.swipe(*loc)
        except AttributeError as e:
            logger.error(str(e))
            print('swipe %s' %e)
            
    def keyevent(self, *loc):
        self.driver.keyevent(*loc)
         
            
            
            
            
            
    