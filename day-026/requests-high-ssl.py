#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""
import requests
from requests.auth import HTTPBasicAuth

#请将username和password替换成自己在该网站的登录用户名和密码
res = requests.get('http://www.baidu.com', auth=HTTPBasicAuth('username', 'password'))
print(res.status_code)



