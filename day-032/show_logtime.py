import logging
# 显示消息时间
logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning('is when this event was logged.')

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when this event was logged.')