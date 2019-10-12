# -*- coding: utf-8 -*-
BOT_NAME = 'peilv'
SPIDER_MODULES = ['peilv.spiders']
NEWSPIDER_MODULE = 'peilv.spiders'
FEED_EXPORT_ENCODING = "gb18030" #解决导出的Excel文件中文乱码问题
user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
FEED_URI = 'file:///e:/PythonLearn/Python learning/peilv/BaseData.csv'
FEED_FORMAT = 'csv'
FEED_EXPORTERS = {
    'csv': 'peilv.spiders.itemcsvexporter.itemcsvexporter',
}  # 这里你的project名字为peilv
FIELDS_TO_EXPORT = [
    'cc',#比赛场次
    'li',#立博的赔率
    'b5',#bet365的赔率
   ]
ROBOTSTXT_OBEY = False #当用cookies时候要设置为false
DOWNLOADER_MIDDLEWARES = {
'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
}
HTTPERROR_ALLOWED_CODES = [403]
