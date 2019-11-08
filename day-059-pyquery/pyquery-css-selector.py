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
            <li class="li1">五星</li>
            <li class="li2">红旗</li>
            <li class="li3">迎风飘扬</li>
        </ul>
    </body>
</html>
"""

doc = pq(html)
print(type(doc('#container')))
print(doc('#container'))

print(type(doc('.li2')))
print(doc('.li2'))


print(doc('html #container'))

li2 = doc('.li2')
li2.css('font-size', '18px')
print(li2)

