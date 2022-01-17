from cProfile import label
from tkinter.ttk import Style
from scipy.interpolate import lagrange
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# 异常值也称为离群点

# 异常值分析
# （1）如果数据服从正态分布，则 p(|x - μ| > 3σ) ≤ 0.003
data = pd.Series(np.random.randn(10000) * 100)

# u = data.mean()
# std = data.std()

# fig = plt.figure(figsize=(10, 6))
# ax1 = fig.add_subplot(2, 1, 1)
# data.plot(kind='kde', grid=True, style='--k', title='density curve')

# ax2 = fig.add_subplot(2, 1, 2)
# error = data[np.abs(data - u) > 3 * std]
# data_c = data[np.abs(data - u) <= 3 * std]
# rate = (len(error) / len(data)) * 100
# print('outlier %.2f%% in all' % rate)

# plt.scatter(data_c.index, data_c, color='k', marker='.', alpha=0.3)
# plt.scatter(error.index, error, color='r', marker='.', alpha=0.5)
# plt.xlim([-10, 10010])
# plt.grid()

# （2）箱型图分析
fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(2, 1, 1)
color = dict(boxes='DarkGreen', whiskers='DarkOrange',
             medians='DarkBlue', caps='Gray')
data.plot.box(vert=False, grid=True, color=color, ax=ax1, label='sample data')

s = data.describe()
q1 = s['25%']
q3 = s['75%']
iqr = q3 - q1
mi = q1 - 1.5 * iqr
ma = q3 + 1.5 * iqr

ax2 = fig.add_subplot(2, 1, 2)
error = data[(data < mi) | (data > ma)]
data_c = data[(data >= mi) & (data <= ma)]

plt.scatter(data_c.index, data_c, color='k', marker='.', alpha=0.3)
plt.scatter(error.index, error, color='r', marker='.', alpha=0.5)
plt.xlim([-10, 10010])
plt.grid()

plt.show()