import numpy as np
A = np.mat([[1, 1, 1], [3, 1, 4], [8, 9, 5]], int)
b = np.mat([[3], [8], [22]], int)
x = np.linalg.solve(A,b)
print(x)