#使用numpy库生成数组
import numpy as np
import matplotlib.pyplot as plt
a=np.arange(0.0,5.0,0.02)
b=np.cos(2*np.pi*a)

#作图
plt.plot(a,b)

#添加横纵坐标中文信息
plt.xlabel('时间',fontproperties='SimHei',fontsize=20)
plt.ylabel('振幅',fontproperties='SimHei',fontsize=20)
plt.title('正弦波',fontproperties='SimHei',fontsize=20)

#添加网格
plt.grid(True)

#显示图形
plt.show()