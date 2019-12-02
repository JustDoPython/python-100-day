#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""
import requests

r = requests.post('http://httpbin.org/post', data = {'key':'value'})
print(r.text)

r = requests.post('http://httpbin.org/post', params = {'key':'value'})
print(r.text)

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)


payload = (('key1', 'value1'), ('key1', 'value2'))
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)

payload = {'some': 'data'}
r = requests.post("http://httpbin.org/post", json=payload)
print(r.text)

files = {'file': open('test.txt', 'rb')}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)


files = {'file': ('test.txt', 'some,data,to,send\nanother,row,to,send\n')}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)




