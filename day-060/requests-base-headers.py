#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""
import requests

r = requests.get('http://httpbin.org/get')
print(r.status_code)

print(r.status_code == requests.codes.ok)

print(r.headers)

print(r.headers['Content-Encoding'])
