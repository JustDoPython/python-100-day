# 导入模块
import numpy as np
import matplotlib.pyplot as plt

# 绘制 x 轴数据
x = np.arange(2, 15)
y = 3 * x+6

# 给图形设置标题
plt.title('line chart')
# 设置 x 轴和 y 轴的属性名
plt.xlabel("x axis")
plt.ylabel("y axis")

# 绘制图形
plt.plot(x,y)

# 显示图形
plt.show()