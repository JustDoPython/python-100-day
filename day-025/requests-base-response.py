#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""
###改变编码###
import requests
r = requests.get('http://www.baidu.com')
print(r.text)

print(r.encoding)

r.encoding = 'Unicode'
print(r.text)



###二进制返回###
import requests
from PIL import Image
from io import BytesIO

r = requests.get('http://img.sccnn.com/bimg/326/203.jpg')
print(r.content)
bi = BytesIO(r.content)
print(bi)
i = Image.open(bi)
print(i)



###JSON返回###
import requests

r = requests.get('https://www.baidu.com')
print(r.json())









