import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="darkgrid")

# 2.1Ê¾Àý
tips = sns.load_dataset("tips")
sns.catplot(x="day", y="total_bill", data=tips)

sns.catplot(x="day", y="total_bill", jitter=False, data=tips)

# 2.2Ê¾Àý
sns.catplot(x="day", y="total_bill", kind="swarm", data=tips)

sns.catplot(x="day", y="total_bill", hue="sex", kind="swarm", data=tips)

sns.catplot(x="size", y="total_bill", kind="swarm", data=tips)

sns.catplot(x="size", y="total_bill", order=[6, 5, 4, 2, 1, 3], kind="swarm", data=tips)

sns.catplot(x="total_bill", y="day", hue="time", kind="swarm", data=tips)

