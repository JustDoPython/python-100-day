#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: 闲欢
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

# 声明浏览器对象
driver = webdriver.Chrome()
# 访问页面
driver.get("http://www.baidu.com")

# 查找多个元素
elements = driver.find_elements(By.CLASS_NAME, 'mnav')
for e in elements:
    print(e.text)




