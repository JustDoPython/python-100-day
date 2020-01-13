#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""

import numpy as np


# 连接两个字符串：
print(np.char.add(['hello'], [' world']))

# 连接多个字符串
print(np.char.add(['hello', 'hi'], [' world', ' Tracy']))


# 多重连接
print(np.char.multiply('hello ', 3))
print(np.char.multiply(['hello', 'hi'], 3))

# np.char.center(str , width,fillchar) ：
# str: 字符串，width: 长度，fillchar: 填充字符
print(np.char.center('hello', 20, fillchar='*'))
print(np.char.center(['hello', 'hi'], 19, fillchar='*'))

# 首字母大写
print(np.char.capitalize('hello'))

# 每个单词的首字母大写
print(np.char.title('i love china'))


# 操作字符串
print(np.char.lower('GOOGLE'))

# 操作数组
print(np.char.lower(['I', 'LOVE', 'CHINA']))


# 操作字符串
print(np.char.upper('google'))

# 操作数组
print(np.char.upper(['', 'love', 'china']))


# 分隔符默认为空格
print(np.char.split('do you love china?'))
# 分隔符为 ,
print(np.char.split('yes,i do', sep=','))


# 换行符 \r
print(np.char.splitlines('I\rLove China'))
# 换行符 \n
print(np.char.splitlines('I\nLove China'))
# 换行符 \r\n
print(np.char.splitlines('I\r\nLove China'))


# 将 \t 转成3个tab
print(np.char.expandtabs('i\tlove\tchina', 3))

# 移除字符串头尾的 a 字符
print(np.char.strip('it love china', 'i'))

# 移除数组元素头尾的 a 字符
print(np.char.strip(['it', 'love', 'china'], 'i'))


# 去除左边的空格
print(np.char.lstrip('    china    '))

# 去除右边的空格
print(np.char.rstrip('    china    '))


# 操作字符串
print(np.char.join(':', 'china'))

# 操作数组
print(np.char.join(':', ['china', 'american']))


# 操作字符串
print(np.char.partition('china', 'i'))

# 操作数组
print(np.char.partition(['china', 'like'], 'i'))


# 指定多个分隔符操作数组元素
print(np.char.join([':', '-'], ['china', 'american']))

# 替换字符串
print(np.char.replace('i love china', 'ov', 'ik'))

# 编码
print(np.char.encode('中国', 'utf-8'))

a = np.char.encode('中国', 'utf-8')
print(a)
# 解码
print(np.char.decode(a, 'utf-8'))









