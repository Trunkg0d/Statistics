import pandas as pd
import numpy as np
from statsmodels import robust
from scipy import stats
import weightedstats as ws

def weight_mean(distribution, weight):
    sum_dis = sum(distribution*weight)
    sum_weight = sum(weight)
    return float(sum_dis/sum_weight)

def IQR(data):
    q3, q1 = np.percentile(data,[75,25])
    iqr = q3-q1
    return iqr

def Mean_Absolute_Deviation(data):
    mean = data.mean()
    mad = sum(abs(df["Population"] - mean) ) / len(df["Population"])
    return mad
    
df = pd.read_csv("state.csv")
print(df)
# Mean of the population
print("Mean of the population: ", df["Population"].mean())
print("--------")
#Trimmed mean of the population
print("Trimmed mean of the population: ",stats.trim_mean(df["Population"],0.1))
print("--------")
#The median of the population
print("Median of the population: ", df["Population"].median())
print("--------")
#The Weighted mean of the murder rate of each population
print("Weighted mean of the murder rate: ",weight_mean(df["Murder rate"], df["Population"]))
print("--------")
#The weighted median of the murderer
print("The weight median of the murderer: ", ws.weighted_median(df["Murder rate"].tolist(), df["Population"].tolist()))
print("--------")
#The variance of the population
variance = df["Population"].var()
print("The variance of the population: ", variance)
print("--------")
#The standard deviation of the population: sd = var ** (1/2)
print("The standard deviation: ", variance**(1/2))
print("--------")
#The IQR of the population:
print("The IQR of the Population: ", IQR(df["Population"]))
print("--------")
#The Mean Absolute Deviation of the population:
print("The Mean Absolute Deviation of the population: ", df["Population"].mad())
print("The Mean Absolute Deviation of the Population: ", Mean_Absolute_Deviation(df["Population"]))
print("--------")
#The Median Absolute Deviation of the population:
print("The Median Absolute Deviation of the population:",robust.mad(df["Population"]))
print("--------")



