#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""
from pyquery import PyQuery as pq

html = """
<html>
    <head>
        我爱我的祖国
        <title>China</title>
    </head>
    <body>
        <ul id="container">
            <li class="li1">五星啊</li>
            <li class="li2">红旗</li>
            <li class="li3">迎风飘扬啊</li>
        </ul>
    </body>
</html>
"""

pseudo_doc = pq(html)
print(pseudo_doc('li:nth-child(2)'))
#打印第一个li标签
print(pseudo_doc('li:first-child'))
#打印最后一个标签
print(pseudo_doc('li:last-child'))

#找到含有Python的li标签
print(pseudo_doc("li:contains('五星')"))

#找到含有好的li标签
print(pseudo_doc("li:contains('红')"))

#找到含有啊的li标签
print(pseudo_doc("li:contains('啊')"))



