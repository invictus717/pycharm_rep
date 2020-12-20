# 1
#导入 matplotlib.pyplot模块，并起一个别名：plt
import matplotlib.pyplot  as plt
import numpy as np
# rang(n,m)，生成m-n各整数 ，不包含m
# 只输入一个列表或者数组使，参数被当作Y轴，X轴索引自动生成

plt.plot(range(1,6))
plt.plot(range(11,16))

# 添加横纵坐标的名称
plt.ylabel("passerby")
plt.xlabel("order")

### 设置x轴和y轴坐标范围
plt.xlim((-1,6))
plt.ylim((-5,17))

#显示图形
plt.show()

#保存图片到默认文件，默认格式为PNG，dpi像素
plt.savefig('passerby-1',dpi=600) 