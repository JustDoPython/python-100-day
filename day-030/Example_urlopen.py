# 创建一个 HTTP GET 请求，输出响应上下文
from urllib.request import urlopen
response = urlopen("http://www.python.org")
print(response.read()) 

# 创建一个 HTTP POST 请求，输出响应上下文
from urllib.request import urlopen
from urllib.parse import urlencode
data = {'kw' : 'python'}
data = bytes(urlencode(data), encoding = 'utf-8')
response = urlopen("https://fanyi.baidu.com/sug", data)
print(response.read().decode('unicode_escape'))

# 创建一个 HTTP GET 请求，设置超时时间为0.1s
import urllib.request
import urllib.error
try:
    response=urllib.request.urlopen('http://www.python.org',timeout=0.1)
    print(response.read()) 
except urllib.error.URLError as e:
    print(e.reason)