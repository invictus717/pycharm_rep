import matplotlib.pyplot as plt
import numpy as np

# 生成数据
t = np.arange(0.0, 2.0, 0.01)
s1 = np.sin(2*np.pi*t)
s2 = np.sin(4*np.pi*t)

#定义一个图像窗口
plt.figure(1)

#将图形定义为2行1列，当前位置为1
plt.subplot(211)
plt.plot(t, s1)

#将图形定义为2行1列，当前位置为2
plt.subplot(212)
plt.plot(t, 2*s1)

#显示图像
plt.show()



#将图形定义为2行2列，当前位置为1
plt.subplot(221)
plt.plot(t, s1)

#将图形定义为2行2列，当前位置为2
plt.subplot(222)
plt.plot(t, 2*s1)

#将图形定义为2行2列，当前位置为3
plt.subplot(223)
plt.plot(t, 3*s1)

#将图形定义为2行2列，当前位置为4
plt.subplot(224)
plt.plot(t, 4*s1)

#显示图像
plt.show()