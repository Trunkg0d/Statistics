import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Hexbin2.csv")
print(df)

#contour([X, Y,] Z, [levels], **kwargs)

plt.subplot(1,2,1)
plt.contour([df["coord_x"], df["coord_y"]])

#Use z as height
plt.subplot(1,2,2)
[x,y] = np.meshgrid(df["coord_x"], df["coord_y"])
z = np.cos(x/2) + np.sin(y/2)
plt.contour(x,y,z)
plt.show()