#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""
from PIL import Image

# 蓝色图像
image1 = Image.new('RGB', (128, 128), (0, 0, 255))
# 红色图像
image2=Image.new('RGB', (128, 128), (255, 0, 0))
# 取中间值
im = Image.blend(image1, image2, 0.5)
image1.show()
image2.show()
# 显示紫色图像,因为红色叠加蓝色会调和成紫色
im.show()
