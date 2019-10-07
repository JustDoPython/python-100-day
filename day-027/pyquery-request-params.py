#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""
from pyquery import PyQuery as pq

cookies = {'Cookie':'cookie'}
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

response = pq(url='https://www.baidu.com',headers=headers,cookies=cookies)
print(response)




