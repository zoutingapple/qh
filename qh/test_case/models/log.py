#coding=utf-8
'''开发一个日志系统， 既要把日志输出到控制台， 还要写入日志文件 '''
import logging.handlers
import sys
import os
sys.path.append('F:\workspace\qh')
 
class FinalLogger:
 
     file_path = str(os.getcwd()).split('\\test_case')
     log_file = file_path[0] + '/'+'data/login.log'
     logger = None
     
     levels = {"n" : logging.NOTSET,
      "d" : logging.DEBUG,
      "i" : logging.INFO,
      "w" : logging.WARN,
      "e" : logging.ERROR,
      "c" : logging.CRITICAL}
     
     log_level = "d"
     log_max_byte = 10 * 1024 * 1024;
     log_backup_count = 5
     
     @staticmethod
     def getLogger(log_file):
      if FinalLogger.logger is not None:
       return FinalLogger.logger
     
      FinalLogger.logger = logging.Logger("oggingmodule.FinalLogger")
      log_handler = logging.handlers.RotatingFileHandler(filename = FinalLogger.log_file,\
      maxBytes = FinalLogger.log_max_byte,\
      backupCount = FinalLogger.log_backup_count)
      log_fmt = logging.Formatter("[%(levelname)s][%(funcName)s][%(asctime)s]%(message)s")
      log_handler.setFormatter(log_fmt)
      FinalLogger.logger.addHandler(log_handler)
      FinalLogger.logger.setLevel(FinalLogger.levels.get(FinalLogger.log_level))
      return FinalLogger.logger
  
if __name__ == "__main__":
 logger = FinalLogger.getLogger(log_file)
 name = 'zhangdanlisi ==='
 logger.debug(name)
 logger.info("this is a info msg!")
 logger.warn("this is a warn msg!")
 logger.error("this is a error msg!")
 logger.critical("this is a critical msg!")
