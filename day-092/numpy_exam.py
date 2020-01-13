import numpy as np
import matplotlib.pyplot as plt

# 赋值数组 a
a = np.array([22, 87, 43, 56, 73, 55, 11, 20, 51, 5, 79, 27,100])

# plt() 函数将数据变为直方图
plt.hist(a, bins=[0,20,40,60,80,100])
plt.title("histogram")
# 显示图形
plt.show()

# 调用函数
np.histogram(a, bins=[0, 20, 40, 60, 80, 100])
hist, bins = np.histogram(a, bins=[0, 20, 40, 60, 80, 100])

# 输出值
print(hist)
print(bins)

