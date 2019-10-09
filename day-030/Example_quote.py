# 采用 quote 对 url 中的汉字进行编码，输出编码后的结果
import urllib
url = 'http://www.baidu.com/爬虫'
result = urllib.parse.quote(url)
print(result)
url = 'http://www.baidu.com/+爬虫'
result = urllib.parse.quote(url, '+') # 更改 safe 参数
print(result)