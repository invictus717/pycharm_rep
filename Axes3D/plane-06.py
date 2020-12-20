import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure(figsize=(40,30))
#定义新的三维坐标轴
ax3 = plt.axes(projection='3d')
xx = np.arange(-20,20,0.5)
yy = np.arange(-20,20,0.5)
X, Y = np.meshgrid(xx, yy)#将两个一维数组变为二维矩阵
Z = X*Y**2
ax3.plot_surface(X,Y,Z,rstride = 1, cstride = 1,cmap='rainbow')
plt.savefig('1.png',dpi=80)
plt.show()
