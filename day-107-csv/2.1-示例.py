import numpy as np
A = np.mat(np.full((3, 3), 100), int)
B = np.mat(np.full((3, 3), 200), int)
print(A+B)
print(A-B)