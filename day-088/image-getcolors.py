#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""

from PIL import Image

im = Image.open('cat.png')

# 将彩色图像转换成灰度图
im2 = im.convert("L")

# 打印灰度图的颜色列表，返回的点数超过maxcolors就直接返回None
print(im2.getcolors(maxcolors=200))
print(im2.getcolors(maxcolors=255))

print(im2.getextrema())


