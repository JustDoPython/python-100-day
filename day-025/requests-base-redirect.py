#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""
import requests

r = requests.get('http://github.com')
print(r.url)
print(r.status_code)
print(r.history)

r = requests.get('http://github.com', allow_redirects=False)
print(r.status_code)
print(r.history)