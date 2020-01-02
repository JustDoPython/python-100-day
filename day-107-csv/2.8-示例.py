import numpy as np
A = np.mat([[1, 2],[3, 4]], int)
value, vector = np.linalg.eig(A)
print(value)
print(vector)