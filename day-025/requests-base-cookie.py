#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""
import requests

jar = requests.cookies.RequestsCookieJar()
#为路径/cookies设置cookie
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
#为路径/elsewhere设置cookie
jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
#请求路径为/cookies的URL
url = 'http://httpbin.org/cookies'
r = requests.get(url, cookies=jar)
print(r.text)



url = 'http://example.com'
r = requests.get(url)
print(r.cookies)
print(r.cookies['example_cookie_name'])


cookies = dict(cookies_are='working')
r = requests.get('http://httpbin.org/cookies', cookies=cookies)
print(r.text)


