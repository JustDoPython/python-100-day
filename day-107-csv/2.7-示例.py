import numpy as np
A = np.mat([[1, 2],[3, 4]], int)
rank = np.linalg.matrix_rank(A)
print(rank)