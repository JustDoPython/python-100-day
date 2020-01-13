#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""
from PIL import Image
from io import BytesIO
import requests

# 打开图像文件
im = Image.open('cat.jpg')

# 打印图像的格式、大小、模式
print(im.format, im.size, im.mode)

# 从文件流中打开图像
r = requests.get('http://f.hiphotos.baidu.com/image/pic/item/b151f8198618367aa7f3cc7424738bd4b31ce525.jpg')
im2 = Image.open(BytesIO(r.content))

# 打印图像的格式、大小、模式
print(im2.format, im2.size, im2.mode)

# 展示图像
im.show()
im2.show()

# 翻转90度展示
im.rotate(90).show()