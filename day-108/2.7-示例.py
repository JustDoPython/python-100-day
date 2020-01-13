import numpy as np
A_mat = np.mat(np.eye(3, 3), int)
A_array = np.eye(3, 3)

print(np.linalg.matrix_rank(A_mat))
print(np.linalg.matrix_rank(A_array))