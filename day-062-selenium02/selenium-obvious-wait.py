#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 声明浏览器对象
driver = webdriver.Chrome()

# 访问页面
driver.get("https://www.baidu.com/")

# 设置搜索关键词
element = driver.find_element_by_id("kw")
element.send_keys("selenium", Keys.ENTER)

# 此时页面右边的"相关术语"还没有加载出来，肯定会报错
#element1 = driver.find_element_by_class_name("opr-recommends-merge-p")
#print(element1)

# 显示等待10秒，直到页面右边的"相关术语"出现
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "opr-recommends-merge-p")))

# 获取页面右边的"相关术语"
element2 = driver.find_element_by_class_name("opr-recommends-merge-p")
print(element2)


