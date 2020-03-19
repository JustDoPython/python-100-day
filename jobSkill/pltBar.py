import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
params = {
    'axes.labelsize': '14',
    'xtick.labelsize': '14',
    'ytick.labelsize': '13',
    'lines.linewidth': '2',
    'legend.fontsize': '20',
    'figure.figsize': '26, 24'
}
plt.style.use("ggplot")
plt.rcParams.update(params)

# 筛选分词中高频的
barDir = {
    'PYTHON': 2283,
    'LINUX': 981,
    '算法': 658,
    '运维': 530,
    '数据库(MySql,Sql,Redis等)': 1021,
    'SHELL': 996,
    '数据分析/挖掘': 695,
    'WEB': 454,
    '测试用例': 515,
    'MATLAB': 221,
    'PERL': 209,
    'HIVE': 122,
    'HADOOP': 176,
    'SPARK': 146,
    'TENSORFLOW': 136,
    '多线程': 127,
    'AI': 106,
    'SAS': 104,
    '视觉/图像处理': 180,
    '人工智能': 170,
    'HTTP': 90,
    'DOCKER': 82,
    'DJANGO': 82,
}


fig, ax = plt.subplots(figsize=(20, 10), dpi=100)

# 添加刻度标签
labels = np.array(list(barDir.keys()))
ax.barh(range(len(barDir.values())), barDir.values(), tick_label=labels, alpha=1)

ax.set_xlabel('Python技术词的次数', color='k')
ax.set_title('Python工作高频技术词')


# 为每个条形图添加数值标签
for x, y in enumerate(barDir.values()):
    ax.text(y + 0.5, x, y, va='center', fontsize=14)

# 显示图形
plt.show()
