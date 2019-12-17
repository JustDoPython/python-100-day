import matplotlib.pyplot as plt

plt.subplot(2,1,1)
#设置 x 和 y 轴上的值
plt.xticks([]), plt.yticks([]) # 表示无显示值
plt.text(0.5,0.5, 'subplot(2,1,1)',ha='center',va='center',size=24,alpha=.5)

plt.subplot(2,1,2)
plt.xticks([]), plt.yticks([])
plt.text(0.5,0.5, 'subplot(2,1,2)',ha='center',va='center',size=24,alpha=.5)

plt.show()
