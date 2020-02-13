import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="darkgrid")

# 3.1 示例
sns.catplot(x="day", y="total_bill", kind="box", data=tips)

sns.catplot(x="day", y="total_bill", hue="smoker", kind="box", data=tips)

sns.catplot(x="day", y="total_bill", hue="smoker", kind="box", dodge=False, data=tips)

tips["weekend"] = tips["day"].isin(["Sat", "Sun"])  # 新增变量 "weekend"，该变量并未嵌套在主分类 "day" 变量中
sns.catplot(x="day", y="total_bill", hue="weekend",
            kind="box", dodge=False, data=tips)
			
# 3.2 示例
diamonds = sns.load_dataset("diamonds")
print(diamonds)

sns.catplot(x="color", y="price", kind="boxen",
            data=diamonds.sort_values("color"))
			
# 3.3 示例
sns.catplot(x="total_bill", y="day", hue="time",
            kind="violin", data=tips)
			
sns.catplot(x="total_bill", y="day", hue="time",
            kind="violin", bw=.15, cut=0,  # bw:用来计算核密度的带宽，cut:设置为0将小提琴图范围限制在观察数据的范围内
            data=tips)

sns.catplot(x="day", y="total_bill", hue="sex",
            kind="violin", split=True, data=tips)
			
sns.catplot(x="day", y="total_bill", hue="sex",
            kind="violin", inner="stick", split=True,
            palette="pastel", data=tips)
			
g = sns.catplot(x="day", y="total_bill", kind="violin", inner=None, data=tips)
sns.swarmplot(x="day", y="total_bill", color="k", size=3, data=tips, ax=g.ax)





