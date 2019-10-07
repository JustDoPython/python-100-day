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

doc = pq(html)

#打印id为container的标签
print(doc.find('#container'))


#打印id为container的标签的子标签
container = doc.find('#container')
print(container.children())


#打印id为container的标签的父标签
container = doc.find('#container')
print(container.parent())

#打印class为li2的标签的兄弟标签
li2 = doc.find('.li2')
print(li2.siblings())