import numpy as np

# Numpy 位与运算
a, b = 13, 17
print('13 和 17 的二进制：')
print(bin(a), bin(b))
print('\n')


print('13 和 17 的位与：')
print(np.bitwise_and(a,b))

# Numpy 位或运算
a, b = 13, 17
print('13 和 17 的二进制形式：')
print(bin(a), bin(b))

print('13 和 17 的位或：')
print(np.bitwise_or(a,b))


# Numpy 非操作

# 比较 13 和 242 的二进制表示，发现了位的反转
print('13 的二进制表示：')
print(np.binary_repr(13, width=8))
print('\n')

print('242 的二进制表示：')
print(np.binary_repr(242, width=8))

print('13 的位反转：')
print(np.invert(np.array([13], dtype=np.uint8)))
print('\n')

# Numpy 左移二进制位操作

print('将 10 左移两位：')
print(np.left_shift(10, 2))
print('\n')

print('10 的二进制表示：')
print(np.binary_repr(10, width=8))
print('\n')

print('40 的二进制表示：')
print(np.binary_repr(40, width=8))
#  '00001010' 中的两位移动到了左边，并在右边添加了两个 0。

# Numpy 右移二进制位操作

print('将 40 右移两位：')
print(np.right_shift(40, 2))
print('\n')

print('40 的二进制表示：')
print(np.binary_repr(40, width=8))
print('\n')

print('10 的二进制表示：')
print(np.binary_repr(10, width=8))
#  '00001010' 中的两位移动到了右边，并在左边添加了两个 0。