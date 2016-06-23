'''
Created on 2016年5月17日

@author: zou_yanping
'''
import sys
sys.path.append('F:\workspace\qh')
import os
from unittest.case import skip
import unittest
from test_case.models.log import FinalLogger

from test_case.models import function, myunit
from test_case.page_obj.login_page import Login
from test_case.models.driver import connect_appium
from time import sleep
from test_case.models.login_excel import LoginExcel
from test_case.models.swipe_to import SwipeTo

class LoginTest(myunit.MyTest):
    '''登录测试'''
    file_path = str(os.getcwd()).split('\\test_case')
    
    log_file = file_path[0] + '/data/login.log'
    
    excel_file = file_path[0] + '/data/userlogin.xlsx'
    
    logger = FinalLogger().getLogger(log_file)
   
    """
    #测试用户登录
    def user_login_verity(self, username, password):
        self.logger.info('user_login_verity username------ %s' %username)
        Login(self.driver).user_login(username, password)
        
    def test_login1(self):
        login = Login(self.driver)
        wizard_page_element = login.wizard_page()
        if wizard_page_element.is_displayed():
            '''
            wizard_page_element.is_displayed()判读是否第一次运行app进行向导页滑动
            '''
            SwipeTo(self.driver).swipe_left()
            login.enter_iv()
        login.qh_login()
        self.driver.implicitly_wait(8)
        login_excel_list = LoginExcel().excel_table_byname(
                                    file=str(self.excel_file), 
                                    colnameindex=0, 
                                    by_name='userlogin')
        for i in range(len(login_excel_list)):
            username = login_excel_list[i]['username']
            self.logger.info("=================username======================")
            self.logger.info(username)
            password = login_excel_list[i]['password']
            self.logger.info("==================password=============================")
            self.logger.info(password)
            self.user_login_verity(username, password)
            screen_img_name = 'login_'+str(username)+'.png'
            #调用login.user_login_succ()判断是否登录成功进入找桩界面
            login_succ_element = login.user_login_succ()
            if self.assertTrue(login_succ_element.is_displayed()):
                self.logger.info('login succ %s' %username)
                function.insert_screen_img(self.driver, screen_img_name)
            else:
                self.logger.info('login fail %s' %username)
                function.insert_screen_img(self.driver, screen_img_name)
#     
# if __name__ == "__main__":
#     unittest.main()
"""