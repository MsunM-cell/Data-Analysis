from os import rename
import pandas as pd
# from IPython.display import display
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# 数据读取
data = pd.read_csv(
    'D:/2022一定会/Data-Analysis/Code/FeatureAnalysis/Distribution/second_hand_house.csv')
# plt.scatter(data['经度'], data['纬度'],  # 按照经纬度显示
#             s=data['房屋单价']/500,  # 按照单价显示大小
#             c=data['参考总价'],  # 按照总价显示颜色
#             alpha=0.4, cmap='Reds')

# plt.grid()
# print(data.dtypes)
# print('-------\n数据长度为%i条' % len(data))
# print(data.head())
# plt.show()


# def d_range(df, *cols):
#     krange = []
#     for col in cols:
#         crange = df[col].max() - df[col].min()
#         krange.append(crange)
#     return (krange)
# # 创建函数求极差


# key1 = '参考首付'
# key2 = '参考总价'
# dr = d_range(data, key1, key2)
# # print('%s极差为 %f \n%s极差为 %f' % (key1, dr[0], key2, dr[1]))
# # 求出数据对应列的极差

# # 频率分布情况 - 定量字段

# # 1 通过直方图直接判断分组组数
# # 简单查看数据分布，确定分组数
# # data[key2].hist(bins=10)
# # plt.show()

# # 2 求出分组区间
# gcut = pd.cut(data[key2], 10, right=False)
# gcut_count = gcut.value_counts(sort=False)  # 不排序
# data['%s分组区间' % key2] = gcut.values
# # print(gcut.head(), '\n-------')
# # print(gcut_count)
# # print(data.head())

# # 3 求出目标字段下频率分布的其它统计量
# r_zj = pd.DataFrame(gcut_count)
# r_zj.rename(columns={gcut_count.name: '频数'}, inplace=True)
# r_zj['频率'] = r_zj / r_zj['频数'].sum()
# r_zj['累计频率'] = r_zj['频率'].cumsum()
# r_zj['频率%'] = r_zj['频率'].apply(lambda x: "%.2f%%" % (x*100))
# r_zj['累计频率%'] = r_zj['累计频率'].apply(lambda x: "%.2f%%" % (x*100))
# s = r_zj.style.bar(subset=['频率', '累计频率'], color='green', width=100)

# # 4 绘制频率直方图
# r_zj['频率'].plot(kind='bar', width=0.8, figsize=(15, 2),
#                 rot=0, color='k', grid=True, alpha=0.5)
# plt.title('参考总价分布频率直方图')

# x = len(r_zj)
# y = r_zj['频率']
# m = r_zj['频数']
# for i, j, k in zip(range(x), y, m):
#     plt.text(i - 0.1, j + 0.01, '%i' % k, color='k')
# # 添加频数标签

# # 解决中文乱码问题
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

# plt.show()

# 频率分布情况 - 定性字段
# 1 通过计数统计判断不同类别的频率

cx_g = data['朝向'].value_counts(sort=True)
print(cx_g)

r_cx = pd.DataFrame(cx_g)
r_cx.rename(columns={cx_g.name: '频数'}, inplace=True)
r_cx['频率'] = r_cx / r_cx['频数'].sum()

# 2 绘制频率直方图、饼图
plt.figure(num=1, figsize=(12, 2))
r_cx['频率'].plot(kind='bar',
                  width=0.8,
                  rot=0,
                  color='k',
                  grid=True,
                  alpha=0.5)
plt.title('朝向分布频率直方图')

plt.figure(num=2)
plt.pie(r_cx['频数'],
        labels=r_cx.index,
        autopct='%.2f%%',
        shadow=True)

plt.axis('equal')
plt.show()