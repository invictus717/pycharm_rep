import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x=np.arange(-5,5,0.1)
y=np.arange(-5,5,0.1)
X,Y=np.meshgrid(x,y)
Z=np.sin(np.sqrt(X**2+Y**2))

fig=plt.figure()
ax=Axes3D(fig)
ax.plot_surface(X,Y,Z,cmap='rainbow')

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z=2X+Y")

plt.show()