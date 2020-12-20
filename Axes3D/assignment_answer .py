import numpy as np
from scipy import stats
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def draw (sample_num):
    d = np.random.randn(sample_num,2)
    N = 45
    d= np.histogramdd(d, bins=[N, N])[0]
    d /= d.max()
    x = y = np.arange(N)
    X,Y = np.meshgrid(x, y)
    fig = plt.figure(num="Sample_num:{}".format(sample_num))
    ax= Axes3D(fig)
    ax.plot_wireframe(X, Y, d, color='b',linewidth=0.32)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()
if __name__=='__main__':
    draw(100)
    draw(10000)
    draw(1000000)