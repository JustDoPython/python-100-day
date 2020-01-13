#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""

import numpy as np

a = np.array([[30, 40, 70], [80, 20, 10], [50, 90, 60]])
print(np.char.center('初始数组', 20, '*'))
print(a)
print('\n')

print(np.char.center('调用 argmax() 函数', 20, '*'))
print(np.argmax(a))
print('\n')

print(np.char.center('展开数组', 20, '*'))
print(a.flatten())
print('\n')

print(np.char.center('沿0轴的最大索引', 20, '*'))
print(np.argmax(a, 0))
print('\n')

print(np.char.center('沿1轴的最大索引', 20, '*'))
print(np.argmax(a, 1))
print('\n')

print(np.char.center('调用 argmin() 函数', 20, '*'))
print(np.argmin(a))
print('\n')

print(np.char.center('沿0轴的最小索引', 20, '*'))
print(np.argmin(a, 0))
print('\n')

print(np.char.center('沿1轴的最小索引', 20, '*'))
print(np.argmin(a, 1))

b = np.array([[30, 40, 0], [0, 20, 10], [50, 0, 60]])
print(np.char.center('我们的数组是', 20, '*'))
print(b)
print(np.char.center('调用 nonzero() 函数', 20, '*'))
c = np.nonzero(b)
print(c)
print(np.transpose(np.nonzero(b)))

print(np.char.center('调用 where() 函数', 20, '*'))
print(np.where(b > 20))
print(np.transpose(np.where(b > 20)))


x = np.arange(9.).reshape(3,  3)
print(np.char.center('我们的数组是', 20, '*'))
print(x)
# 定义条件, 选择偶数元素
condition = np.mod(x, 2) == 0
print(np.char.center('按元素的条件值', 20, '*'))
print(condition)
print(np.char.center('使用条件提取元素', 20, '*'))
print(np.extract(condition, x))


