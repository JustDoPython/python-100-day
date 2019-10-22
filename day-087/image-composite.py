#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""
from PIL import Image

# 打开 cat.png
image1 = Image.open('cat.png')

# 打开 flower.jpg
image2 = Image.open('flower.jpg')

# 分离image1的通道
r, g, b = image1.split()

# 合成图像，获得 cat + flower
im = Image.composite(image1, image2, mask=b)

image1.show()
image2.show()
im.show()
