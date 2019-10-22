#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""
from PIL import Image

im = Image.open('flower.jpg')

img1 = im.resize((250, 250), Image.BILINEAR)
img2 = im.resize((250, 250), Image.BICUBIC)
img3 = im.resize((250, 250), Image.NEAREST)

im.show()
img1.show()
img2.show()
img3.show()