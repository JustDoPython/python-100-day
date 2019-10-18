#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""

from selenium import webdriver

# 设置无窗口
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

# 设置代理
chrome_options.add_argument('--proxy-server=http://{ip}:{port}')

# 声明浏览器对象
driver = webdriver.Chrome(options=chrome_options)

# 访问页面
driver.get("http://www.baidu.com")