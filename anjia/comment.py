import pandas as pd, matplotlib.pyplot as plt

csv_data = pd.read_csv('data.csv')
df = pd.DataFrame(csv_data)
df_gp = df.groupby(['time']).size()
values = df_gp.values.tolist()
index = df_gp.index.tolist()
# 设置画布大小
plt.figure(figsize=(10, 6))
# 数据
# plt.plot(index, values, label='weight changes', linewidth=3, color='r', marker='o',
#          markerfacecolor='blue', markersize=20)
plt.plot(index, values, label='评论数')
# 设置数字标签
for a, b in zip(index, values):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=13, color='black')
plt.title('评论数随时间变化折线图')
# plt.xlabel('日期')
# plt.ylabel('评论数')
plt.xticks(rotation=330)
plt.tick_params(labelsize=10)
plt.ylim(0, 200)
plt.legend(loc='upper right')
plt.show()


