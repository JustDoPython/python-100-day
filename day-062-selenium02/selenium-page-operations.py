#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 声明浏览器对象
driver = webdriver.Chrome()
# 访问页面
driver.get("http://www.baidu.com")

# 获取百度搜索框元素
element = driver.find_element_by_id("kw")
# 在搜索框中输入关键词selenium
element.send_keys("selenium")
# 点击"百度一下"按钮
driver.find_element_by_xpath('//*[@id="su"]').click()

time.sleep(5)

# 清空搜索框关键词
element.clear()

time.sleep(2)

# 在搜索框中输入关键词python，并模拟键盘的enter操作
element.send_keys("python", Keys.ENTER)

time.sleep(5)

driver.close()


