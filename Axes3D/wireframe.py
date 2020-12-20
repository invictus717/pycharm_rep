import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x=np.arange(1,10,0.5)
y=np.arange(1,10,0.5)
X,Y=np.meshgrid(x,y)
Z=2*X+Y

fig=plt.figure()
ax=Axes3D(fig)
ax.plot_wireframe(X,Y,Z,color='m',linewidth=0.55)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z=2X+Y")

plt.show()