# 基于 url 对 base_url 进行重新组合，并输出组合结果。
import urllib
base_url = 'http://www.baidu.com'
url = 'https://www.google.com/urllib.parse.html;python?kw=urllib.parse#module-urllib'
result = urllib.parse.urljoin(base_url,url,False)
print(result)