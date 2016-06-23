# -*- coding = utf-8 -*-  
from appium import webdriver
import time
class SwipeTo:
    '''
        手机引导页滑动，以手机1080*1920为例,width=x=1080,heignt=y=1920
        将x轴划分为20等分,网左边滑动，x轴起点>x轴终点，y轴不变，x轴起点定为900，即width/10*9,终点为width/20,y轴为heignt/5
    '''
    def __init__(self, appium_driver):
        self.driver = appium_driver
         
    def swipe_left(self,times = 3):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        start_x = int(width/10*9)
        start_y = height/5
        end_x = int(width/20)
        end_y = height/5
        for x in range(times):
            self.driver.swipe(start_x, start_y, end_x, end_y, duration=1000)
            time.sleep(1)
        
        
    def swipe_right(self,times = 3):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        start_x = int(width/20)
        start_y = height/5
        end_x = int(width/10*9)
        end_y = height/5
        for x in range(times):
            self.driver.swipe(start_x, start_y, end_x, end_y, duration=1000)
            time.sleep(1)
