import pandas as pd, jieba, matplotlib.pyplot as plt

csv_data = pd.read_csv('data.csv')
roles = {'姑姑':0, '房似锦':0, '王子':0, '闪闪':0, '老油条':0, '楼山关':0, '鱼化龙':0}
names = list(roles.keys())
for name in names:
    jieba.add_word(name)
for row in csv_data['comments']:
    row = str(row)
    for name in names:
        count = row.count(name)
        roles[name] += count
plt.figure(figsize=(8, 5))
# 数据
plt.bar(list(roles.keys()), list(roles.values()), width=0.5, label='提及次数', color=['g', 'r', 'dodgerblue', 'c', 'm', 'y', 'aquamarine'])
# 设置数字标签
for a, b in zip(list(roles.keys()), list(roles.values())):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=13, color='black')
plt.title('角色被提及次数柱状图')
plt.xticks(rotation=270)
plt.tick_params(labelsize=10)
plt.ylim(0, 30)
plt.legend(loc='upper right')
plt.show()