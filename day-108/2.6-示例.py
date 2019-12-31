import numpy as np
A_mat = np.mat([[1, 2],[3, 4]], int)
A_array = np.array([[1, 2],[3, 4]])

print(np.linalg.det(A_mat))
print(np.linalg.det(A_array))