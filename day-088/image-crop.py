#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""
from PIL import Image

im = Image.open('cat.jpg')
print(im.size)
im.show()

# 定义了图像的坐标位置，从左、上、右、下
box = (100, 100, 250, 250)

# 它会从左上角开始，同时向下和向右移动100像素的位置开始截取250-100的像素宽高，也就是150x150的图像
# 这里注意后两个数值要大于前两个数值，不然截取后的图像宽高为负数，会报错
region = im.crop(box)
print(region.size)
region.show()
