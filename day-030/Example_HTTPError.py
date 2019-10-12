# 返回401未授权错误
from urllib import request,error
try:
    response=request.urlopen('http://pythonscraping.com/pages/auth/login.php')
    print(response.getcode())
except error.HTTPError as e:
    print('1.错误原因：\n%s\n2.状态码：\n%s\n3.响应头信息：\n%s' %(e.reason, e.code, e.headers))
except error.URLError as e:
    print(e.reason)