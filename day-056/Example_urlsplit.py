# 解析并输出 url 中每个字段的字符串，params 会合并到 path 中。
import urllib
url = 'http://www.baidu.com/urllib.parse.html;python?kw=urllib.parse#modul-urllib'
result = urllib.parse.urlsplit(url)
print(result)
print(result.scheme, result.netloc, result.path, result.query, result.fragment, sep = '\n')