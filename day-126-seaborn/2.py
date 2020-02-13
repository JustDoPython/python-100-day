import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

tips= sns.load_dataset("tips")
print('tips 数据集前十行数据:\n', tips.head(5))
print('每一列的数据类型:\n', tips.dtypes)

# 2.1示例
sns.relplot(x="total_bill", y="tip", data=tips) 

# 2.2示例
sns.relplot(x="total_bill", y="tip", hue="smoker", data=tips)  

# 2.3示例
sns.relplot(x="total_bill", y="tip", hue="smoker", style="smoker", data=tips)  

# 2.4示例
sns.relplot(x="total_bill", y="tip", hue="smoker", style="time", data=tips)  

# 2.5示例
sns.relplot(x="total_bill", y="tip", hue="size", data=tips)  

# 2.6示例
sns.relplot(x="total_bill", y="tip", size="size", data=tips)  
sns.relplot(x="total_bill", y="tip", size="size", sizes=(15, 200), data=tips)

