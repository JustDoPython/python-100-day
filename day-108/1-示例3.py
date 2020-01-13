import numpy as np
A_array = np.array([[1, 2],[3, 4]])
A_mat = np.mat(A_array, int)
print(A_mat, type(A_mat))
print(A_array, type(A_array))