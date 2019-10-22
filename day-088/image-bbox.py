#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""

from PIL import Image

# 打开图像(451x300)
im = Image.open('cat.jpg')
# 创建新图像(450x450)
im1 = Image.new('L', (450, 450), 50)

# 打印图像中非零区域的边界框
print(im.getbbox())
print(im1.getbbox())

