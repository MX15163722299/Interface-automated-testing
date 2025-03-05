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
# 配置日志存放的路径
path = os.path.dirname(os.path.dirname(__file__)) + "/testLog"
def log():
    #创建日志记录器
    logger = logging.getLogger("test")
    #配置日志记录器级别
    logger.setLevel(logging.DEBUG)
    #配置日志记录器的输出格式
    format1 = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s")
    #创建并且添加日志记录器
    sh = logging.StreamHandler()
    sh.setFormatter(format1)

    logger.addHandler(sh)

    fh = TimedRotatingFileHandler(
        filename=path + "/log.txt",
        when='M',
        encoding='utf-8',
        backupCount=3,
        interval=1,
        utc=True
    )
    fh.suffix = "%Y-%m-%d_%H-%M-%S"  # 文件名后缀格式
    fh.setFormatter(format1)

    logger.addHandler(fh)
    return logger


if __name__ == '__main__':

    log = log()
    for i in range(6):
        log.debug("我是")
        time.sleep(1)
    # import os
    # os.remove("D:/py_code/pp5/testLog/log.txt.2025-03-03_06-37-03")  # 看是否能正常删除

