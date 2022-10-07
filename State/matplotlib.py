import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels import robust
from scipy import stats
import weightedstats as ws

df = pd.read_csv("state.csv")
print(df)

#------------------------------------------------#
#Percentiles and Boxplots

# A boxplot — with the top and bottom of the box at the 75th and 25th percentiles, 
# respectively — also gives a quick sense of the distribution of the data; it is 
# often used in side-by-side displays to compare distributions.

#Plot the box plot
fig = plt.figure(figsize = (10,7))
plt.boxplot([df["Population"]/1000000, df["Murder rate"]])
plt.ylabel("Population (millions)")
plt.show()

#------------------------------------------------#
# Frequency Table and Histograms

# A frequency histogram plots frequency counts on the y-axis and variable values 
# on the x-axis; it gives a sense of the distribution of the data at a glance

min = df["Population"].min()
max = df["Population"].max()

arr = np.arange(min,max+1)

#To get the bins
cut, bins = pd.cut(arr, 10, retbins = True)

#To cut the df["Population"] into the bins
value_counts  = df["Population"].value_counts(bins=bins)
print(value_counts)

df1 = pd.DataFrame(value_counts)
df1 = df1.reset_index()
print(df1)
df1.columns = ["Bin Range", "Count"]

#Plot histogram with exist bins
plt.hist(df["Population"], bins = bins, edgecolor='black', linewidth=1.2)
#Edgecolor, linewidth to set border color and width
plt.ylabel("Count")
plt.xlabel("Population (e+0.7)")
plt.show()

#------------------------------------------------#
#Density Estimates

# A density plot is a smoothed version of a histogram; it requires 
# a function to estimate a plot based on the data (multiple estimates are possible, of course).

# plt.hist(df["Murder rate"], bins = 4, edgecolor="black", linewidth = 1.2)
# df["Murder rate"].plot(kind="density")
# plt.ylim((0,0.5))
# plt.xlim((2,6))

#OR Use Seaborn
#use matplotlib.pyplot.subplot to show many graph
fig, axs = plt.subplots(1,2)
sns.distplot(df["Murder rate"], hist = False, color = "red", ax= axs[0])

#if hist = False, it will not show the histogram graphic
sns.distplot(df["Murder rate"], hist = True, color = "red", hist_kws={"edgecolor":"black"}, ax= axs[1])
plt.show()

