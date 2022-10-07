import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:\D Data\code\Statistics for DA\State\state.csv")
print(df)

plt.subplot(1,2,1)
plt.violinplot([df["Population"]/10000000, df["Murder rate"]])
plt.xticks([1,2],["Population * 10000000", "Murder rate"])

plt.subplot(1,2,2)
plt.boxplot([df["Population"]/10000000, df["Murder rate"]])
plt.xticks([1,2],["Population * 10000000", "Murder rate"])
plt.show()
