#coding=utf-8
'''
Created on 2016年5月17日

@author: zou_yanping
'''
import sys
sys.path.append('F:\workspace\qh')
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By

from test_case.page_obj.base_page import BasePage

class Login(BasePage):
    '''
          用户登录界面
    '''

    #Action
    #我按钮
    my_loc = (By.ID, 'com.royal.qh:id/personal_center_icon_iv')
    #登录/注册图标
    login_or_regist_loc = (By.ID, 'com.royal.qh:id/fg_user_headpic_iv')
    #退出登录，点击退出
    logout_loc = (By.ID, 'com.royal.qh:id/personal_exit_bt')
#     conform_out_loc = (By.ID, 'com.royal.qh:id/dialog_no_titlebar_cancel_bt')
    #登录用户名定位
    username_loc = (By.ID, 'com.royal.qh:id/user_phone_tv')
    #登录密码定位
    password_loc = (By.ID, 'com.royal.qh:id/login_password_et')
    #登录按钮
    login_loc = (By.ID, 'com.royal.qh:id/login_bt')
    #登录成功，进入找桩界面
    login_succ_loc = (By.ID, 'com.royal.qh:id/top_title')
    #向导页首页
    swize_page_loc = (By.XPATH, '//android.widget.FrameLayout/android.widget.RelativeLayout')
    #点击立即体验
    enter_iv_loc = (By.ID, 'com.royal.qh:id/enter_iv')
    
    def enter_iv(self):
        '''点击立即体验，进入找桩界面'''
        self.click_button(*self.enter_iv_loc) 
    
    def wizard_page(self):
        return self.find_element(*self.swize_page_loc)

    def qh_login(self):
        '''
        step1:点击我
        step2:点击登录/注册按钮
        '''
        sleep(1)
        self.find_element(*self.my_loc).click()
        sleep(1)
        self.click_button(*self.login_or_regist_loc) 
        
    #登录用户名
    def login_username(self, username):
        username_element = self.find_element(*self.username_loc)
        username_element.click()
        username_element.clear()
        username_element.send_keys(username)
        
    #登录密码
    def login_password(self, password):
        password_element = self.find_element(*self.password_loc)
        password_element.click()
        password_element.clear()
        password_element.send_keys(password)
        
    #登录按钮
    def login_button(self):
        self.click_button(*self.login_loc)
  
    #定义统一登录入口
    def user_login(self, username, password):
        '''获取登录的用户名跟密码'''
        self.login_username(username)
        sleep(1)
        self.login_password(password)
        self.driver.keyevent(93) #向下翻页键
        sleep(1)
        self.login_button()
        
        
    #用户名错误提示
    def username_error_hint(self):
        return self.click_button(self.username_error_hint_loc).text
    
    #密码错误提示
    def password_error_hint(self):
        return self.click_button(self.password_error_hint_loc).text
    
    #登录成功提示    
    def user_login_succ(self):
        return self.find_element(*self.login_succ_loc)
    
    
















