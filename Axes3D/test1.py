import numpy as np
from scipy import stats
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

sample_number=10000
x=np.random.randn(sample_number)
y=np.random.randn(sample_number)

x_mean=x.mean()
y_mean=y.mean()
x_sigma=np.std(x)
y_sigma=np.std(y)
stack_xy=np.vstack((x,y))
cov_x_y=np.cov(stack_xy)
# print(stack_xy.shape)
# print(cov_x_y)
relevent=cov_x_y/((x_sigma)*(y_sigma))
relevent=relevent[0,1]

X,Y=np.meshgrid(x,y)
k1=1/(2*np.pi*x_sigma*y_sigma)
k2=-1/2*(1-float(relevent)**2)
Z=((X-x_mean)**2/x_sigma**2)-(2*relevent(X-x_mean)*(Y-y_mean)/((x_sigma)*(y_sigma)))+((Y-y_mean)**2/y_sigma**2)
R=k1*np.exp(k2*Z)

fig=plt.figure()
ax=Axes3D(fig)
ax.plot_wireframe(X,Y,R)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.title("two-dimensional normal distribution")
plt.show()