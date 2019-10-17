
import logging
# 日志信息记录到指定的文件中
logging.basicConfig(filename='F:/example.log', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')