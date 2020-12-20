import tensorflow as tf
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

n=200
x=np.linspace(-10,10,n)
y=np.linspace(-10,10,n)

X,Y=np.meshgrid(x,y)
Z=X**2+Y**2

plt.contourf(X,Y,Z,20,cmap='rainbow')

plt.show()