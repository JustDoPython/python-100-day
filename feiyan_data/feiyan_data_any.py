import time, json, requests

# 腾讯疫情实时数据数据 URL
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d'%int(time.time()*1000)
# 加载 JSON 数据并解析
data = json.loads(requests.get(url=url).json()['data'])
#　打印数据输出数据
print(data)
print(data.keys())

# 统计省份信息(34个省份 湖北 广东 河南 浙江 湖南 安徽....)
num_area = data['areaTree'][0]['children']
print(len(num_area))
# 遍历所有数据后输出，直到输出结束
for item in num_area:
    print(item['name'],end=" ")
else:
    print("\n")

# 解析所有确诊数据
all_data = {}
for item in num_area:
    # 输出省市名称
    if item['name'] not in all_data:
        all_data.update({item['name']:0})
    #输出省市对应的数据
    for city_data in item['children']:
        all_data[item['name']] +=int(city_data['total']['confirm'])
#　输出结果
print(all_data)

#--------------------------------------------------------------------------------

# 使用 Matplotlib 绘制全国确诊病例柱状图
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  #正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    #正常显示负号

#获取数据
names = all_data.keys()
nums = all_data.values()
print(names)
print(nums)

# 绘图
plt.figure(figsize=[11,7])
plt.bar(names, nums, width=0.8, color='purple')

# 设置标题
plt.xlabel("地区", fontproperties='SimHei', size=15)
plt.ylabel("人数", fontproperties='SimHei', rotation=90, size=12)
plt.title("全国疫情确诊图", fontproperties='SimHei', size=16)
plt.xticks(list(names), fontproperties='SimHei', rotation=-60, size=10)

# 显示数字
for a, b in zip(list(names), list(nums)):
    plt.text(a, b, b, ha='center', va='bottom', size=6)

#　图形展示
plt.show()
