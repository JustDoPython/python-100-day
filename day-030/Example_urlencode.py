# 创建 GET 请求
import urllib
params = {'username':'xxx','password':'123'}
base_url='http://www.baidu.com'
url=base_url + '?' + urllib.parse.urlencode(params)
print(url)
params = {'username':['xxx', 'yyy'], 'password':'123'} # username 键对应多个值
base_url='http://www.baidu.com'
url=base_url + '?' + urllib.parse.urlencode(params) # doseq 设置为 False，会解析成乱码
print(url)
url=base_url + '?' + urllib.parse.urlencode(params, True) # doseq 设置为 True
print(url)