# 在请求连接时候捕获网址错误引发的异常
from urllib import request, error
try:
    response = request.urlopen('https://www,baidu,com')
except error.URLError as e:
    print(e.reason)