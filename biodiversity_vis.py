"""
Biodiversity Index Visualization
"""

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

data = pd.read_csv("living-planet-index.csv", delimiter=';')

data.rename(columns = {'Average Index':'AverageIndex'}, inplace = True)

ax = sns.lineplot(data=data, x="Year", y="AverageIndex", hue="Region")

plt.legend(fontsize=7.5)

plt.ylabel("Average Biodiversity Index")

plt.title("Average Biodiversity Over Time")

plt.ylim(0, 200)

plt.show()

