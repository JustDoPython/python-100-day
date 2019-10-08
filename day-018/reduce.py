# -*-coding:UTF-8-*-
from functools import reduce

result = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])

print(result)
# print out： 15


# 设定初始参数：
s = reduce(lambda x, y: x + y, ['1', '2', '3', '4', '5'], "数字 = ")

print(s)
# print out： 数字 = 12345


error = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], "数字 = ")

print(error)
# TypeError: can only concatenate str (not "int") to str

