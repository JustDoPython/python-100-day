import numpy as np
A_mat = np.mat([[1, 2],[3, 4]], int)
A_array = np.array([[1, 2],[3, 4]])

A_mix = A_mat + A_array
print(A_mix, type(A_mix))

A_array = np.array([1, 2])
A_mix = A_mat + A_array
print(A_mix, type(A_mix))