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

# 通过id查找
element = driver.find_element_by_id("kw")
print(element.tag_name)
# 通过name查找
element = driver.find_element_by_name("wd")
print(element.tag_name)
# 通过xpath查找
element = driver.find_element_by_xpath('//*[@id="kw"]')
print(element.tag_name)

# 通过另一种方式查找
element = driver.find_element(By.ID, "kw")
print(element.tag_name)





