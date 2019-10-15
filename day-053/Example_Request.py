# 采用 HTTP GET 请求的方法模拟谷歌浏览器访问网站，输出响应上下文
from urllib import request,parse
url = 'http://www.python.org'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
req = request.Request(url, headers = headers, method = 'GET')
response = request.urlopen(req) 
print(response.read())

# 采用 HTTP POST 请求的方法模拟谷歌浏览器访问网站，输出响应上下文
from urllib import request
from urllib import parse
url = 'https://fanyi.baidu.com/sug'
data = {'kw' : 'python'}
data = bytes(parse.urlencode(data), encoding = 'utf-8')
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
req = request.Request(url, data, headers, method = 'POST')
response = request.urlopen(req) 
print(response.read().decode('unicode_escape'))

# 创建一个 HTTP GET 请求，通过 add_header 添加一个 UserAgent
import urllib.request
import random
url = 'http://www.python.org'
headerUserAgentList = ['Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0']
randomHeaderUserAgent = random.choice(headerUserAgentList) # 随机选取一个 UserAgent
req = urllib.request.Request(url) 
req.add_header('User-Agent', randomHeaderUserAgent) # 添加 UserAgent
response=urllib.request.urlopen(req)
print(req.get_header('User-agent'))
print(req.headers) # 打印请求的 header 信息
