import numpy as np
A = np.mat(np.full((2, 3), 10), int)
B = np.mat(np.full((3, 3), 10), int)
print(A*B)  # 求矩阵相乘形式一
print(A.dot(B))  # 求矩阵相乘形式二
print(np.dot(A, B))  # 求矩阵相乘形式三