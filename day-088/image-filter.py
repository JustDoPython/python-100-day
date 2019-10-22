#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""
from PIL import Image
from PIL import ImageFilter


im = Image.open('flower.jpg')
im.show()

# 模糊
im2 = im.filter(ImageFilter.BLUR)
im2.show()

# 轮廓滤波
im3 = im.filter(ImageFilter.CONTOUR)
im3.show()

# 细节增强
im4 = im.filter(ImageFilter.DETAIL)
im4.show()

