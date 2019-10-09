import urllib
dataList = ['http', 'www.baidu.com', '/urllib.parse.html', 'python', 'kw=urllib.parse', 'modul-urllib'] # 六个字符串都必须填写，否则会出现 ValueError 错误，如果某一字符串不存在则填入空字符
dataTuple = ('http', 'www.baidu.com', '/urllib.parse.html', '', 'kw=urllib.parse', 'modul-urllib') # 六个字符串都必须填写，否则会出现 ValueError 错误，如果某一字符串不存在则填入空字符
urlList = urllib.parse.urlunparse(dataList)
urlTuple = urllib.parse.urlunparse(dataTuple)
print('1.urlList:%s\n2.urlTuple:%s' % (urlList, urlTuple))