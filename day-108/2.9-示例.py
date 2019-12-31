import numpy as np
A_mat = np.mat([[1, 1, 1], [3, 1, 4], [8, 9, 5]], int)
b_mat = np.mat([[3], [8], [22]], int)
x = np.linalg.solve(A_mat, b_mat)
print(x)

A_array = np.array([[1, 1, 1], [3, 1, 4], [8, 9, 5]])
b_array = np.array([[3], [8], [22]])
x = np.linalg.solve(A_array, b_array)
print(x)