#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""
import urllib.parse
import urllib.request

url = "http://www.baidu.com/s"
params = urllib.parse.urlencode({'wd':'python'})
# 发送请求
response = urllib.request.urlopen('?'.join([url, params]))
# 处理响应
print(response.getcode())

