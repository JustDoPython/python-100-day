import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="darkgrid")

iris = sns.load_dataset("iris")
sns.catplot(data=iris, orient="h", kind="box")

sns.violinplot(x=iris.species, y=iris.sepal_length)

f, ax = plt.subplots(figsize=(7, 3))
sns.countplot(y="deck", data=titanic, color="c")