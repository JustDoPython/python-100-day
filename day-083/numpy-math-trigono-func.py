#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""
import numpy as np

a = np.array([0, 30, 45, 60, 90])

print(np.char.center('不同角度的正弦值', 30, '*'))
# 通过乘 pi/180 转化为弧度
sin = np.sin(a*np.pi/180)
print(sin)
print('\n')

print(np.char.center('不同角度的余弦值', 30, '*'))
# 通过乘 pi/180 转化为弧度
cos = np.cos(a*np.pi/180)
print(cos)
print('\n')

print(np.char.center('不同角度的正切值', 30, '*'))
# 通过乘 pi/180 转化为弧度
tan = np.tan(a*np.pi/180)
print(tan)
print('\n')

print(np.char.center('不同角度的反正弦值', 30, '*'))
arcsin = np.arcsin(sin)
# 将弧度转换成角度打印输出
print(np.degrees(arcsin))
print('\n')

print(np.char.center('不同角度的反余弦值', 30, '*'))
arccos = np.arccos(cos)
# 将弧度转换成角度打印输出
print(np.degrees(arccos))
print('\n')

print(np.char.center('不同角度的反正切值', 30, '*'))
arctan = np.arctan(tan)
# 将弧度转换成角度打印输出
print(np.degrees(arctan))
print('\n')

