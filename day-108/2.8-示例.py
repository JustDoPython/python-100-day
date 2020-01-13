import numpy as np
A_mat = np.mat([[1, 2],[3, 4]], int)
value, vector = np.linalg.eig(A_mat)
print(value)
print(vector)

A_array = np.array([[1, 2],[3, 4]])
value, vector = np.linalg.eig(A_array)
print(value)
print(vector)