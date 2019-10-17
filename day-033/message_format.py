import logging
#　更改显示消息的格式
logging.basicConfig(format='%(levelname)s:%(message)s',level=logging.DEBUG)
logging.debug('Python message format Debug')
logging.info('Python message format Info')
logging.warning('Python message format Warning')