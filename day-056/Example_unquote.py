# 解码经过 quote 函数处理后的 url，输出解码后的结果。
import urllib
url = 'http://www.baidu.com/爬虫'
result = urllib.parse.quote(url)
print(result)
result = urllib.parse.unquote(url)
print(result)