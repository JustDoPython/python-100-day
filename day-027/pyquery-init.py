#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""
from pyquery import PyQuery as pq


###初始化HTML字符串###
html = """
<html>
    <head>
        我爱我的祖国
        <title>China</title>
    </head>
    <body>
        <ul id="container">
            <li class="li1">五星</li>
            <li class="li2">红旗</li>
            <li class="li3">迎风飘扬</li>
        </ul>
    </body>
</html>
"""

doc = pq(html)
print(type(doc))
print(doc)


###初始化非HTML字符串###
test = '''
this is a string
this is second row
'''

doc = pq(test)
print(type(doc))
print(doc)


###初始化HTML文件###
#filename参数为html文件路径
test_html = pq(filename='test.html')
print(type(test_html))
print(test_html)

###初始化非HTML文件###
test_txt = pq(filename='test.txt')
print(type(test_txt))
print(test_txt)

###初始化网址响应内容###
response = pq(url='https://www.baidu.com')
print(type(response))
print(response)









