#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""
import numpy as np

a = np.array([1, 2.0, 30.12, 129.567])

# 四舍五入（取整）
print(np.around(a))
# 四舍五入（取一位小数）
print(np.around(a, decimals=1))
# 四舍五入（取小数点左侧第一位）
print(np.around(a, decimals=-1))

print(np.char.center('我是分隔线', 30, '*'))
print('\n')

# 只舍不入（取整）
print(np.around(a))
# 只舍不入（到小数点后一位）
print(np.around(a, decimals=1))
# 只舍不入（取小数点左侧第一位）
print(np.around(a, decimals=-1))

print(np.char.center('我是分隔线', 30, '*'))
print('\n')

# 向下取整
print(np.floor(a))

print(np.char.center('我是分隔线', 30, '*'))
print('\n')

# 向上取整
print(np.ceil(a))







