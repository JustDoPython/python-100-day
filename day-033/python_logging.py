import logging

#　打印日志级别
def test():
    logging.basicConfig(level=logging.DEBUG)
    logging.debug('Python debug')
    logging.info('Python info')
    logging.warning('Python warning')
    logging.error('Python Error')
    logging.critical('Python critical')

test()

# 记录可变数据
logging.warning('%s before you %s', 'Look', 'leap!')







