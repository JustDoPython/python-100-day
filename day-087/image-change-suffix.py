#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""

from PIL import Image

# 加载 cat.jpg
im = Image.open('cat.jpg', 'r')

# 打印图片类型
print(im.format)

# 保存为 png 类型图片
im.save('cat.png')

# 加载新保存的 png 类型图片
im2 = Image.open('cat.png', 'r')

# 打印新保存图片类型
print(im2.format)




