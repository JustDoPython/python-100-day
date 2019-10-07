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

#获取li2的class属性值
print(doc('.li2').attr('class'))

#获取li2的文本
print(doc('.li2').text())

#获取html标签下面的所有文本
print(doc('html').text())


#排除部分标签文本
tag = doc('html')
tag.remove('title')
print(tag.text())

