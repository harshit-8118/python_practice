import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
print(titanic.head())

titanic_pivot = titanic.pivot_table(index='who', columns='class', values='survived')
sns.heatmap(titanic_pivot, cmap='YlGnBu', annot=True)
plt.show()
