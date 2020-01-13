#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""

import numpy as np

print(np.char.center('argsort() 函数', 15, '*'))
a = np.array([3, 4, 2])
print("初始数组：")
print(a)
print('\n')

print(np.char.center('调用 argsort() 函数', 15, '*'))
b = np.argsort(a)
print(b)
print('\n')

print(np.char.center('以排序后的顺序重构原数组', 15, '*'))
print(a[b])
print('\n')
print('\n')


print(np.char.center('lexsort() 函数', 15, '*'))
# 录入了四位同学的成绩
math = (10, 20, 50, 10)
chinese = (30, 50, 40, 60)
total = (40, 70, 90, 70)
# 将优先级高的项放在后面
ind = np.lexsort((math, chinese, total))

for i in ind:
    print(total[i], chinese[i], math[i])

print('\n')
print('\n')

print(np.char.center('msort() 函数', 20, '*'))
msa = np.array([[3, 7, 12, 45], [9, 1, 0, 34]])
print(np.msort(msa))
print('\n')
print('\n')


print(np.char.center('partition() 函数', 20, '*'))
pta = np.array([3, 7, 12, 45, 15, 0])
print(np.partition(pta, 2))
print('\n')
print(np.partition(pta, (2, 4)))
print('\n')



