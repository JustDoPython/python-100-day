import numpy as np
A_mat = np.mat(np.full((3, 3), 100), int)
A_array = np.full((3, 3), 100)

print(A_mat*A_mat)  # 点乘方式一
print(A_array*A_array)

print(A_mat.dot(A_mat))  # 点乘方式二
print(A_array.dot(A_array))