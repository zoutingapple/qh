#coding=utf-8
import sys
sys.path.append('F:\workspace\qh')

import unittest
from test_case.models import function, myunit
from test_case.page_obj.update_personal_page import  UpdatePersonal

class UpdatePersonalTest(myunit.MyTest):
    
   
    '''   
    def test_update_head_portrait(self):
        update_personal = UpdatePersonal(self.driver)
        update_personal.update_head_portrait()
        update_personal.update_nickname()
    '''    
    def test_update_nickname(self):
        update_personal = UpdatePersonal(self.driver)
        update_personal.update_nickname()

if __name__ == "__main__":
    unittest.main()

