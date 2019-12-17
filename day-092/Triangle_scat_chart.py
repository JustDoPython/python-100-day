# 导入模块
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(2, 15)
y = 2 * x + 6
plt.title("triangle_scatter chart")
plt.xlabel("x axis")
plt.ylabel("y axis")

# 设置图形样式和颜色
plt.plot(x, y, "^c")
plt.show()