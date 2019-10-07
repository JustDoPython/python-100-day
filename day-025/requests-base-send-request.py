#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""
import requests

r = requests.get('https://api.github.com/events')
print(r.status_code)

r = requests.post('http://httpbin.org/post', data = {'key':'value'})
print(r.status_code)

r = requests.put('http://httpbin.org/put', data = {'key':'value'})
print(r.status_code)

r = requests.delete('http://httpbin.org/delete')
print(r.status_code)

r = requests.head('http://httpbin.org/get')
print(r.status_code)

r = requests.options('http://httpbin.org/get')
print(r.status_code)