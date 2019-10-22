#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""

from PIL import Image

im = Image.open('cat.png')
# 将三个通道分开
im_split = im.split()

# 分别显示三个单通道图像
im_split[0].show()
im_split[1].show()
im_split[2].show()

# 将三个通道再次合并
im2 = Image.merge('RGB', im_split)
im2.show()

# 打开第二张图像
im3 = Image.open('flower.jpg')
# 将第二张图像的三个通道分开
im_split2 = im3.split()

# 将第二张图像的第1个通道和第一张图像的第2、3通道合成一张图像
rgbs = [im_split2[0], im_split[1], im_split[2]]
im4 = Image.merge('RGB', rgbs)
im4.show()


