import numpy as np
a = 0.1
A_mat = np.mat(np.full((3, 3), 100), int)
A_array = np.full((3, 3), 100)
print(a*A_mat)
print(a*A_array)