import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x=np.random.uniform(10,40,300)
y=np.random.uniform(100,200,300)
z=2*x+y
fig=plt.figure()
ax=Axes3D(fig)
ax.scatter(x,y,z,c='b',marker="*")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z=2X+Y")
plt.show()
