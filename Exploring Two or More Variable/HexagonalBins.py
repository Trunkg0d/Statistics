import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv("HexagonalBins.csv")
ax = df1.plot.hexbin(x='X_Data', y='Y_Data', gridsize=20)

df2 = pd.read_csv("Hexbin2.csv")
ax = df2.plot.hexbin(x='coord_x',
                    y='coord_y',
                    C='observations',
                    reduce_C_function=np.sum,
                    gridsize=10,
                    cmap="viridis")

# x     int or str
# The column label or position for x points.

# y     int or str
# The column label or position for y points.

# C     int or str, optional
# The column label or position for the value of (x, y) point.

# reduce_C_functioncallable, default np.mean
# Function of one argument that reduces all the values in a bin to a single number (e.g. np.mean, np.max, np.sum, np.std).
#For example, with the reduce_C_function = np.sum, they sum the value of each point(x, y) in the group


