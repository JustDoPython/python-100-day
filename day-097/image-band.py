#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""

from PIL import Image

# 打开图像
im = Image.open('cat.jpg')
# 创建新图像
im1 = Image.new('L', (450, 450), 50)

# 获取图像的通道名称元组
print(im.getbands())
print(im1.getbands())

