#coding=utf-8
import configparser, itertools
import sys

from appium import webdriver


sys.path.append('F:\workspace\qh')

class WDConner:
    def __init__(self, config_file_path):
        self.file_path = config_file_path
        
    def test(self, config_file_path):
        
        cf = configparser.ConfigParser()
        
        cf.sections()
        
        cf.read(config_file_path,encoding="utf-8-sig")
        
        print("===========================================")
        
        desired_caps = {}
            
        appium_server_ip = cf.get("GalaxyS4", "appium_server_ip")
        print(appium_server_ip)
        
        appium_server_port = cf.get("Galaxy S4", "appium_server_port")
            
        desired_caps['platformName'] = cf.get("Galaxy S4",'OS_type') #测试手机的系统类型
            
        desired_caps['platformVersion'] =  cf.get("Galaxy S4",'OS_version') #该手机系统的版本号
            
        desired_caps['deviceName'] = cf.get("Galaxy S4",'deviceName') #该手机的deviceName,Android请用adb devices查询
            
        desired_caps['app'] =  cf.get("Galaxy S4",'app') #本地apk或者ipa的绝对路径，如果iPhone上安装了app，则为bundle ID
            
        desired_caps['udid'] =  cf.get("Galaxy S4",'udid') #iphone的udid，通过iTunes查找
            
        desired_caps['automationName'] = cf.get('android_config','automationName') #选择测试引擎
                
        desired_caps['appPackage'] = cf.get('android_config','appPackage') #app的包名，可以咨询开发
              
        desired_caps['appActivity'] = cf.get('android_config','appActivity') #咨询开发
              
#         self.driver = webdriver.Remote('http://%s:%s/wd/hub' % (appium_server_ip,appium_server_port), desired_caps)    
        
if __name__ == "__main__":
    print('=================start==========================')
    wdc = WDConner('../data/params_config.ini')
    wdc.test('../data/params_config.ini')
        
        