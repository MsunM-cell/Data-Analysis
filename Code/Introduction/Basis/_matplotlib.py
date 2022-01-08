import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O
import matplotlib.pyplot as plt
import seaborn as sns  # visualization tool

# 使用pandas从数据集中的csv文件写入数据
data = pd.read_csv('Pokemon.csv')

# 线图
# 绘制两条曲线，Speed和Defense；分别定义颜色，线宽，不透明度，网格，线型等属性
# data.Speed.plot(kind='line', color='blue', label='Speed',
#                 linewidth=1, alpha=0.5, grid=True, linestyle=':')
# data.Defense.plot(color='red', label='Defense', linewidth=1,
#                   alpha=0.5, grid=True, linestyle='-')

# plt.legend(loc='upper right')  # 在图像中显示标签
# plt.xlabel('x axis')  # 定义x轴名称
# plt.ylabel('y axis')  # 定义y轴名称
# plt.title('Line Plot')  # 定义图像名称
# plt.show()  # 显示图像

# 散点图
# x = attack, y = defense
# data.plot(kind='scatter', x='Attack', y='Defense', alpha=0.5, color='red')
# plt.xlabel('Attack')
# plt.ylabel('Defense')
# plt.title('Attack Defense Scatter Plot')
# plt.show()

# 直方图
# bins = 直方图中竖条区域的个数，这里我们设置为10个
# data.Speed.plot(kind='hist', bins=10, figsize=(6, 5))
# plt.show()
# plt.clf()


