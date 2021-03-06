# 3D图形的绘制；
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, R,cmap=cm.viridis)
ax.view_init(azim=-45,elev=30)
plt.tight_layout()
plt.show()
# cmap=cm.viridis,rstride=1, cstride=1,