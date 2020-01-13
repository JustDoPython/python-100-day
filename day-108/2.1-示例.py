import numpy as np
A_mat = np.mat([[1, 2],[3, 4]], int)
B_mat = np.mat([[1, 2],[3, 4]], int)
A_array = np.array([[1, 2],[3, 4]])
B_array = np.array([[1, 2],[3, 4]])
print(A_mat + B_mat)
print(A_array + B_array)

C_array = np.array([[1, 2]])
C_mat = np.mat([[1, 2]], int)
print(A_array + C_array)
print(A_mat + C_mat)