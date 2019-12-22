#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""

from PIL import Image

# 加载图像
im = Image.open('cat.png')

# 展示图像
im.show()

# 图像尺寸
size = 128, 128
# 缩放图像
im.thumbnail(size, Image.ANTIALIAS)

# 展示图像
im.show()





