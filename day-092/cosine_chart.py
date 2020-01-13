import numpy as np
import matplotlib.pyplot as plt

# 计算正弦曲线上点的 x 和 y 坐标
print(np.pi)

# 绘制 x 轴，从 0 开始，
x = np.arange(0, 4 * np.pi,  0.1)
y = np.cos(x)

# 设置标题
plt.title("cosine wave form")

# 绘制图形点
plt.plot(x, y, 'm')
plt.show()