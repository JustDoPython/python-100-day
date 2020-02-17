import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
sns.set(color_codes=True)

# 2.1 示例
x = np.random.normal(size=100)
sns.distplot(x)

# 2.2 示例
x = np.random.normal(size=100)
sns.distplot(x, kde=False, rug=True)

# 2.3 示例
x = np.random.normal(size=100)
sns.distplot(x, hist=False, rug=True)

x = np.random.normal(0, 1, size=30)  # 初始化一组服从正态分布的随机数
bandwidth = 1.06 * x.std() * x.size ** (-1 / 5.)  # 根据经验公式计算 KDE 的带宽
support = np.linspace(-4, 4, 200)

kernels = []
for x_i in x:

    kernel = stats.norm(x_i, bandwidth).pdf(support)  # 获取每一个观测值的核密度估计
    kernels.append(kernel)
    plt.plot(support, kernel, color="r") # 为每一个观测值绘制核密度估计曲线

sns.rugplot(x, color=".2", linewidth=3)

from scipy.integrate import trapz
density = np.sum(kernels, axis=0)
density /= trapz(density, support)
plt.plot(support, density)

sns.kdeplot(x, shade=True)

sns.kdeplot(x)
sns.kdeplot(x, bw=.2, label="bw: 0.2")
sns.kdeplot(x, bw=2, label="bw: 2")
plt.legend()

sns.kdeplot(x, shade=True, cut=0)
sns.rugplot(x)

# 2.4 示例
x = np.random.gamma(6, size=200)
sns.distplot(x, kde=False, fit=stats.gamma)






