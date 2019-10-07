#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""
import requests

# 发送请求
response = requests.get(url="http://www.baidu.com/s", params={'wd':'python'})
# 处理响应
print(response.status_code)