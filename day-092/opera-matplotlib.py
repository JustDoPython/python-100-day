
import numpy as np

import matplotlib.pyplot as plt

# np.linspace() 是等差数列函数,返回num均匀分布的样本，在[start, stop]

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)

C,S = np.cos(X), np.sin(X)

plt.plot(X,C)
plt.plot(X,S)

plt.show()


