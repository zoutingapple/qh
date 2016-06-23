
#执行
运行run_qh_test.py点击Run As-->Python unit-test

##目录介绍：

* command 目录用来存储 上传测试报告、发送报告邮件等脚本。

* data目录用来存储  数据文件

* report 目录用来存储HTML测试报告，下面创建了image目录用于存放测试过程中的截图

* test_case 测试用例目录，用于存放测试数据及相关模块

* test_case\page_obj 目录用来存放操作的Page页面（BasePage+各个页面脚本）

* test_case\models 目录用来存放公共方法及公共类

* *_test.py 测试用例文件，根据测试文件匹配规则，以*_sta.py命名的文件被当作自动化测试用例执行

* data/login.log日志记录文件

* models/log.py  日志配置文件 

**【拉下代码后，运行qh\run_qh_test.py 运行demo。可在report目录下查看测试报告】**


http://www.jb51.net/article/42626.htm 日志管理
