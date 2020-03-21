import pandas as pd, numpy as np, matplotlib.pyplot as plt

csv_data = pd.read_csv('data.csv')
df_time = csv_data.groupby(['time']).size()
df_star = csv_data.groupby(['star']).size()
index = df_time.index.tolist()
value = [0] * len(index)
# 生成字典
dic = dict(zip(index, value))
# rows = df.loc[df['time'] == '2020-03-05', 'star']
# list = list(map(int, rows.values.tolist()))
# avg = np.mean(list)
# print(list)
# print(avg)
for k, v in dic.items():
    stars = csv_data.loc[csv_data['time'] == str(k), 'star']
    # 平均值
    avg = np.mean(list(map(int, stars.values.tolist())))
    dic[k] = round(avg ,2)
# 设置画布大小
plt.figure(figsize=(9, 6))
# 数据
plt.plot(list(dic.keys()), list(dic.values()), label='星级', color='red', marker='o')
plt.title('星级随时间变化折线图')
plt.xticks(rotation=330)
plt.tick_params(labelsize=10)
plt.ylim(0, 5)
plt.legend(loc='upper right')
plt.show()

