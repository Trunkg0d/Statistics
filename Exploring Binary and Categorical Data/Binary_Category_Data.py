import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("delay_cause.csv")
print(df)

#Bar plot 
cause = df.columns.to_list()
percent = df.iloc[0].to_list()
plt.bar(cause, percent)
plt.xlabel("Cause")
plt.ylabel("Percentage")
plt.show()
