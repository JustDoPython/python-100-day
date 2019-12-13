#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""

import numpy as np

a = np.arange(6, dtype=np.float_).reshape(2, 3)
print('第一个数组：')
print(a)
print('第二个数组：')
b = np.array([10, 10, 10])
print(b)
print('\n')

print(np.char.center('两个数组相加', 20, '*'))
print(np.add(a, b))
print('\n')

print(np.char.center('两个数组相减', 20, '*'))
print(np.subtract(a, b))
print('\n')

print(np.char.center('两个数组相乘', 20, '*'))
print('两个数组相乘：')
print(np.multiply(a, b))
print('\n')

print(np.char.center('两个数组相除', 20, '*'))
print(np.divide(a, b))
print('\n')

print(np.char.center('可爱分隔线', 20, '*'))
print('\n')

c = np.array([10, 100, 1000])
print('第一个数组是：')
print(c)
print('\n')

print(np.char.center('调用 power 函数', 20, '*'))
print(np.power(c, 2))
print('\n')

d = np.array([1, 2, 3])
print('第二个数组是：')
print(d)
print('\n')

print(np.char.center('再次调用 power 函数', 20, '*'))
print(np.power(c, d))

print(np.char.center('可爱分隔线', 20, '*'))
print('\n')

e = np.array([10, 20, 30])
f = np.array([3, 5, 7])
print('第一个数组：')
print(e)
print('\n')

print('第二个数组：')
print(f)
print('\n')

print(np.char.center('调用 mod 函数', 20, '*'))
print(np.mod(e, f))



