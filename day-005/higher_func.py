# -*-coding:UTF-8-*-

# 常见的一些数学函数如下：
# ceil(X):大于或等于X的整数！
# cos(X):X的余弦.
# degrees(X):将X的弧度转为度.
# exp(x):e的X次方.
# factorial(n):计算n的阶乘(n!).
# log(x):以e为底的x 的对数
# log(x,b):以b为底的X的对数
# pow(x,y):x的y次方.//**也是乘方！
# radians(x):将x度转换为弧度数
# sin(x):x的正弦
# sqrt(x):x的平方根
# tan(x):x的正切.
from math import factorial

def high_func(f, arr):
    return [f(x) for x in arr]

def square(n):
    return n ** 2

# 使用python自带数学函数
print(high_func(factorial, list(range(10))))
# print out: [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

# 使用自定义函数
print(high_func(square, list(range(10))))
# print out: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



