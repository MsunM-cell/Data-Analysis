from scipy.interpolate import lagrange
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# 连续属性变换成分类属性，即连续属性离散化

# 等宽法 → 将数据均匀划分成n等份，每份的间距相等
# cut方法
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]

bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
# print(cats)
# print(type(cats))

# print(cats.codes, type(cats.codes))
# print(cats.categories, type(cats.categories))
# print(pd.value_counts(cats))

# print(pd.cut(ages, [18, 26, 36, 61, 100], right=False))

# group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
# print(pd.cut(ages, bins, labels=group_names))

# df = pd.DataFrame({'ages': ages})
# group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
# s = pd.cut(df['ages'], bins)
# df['label'] = s
# cut_counts = s.value_counts(sort=False)
# print(df)
# print(cut_counts)

# plt.scatter(df.index, df['ages'], cmap='Reds', c=cats.codes)
# plt.grid()

# 等频法 - 以相同数量的记录放进每个区间
# qcut方法

data = np.random.randn(1000)
s = pd.Series(data)

cats = pd.qcut(s, 4)
# print(cats)
# print(cats.head())
# print(pd.value_counts(cats))

plt.scatter(s.index, s, cmap='Greens', c=pd.qcut(data, 4).codes)
plt.grid()
plt.show()