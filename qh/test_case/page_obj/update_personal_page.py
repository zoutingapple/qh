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

class UpdatePersonal(BasePage):
    '''修改个人信息 '''

    #Action
    #我按钮
    my_loc = (By.ID, 'com.royal.qh:id/personal_center_icon_iv')
    #头像图标
    user_headpic_loc = (By.ID, 'com.royal.qh:id/fg_user_headpic_iv')
    #点击更改头像
    headpic_layout_loc = (By.ID,"com.royal.qh:id/headpic_layout")
    #取消头像修改
    headpic_cancel_loc = (By.ID,"com.royal.qh:id/btn_cancel")
    #取消头像修改
    album_select_loc = (By.NAME,"从相册选择")
    #选取头像之后，点击保存
    headpic_save_loc = (By.ID,"com.sec.android.gallery3d:id/save")
    #选取拍照
    take_photo_loc = (By.ID,"com.royal.qh:id/btn_take_photo")
    #拍完照之后，点击存储
    photo_save_loc = (By.ID,"com.sec.android.app.camera:id/save")
    #拍完之后点击放弃,不保存照片
    photo_giveup_loc = (By.ID,'com.sec.android.app.camera:id/discard')
    #点击完成保存本次头像修改
    finish_headpic_update_loc = (By.ID,'com.sec.android.gallery3d:id/gl_root_view')
    #区域选取
    select_partimg_loc = (By.ID, 'com.sec.android.gallery3d:id/save')
    
    
    '''修改昵称Action'''
    #点击昵称
    nickname_loc = (By.NAME,"昵 称")
    #修改昵称输入文本框
    nickname_et_loc = (By.ID, "com.royal.qh:id/nickname_et")
    #确认修改昵称   
    confirm_nickname_update_loc = (By.ID, 'com.royal.qh:id/confirm_bt')
    
    
    
    '''点击我的，点击头像图标'''
    def common_operate(self):
        sleep(2)
        self.click_button(*self.my_loc)
        sleep(1)
        self.click_button(*self.user_headpic_loc)
        sleep(1)
    
    def update_nickname(self):
        self.common_operate()
        sleep(5)
        self.click_button(*self.nickname_loc)
        sleep(2)
        nickname = self.find_element(*self.nickname_et_loc)
        nickname.click()
        nickname.clear()
        nickname.send_keys('轻侯')
#         self.keyevent(4)
        sleep(2)
        self.click_button(*self.confirm_nickname_update_loc)
        
    
    def update_head_portrait(self):
        '''修改头像'''
        self.common_operate()
        self.click_button(*self.headpic_layout_loc) 
        image_select = 1
        if image_select == 0:
            #取消
            self.click_button(*self.headpic_cancel_loc)
        if image_select == 1:
            #从相册选择
            self.click_button(*self.album_select_loc)
            #开启相册app应用
#             self.driver = connect_appium()
            self.wait_activity("com.sec.android.app.collage", 10)
            #选择某个相册
            self.execute_script("mobile: tap", {"touchCount":"1", "x":888, "y":320})
            sleep(5)
            #点击选中相册
            self.execute_script("mobile: tap", {"touchCount":"1", "x":450, "y":436})
            sleep(5)
            #选中图片部分
            self.swipe(854,1348,1035,1528,1000)
            sleep(5)
            self.swipe(222,737,37,525,1000)
            sleep(5)
            #点击完成,选取图片
            self.click_button(*self.headpic_save_loc)
            
            sleep(5)
        if image_select == 2:
            self.click_button(*self.take_photo_loc)
            #等待相机开启
            self.wait_activity("com.sec.android.app.camera", 10)
            sleep(5)
            #点击拍照键进行拍照
            self.keyevent(27)
            sleep(7)
            #拍完之后点击存储
            save = True
            if save:
                self.click_button(*self.photo_save_loc)
            else:
                #拍完之后点击放弃,不保存照片
                self.click_button(*self.photo_giveup_loc)
                save = True
            #点击完成保存本次头像修改
            sleep(5)
            self.click_button(*self.finish_headpic_update_loc)
            #区域选取
            sleep(5)
            self.click_button(*self.select_partimg_loc)
    
    
















