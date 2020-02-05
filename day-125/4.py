import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="darkgrid")

titanic = sns.load_dataset("titanic")
print(titanic)

# 4.1 示例
sns.catplot(x="sex", y="survived", hue="class", kind="bar", data=titanic)

# 4.2 示例
sns.catplot(x="deck", kind="count", palette="ch:.25", data=titanic)

sns.catplot(y="deck", hue="class", kind="count",
            palette="pastel", edgecolor=".6",
            data=titanic)
			
# 4.3 示例
sns.catplot(x="sex", y="survived", hue="class", kind="point", data=titanic)

sns.catplot(x="class", y="survived", hue="sex",
            palette={"male": "g", "female": "m"},
            markers=["^", "o"], linestyles=["-", "--"],
            kind="point", data=titanic)