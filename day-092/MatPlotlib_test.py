import matplotlib.pyplot as plt

# 示例1 简单绘图示例
plt.plot([1, 2], [1, 2], 'r--+')
plt.show()

# 示例2
# 指定一个画板
fig = plt.figure()
# 指定画板后指定轴
# ax = fig.add_subplot(111)
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(224)
ax4 = fig.add_subplot(223)
# 设置轴的位置
# ax.set(xlim=[0.5, 4.5], ylim=[-2, 8], title='An Example Axes',
#        ylabel='Y-Axis', xlabel='X-Axis')
plt.show()





