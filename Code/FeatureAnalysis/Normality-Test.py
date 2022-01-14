# 正态性检验

from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

# 直方图初判
# s = pd.DataFrame(np.random.randn(1000) + 10, columns=['value'])

# fig = plt.figure(figsize=(10, 6))
# ax1 = fig.add_subplot(2, 1, 1)
# ax1.scatter(s.index, s.values)
# plt.grid()

# ax2 = fig.add_subplot(2, 1, 2)
# s.hist(bins=30, alpha=0.5, ax=ax2)
# s.plot(kind='kde', secondary_y=True, ax=ax2)
# plt.grid()

# plt.show()

# QQ图判断
# s = pd.DataFrame(np.random.randn(1000) + 10, columns=['value'])
# 计算均值，标准差
# mean = s['value'].mean()
# std = s['value'].std()

# s.sort_values(by='value', inplace=True)
# s_r = s.reset_index(drop=False)
# s_r['p'] = (s_r.index - 0.5) / len(s_r)
# s_r['q'] = (s_r['value'] - mean) / std

# 计算四分之一位数、四分之三位数
# st = s['value'].describe()
# x1, y1 = 0.25, st['25%']
# x2, y2 = 0.75, st['75%']

# fig = plt.figure(figsize=(10, 9))
# ax1 = fig.add_subplot(3, 1, 1)
# ax1.scatter(s.index, s.values)
# plt.grid()

# ax2 = fig.add_subplot(3, 1, 2)
# s.hist(bins=30, alpha=0.5, ax=ax2)
# s.plot(kind='kde', secondary_y=True, ax=ax2)
# plt.grid()

# ax3 = fig.add_subplot(3, 1, 3)
# ax3.plot(s_r['p'], s_r['value'], 'k.', alpha=0.1)
# ax3.plot([x1, x2], [y1, y2], '-r')
# plt.grid()

# plt.show()

# KS检验，理论推导
# data = [87, 77, 92, 68, 80, 78, 84, 77, 81, 80, 80, 77, 92, 86,
#         76, 80, 81, 75, 77, 72, 81, 72, 84, 86, 80, 68, 77, 87,
#         76, 77, 78, 92, 75, 80, 78]
# df = pd.DataFrame(data, columns=['value'])
# u = df['value'].mean()
# std = df['value'].std()

# 创建频率数据
# s = df['value'].value_counts().sort_index()
# df_s = pd.DataFrame({'血糖浓度': s.index, '次数': s.values})

# df_s['累计次数'] = df_s['次数'].cumsum()
# df_s['累计频率'] = df_s['累计次数'] / len(data)
# df_s['标准化取值'] = (df_s['血糖浓度'] - u) / std
# df_s['理论分布'] = [0.0244, 0.0968, 0.2148, 0.2643, 0.3228,
#                 0.3859, 0.5160, 0.5832, 0.7611, 0.8531, 0.8888, 0.9803]
# df_s['D'] = np.abs(df_s['累计频率'] - df_s['理论分布'])
# dmax = df_s['D'].max()

# df_s['累计频率'].plot(style='--k.')
# df_s['理论分布'].plot(style='--r.')
# plt.legend(loc='upper left')
# plt.grid()

# plt.show()

# 直接用算法做KS检验

# scipy包是一个高级的科学计算库，它和Numpy联系很密切，Scipy一般都是操控Numpy数组来进行科学计算
data = [87, 77, 92, 68, 80, 78, 84, 77, 81, 80, 80, 77, 92, 86,
        76, 80, 81, 75, 77, 72, 81, 72, 84, 86, 80, 68, 77, 87,
        76, 77, 78, 92, 75, 80, 78]

df = pd.DataFrame(data, columns=['value'])
u = df['value'].mean()
std = df['value'].std()
res = stats.kstest(df['value'], 'norm', (u, std))
print(res.pvalue)