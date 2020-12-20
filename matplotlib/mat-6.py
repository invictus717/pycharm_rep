
import matplotlib.pyplot as plt


import numpy as np


import  matplotlib as mpl

x = np.linspace(0, 1, 100)
y = 2* np.pi * x

x1 = 30 * np.random.rand(100)
y1 = 2 * np.pi * np.random.rand(100)
colors = np.random.rand(100)
size = 50 * x1

ax = plt.subplot(121, polar=True)
ax.plot(x, y, color="r", linestyle="-", linewidth=2)

ax1 = plt.subplot(122, polar=True)
ax1.scatter(x1, y1, s=size, c=colors, cmap=mpl.cm.PuOr, marker="*")

plt.show()
