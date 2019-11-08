#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""

from selenium import webdriver

# 声明浏览器对象
driver = webdriver.Chrome()

# 访问百度
driver.get("http://www.baidu.com")

# 获取当前的cookie
print(driver.get_cookies())

# 添加cookie
driver.add_cookie({'name': 'mycookie', 'value': 'world'})

# 获取设置的cookie
print(driver.get_cookie('mycookie'))

# 删除设置的cookie
driver.delete_cookie('mycookie')

# 再次获取设置的cookie
print(driver.get_cookie('mycookie'))

# 清除所有cookie
driver.delete_all_cookies()

# 再次获取cookie
print(driver.get_cookies())

# 退出
driver.close()



