#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""

from selenium import webdriver

# 声明浏览器对象
driver = webdriver.Chrome()
# 访问页面
driver.get("http://www.baidu.com")