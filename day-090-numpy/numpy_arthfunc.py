import numpy as np

# 数的对数测试
c = 100
print('数字100的对数：')
print(np.log(c))
print('\n')

a = np.arange(16, dtype=np.int_).reshape(4,4)
print('第一个数组：')
print(a)
print('\n')

print('第二个数组：')
b = np.array([10, 10, 10, 10])
print(b)
print('\n')

print('两个数组相除：')
print(np.divide(a, b))

# 两个数组相加
print('两个数组相加：')
print(np.add(a, b))
print('\n')


print('两个数组相减：')
print(np.subtract(a, b))
print('\n')

print('两个数组相乘：')
print(np.multiply(a, b))
print('\n')

print('两个数组相除：')
print(np.divide(a, b))
print('\n')

# 数的对数测试
c = 100
print('100的对数：')
print(np.log(c))
print('\n')

# NumPy 幂计算
import numpy as np

d = np.array([2, 5, 10])
print('第一个数组是：')
print(d)

print('\n')
print('调用 power 函数：')
print(np.power(d, 2))

print('\n')
print('第二个数组：')
e = np.array([1, 2, 3])
print(e)
print('\n')
print('再次调用 power 函数：')
print(np.power(d, e))
