#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""

from PIL import Image

im = Image.open('cat.png')
im.show()
# 将图像转换成黑白色并返回新图像
im1 = im.convert('L')
im1.show()



