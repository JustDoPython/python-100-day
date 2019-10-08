# -*-coding:UTF-8-*-
from math import factorial


def square(n):
    return n ** 2

# 使用python自带数学函数
facMap = map(factorial, list(range(10)))
print(list(facMap))
# print out: [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

# 使用自定义函数
squareMap = map(square, list(range(10)))
print(list(squareMap))
# print out: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 使用匿名函数
lamMap = map(lambda x: x * 2, list(range(10)))
print(list(lamMap))
# print out: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 传入多个序列
mutiMap = map(lambda x, y: x+y, list(range(10)), list(range(11, 15)))
print(list(mutiMap))
# print out: [11, 13, 15, 17]

