#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""

import numpy as np
import time

a = np.array([[3, 7, 12, 45], [9, 1, 0, 34]])
print("初始数组：")
print(a)
print('\n')

print(np.char.center('调用 sort() 函数，默认快速排序', 15, '*'))
print(np.sort(a))
print('\n')

print(np.char.center('按列排序', 15, '*'))
print(np.sort(a, axis=0))
print('\n')

b = np.random.randint(1, 1000, size=[10000, 10000])

print(np.char.center('快速排序时间', 15, '*'))
t1 = time.time()
np.sort(b)
t2 = time.time()
print(t2 - t1)
print('\n')

print(np.char.center('堆排序时间', 15, '*'))
t3 = time.time()
np.sort(b, -1, 'heapsort')
t4 = time.time()
print(t4 - t3)
print('\n')

print(np.char.center('归并排序时间', 15, '*'))
t5 = time.time()
np.sort(b, -1, 'mergesort')
t6 = time.time()
print(t6 - t5)
print('\n')

# 根据字段排序
dt = np.dtype([('name', 'S10'), ('age', int)])
c = np.array([("raju", 21), ("anil", 25), ("ravi", 17), ("amar", 27)], dtype=dt)
print(np.char.center('根据字段排序的数组', 15, '*'))
print(c)
print('\n')

print(np.char.center('按 name 排序', 15, '*'))
print(np.sort(c, order='name'))


