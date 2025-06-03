import logging
import os
from fileinput import filename
from logging.handlers import TimedRotatingFileHandler
import time
"""
步骤分析
1.创建记录器级别
2.配置日子记录器级别
3.配置日志记录器的输出格式
4.创建并且添加日志记录hander
5.创建并且添加日志记录器文件
6.对外提供日志记录器

#有bug，设置了backupCount=3,但是无法自动删除日志。会一直叠加log.txt 的数量

"""
import time
# t = time.strftime("%Y-%m-%d", time.localtime())
# 配置日志存放的路径
path = os.path.dirname(os.path.dirname(__file__)) + "/testLog"


# path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testLog")

def log():
    # if not os.path.exists(path):
    #     os.makedirs(path)
    #创建日志记录器
    logger = logging.getLogger("test")
    #配置日志记录器级别
    logger.setLevel(logging.DEBUG)
    #配置日志记录器的输出格式
    format1 = logging.Formatter(
        "日志:%(asctime)s - 级别:%(levelname)s - %(message)s")
    # #创建并且添加日志记录器
    sh = logging.StreamHandler()
    sh.setFormatter(format1)

    logger.addHandler(sh)
    fh = TimedRotatingFileHandler(
        # filename=path + "/log.txt",
        filename=path + "/log.ini",
        when='S',
        encoding='utf-8',
        backupCount=5,

        interval=1,
        utc=False
    )
    fh.suffix = "%Y-%m-%d-%H-%M-%S"  # 文件名后缀格式
    fh.setFormatter(format1)
    logger.addHandler(fh)
    return logger

#单例模式
# logger = log()

if __name__ == '__main__':

    log = log()
    log.info("我是info22")
    log.debug("debug")
    log.error("error")
    log.warning("warning")
    log.critical("critical")
    # for i in range(6):
    #     log.debug("我是")
    #
    #     time.sleep(1)
    # import os
    # os.remove("D:/py_code/pp5/testLog/log.txt.2025-03-03_06-37-03")  # 看是否能正常删除

