#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""
from PIL import Image

im = Image.open('cat.png')

# 调整灰色图像的对比度
im_point=im.convert('L').point(lambda i: i < 80 and 255)
im_point.show()

source = im.split()
# 三通道分别处理对比度（当像素值小于80时，将其调整为255，相当于）
band_r = source[0].point(lambda i: i < 80 and 255)
band_g = source[1].point(lambda i: i < 80 and 255)
band_b = source[2].point(lambda i: i < 80 and 255)
band_r.show()
band_g.show()
band_b.show()
