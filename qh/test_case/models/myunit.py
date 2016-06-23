#coding=utf-8
'''
Created on 2016年5月17日

@author: zou_yanping
'''

'''自定义框架测试类'''

import sys 
sys.path.append('F:\workspace\qh')
import unittest
from test_case.models.driver import connect_appium


class MyTest(unittest.TestCase):

    def setUp(self):
        print("Mytest ding yi de =============================")
        self.driver = connect_appium()
        print('self.driver ====%s =' %self.driver)
        self.driver.implicitly_wait(15)  
    
    def tearDown(self):
        self.driver.quit()
        
# if __name__ == "__main__":
#    unittest.main()


