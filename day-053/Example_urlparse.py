# 解析并输出 url 中每个字段的字符串
import urllib
url = 'http://www.baidu.com/urllib.parse.html;python?kw=urllib.parse#module-urllib'
result = urllib.parse.urlparse(url)
print(result)
print(result.scheme, result.netloc, result.path, result.params, result.query, result.fragment, sep = '\n')