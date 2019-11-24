#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 声明浏览器对象
driver = webdriver.Chrome()

# 设置隐式等待时间，单位为秒
driver.implicitly_wait(0)

# 访问页面
driver.get("https://www.baidu.com/")

# 设置搜索关键词
element = driver.find_element_by_id("kw")
element.send_keys("selenium", Keys.ENTER)

# 页面右边的"相关术语"
element2 = driver.find_element_by_class_name("opr-recommends-merge-p")
print(element2)

