#coding=utf-8
import configparser
from appium import webdriver

class Exmaple:
    def __init__(self):
        pass
    
    def test(self, config_file_path):
        config = configparser.ConfigParser()
        config.sections()
        print(config.sections())
        print("11111111111111111111111111111")
        config.read(config_file_path,encoding="utf-8-sig")
        lists = config.sections()
        print(config.sections())
        appium_server_ip = config.get("Galaxy S4", "appium_server_ip")
        print(appium_server_ip)
        appium_server_port = config.get("Galaxy S4", "appium_server_port")
        print(appium_server_port)
        OS_type = config.get("Galaxy S4", "OS_type")
        print(OS_type)
        OS_version = config.get("Galaxy S4", "OS_version")
        print(OS_version)
        deviceName = config.get("Galaxy S4", "deviceName")
        print(deviceName)
        udid = config.get("Galaxy S4", "udid")
        print(udid)
        app = config.get("Galaxy S4", "app")
        print(app)
        print('=========================================Galaxy S5========================================================')
        
        
        '''Galaxy S5'''
        appium_server_ip_5 = config.get("Galaxy S5", "appium_server_ip")
        appium_server_port_5 = config.get("Galaxy S5", "appium_server_port")
        OS_type = config.get("Galaxy S5", "OS_type")
        OS_version_5 = config.get("Galaxy S5", "OS_version")
        deviceName_5 = config.get("Galaxy S5", "deviceName")
        udid_5 = config.get("Galaxy S5", "udid")
        app_5 = config.get("Galaxy S5", "app")
        desired_caps = {}
        
        desired_caps['platformName'] = config.get("Galaxy S4",'OS_type') #测试手机的系统类型
            
        desired_caps['platformVersion'] =  config.get("Galaxy S4",'OS_version') #该手机系统的版本号
            
        desired_caps['deviceName'] = config.get("Galaxy S4",'deviceName') #该手机的deviceName,Android请用adb devices查询
            
        desired_caps['app'] =  config.get("Galaxy S4",'app') #本地apk或者ipa的绝对路径，如果iPhone上安装了app，则为bundle ID
            
        desired_caps['udid'] =  config.get("Galaxy S4",'udid') #iphone的udid，通过iTunes查找
            
        desired_caps['automationName'] = config.get('android_config','automationName') #选择测试引擎
                
        desired_caps['appPackage'] = config.get('android_config','appPackage') #app的包名，可以咨询开发
              
        desired_caps['appActivity'] = config.get('android_config','appActivity') #咨询开发
              
        self.driver = webdriver.Remote('http://%s:%s/wd/hub' % (appium_server_ip,appium_server_port), desired_caps)    
        
        
        
if __name__ == "__main__":
    exam = Exmaple()
    exam.test('f:\\params_config.ini')





  