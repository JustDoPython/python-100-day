#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""

from selenium import webdriver
import time

# 声明浏览器对象
driver = webdriver.Chrome()
# 访问百度
driver.get("http://www.baidu.com")
time.sleep(2)
# 访问微博
driver.get("https://weibo.com")
time.sleep(2)
# 访问知乎
driver.get("http://www.zhihu.com")
time.sleep(2)
# 返回上个页面
driver.back()
time.sleep(2)
# 前进到下个页面
driver.forward()

# 退出
driver.close()



