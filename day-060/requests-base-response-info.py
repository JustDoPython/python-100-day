#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""
import requests

url = 'http://www.baidu.com'
headers = {'User-Agent': 'myagent/2.21.0'}
r = requests.get(url, headers=headers)
print(r.request.headers)

