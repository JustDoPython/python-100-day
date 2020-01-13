from numpy import *
import numpy as np

#  numpy 简单运用实例
print(eye(4))

# 创建简单的 ndarray 对象
a = np.array([1, 2, 3])
print(a)

# 创建大于 1 维的数组 使用 ndmin 参数，ndmin 参数默认值为0
b = np.array([1, 2, 3], ndmin=2)
print(b)

b1 = np.array([2, 3, 4],ndmin=-1)
print(b1)

# 创建复合类型的数组
c = np.array([1, 2, 3],dtype=complex)
print(c)


# 查看 dtype 运用实例
# 创建一个数组,查看数组的数据类型
da = np.array([1, 2, 3])
print(da.dtype)

# 创建一个
dt = np.dtype('i4')
print(dt)

# 结构化数据类型的使用
# 首先创建结构化数据类型
da = np.dtype(np.int64)
print(da)

dt = np.dtype([('age',np.int8)])
print(dt)

# 将结构化数据类型应用于 ndarray 对象
dt = np.dtype([('age',np.int8)])
a = np.array([(10,),(20,),(30,)], dtype = dt)
print(a)

# 将类型对象用于存取实际的列
dt = np.dtype([('age',np.int8)])
a = np.array([(10,),(20,),(30,)], dtype = dt)
print(a['age'])

# 定义一个结构化数据类型 student，包含字符串字段 name，整数字段 age，及浮点字段 marks，并将这个 dtype 应用到 ndarray 对象
# 创建数组
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
# 将数组用于 ndarray 对象
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)
print(a)


# NumPy 数据类型转换实例

da = np.array([1.2,1.1,1.0])
# 输出 da 的数据类型
print(da.dtype)

# 转换 da 的数据类型
print(da.astype(np.int32))
# 重新查看数据类型,发现数据类型还未改变
print(da.dtype)

# 重新进行赋值操作
da = da.astype(np.int32)
print(da.dtype)
print(da)

