import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("correlation.csv")
print(df)

# The standard way to visualize the relationship between two measured data
# variables is with a scatterplot. The x-axis represents one variable, the 
# y-axis another, and each point on the graph is a record

#Example pick first variable is T and another variable is VZ

first_data = df.loc[:,"T"].to_numpy()
second_data = df.loc[:,"VZ"].to_numpy()

plt.subplot(1,2,1)
plt.scatter(first_data, second_data)
plt.xlabel("T")
plt.ylabel("VZ")

first_data = df.loc[:,"T"].to_numpy()
second_data = df.loc[:,"LVLT"].to_numpy()

plt.subplot(1,2,2)
plt.scatter(first_data, second_data)
plt.xlabel("T")

plt.show()