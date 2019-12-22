#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""

from PIL import Image

im = Image.new('RGB', (450, 450), (255, 0, 0))
im1 = Image.new('RGB', (450, 450), 'red')
im2 = Image.new('RGB', (450, 450), '#FF0000')
im.show()
im1.show()
im2.show()

