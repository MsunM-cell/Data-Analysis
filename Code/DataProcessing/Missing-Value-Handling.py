# 缺失值处理

from scipy.interpolate import lagrange
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

s = pd.Series([12, 33, 45, 23, np.nan, np.nan, 66, 54, np.nan, 99])
df = pd.DataFrame({'value1': [12, 33, 45, 23, np.nan, np.nan, 66, 54, np.nan, 99, 190],
                  'value2': ['a', 'b', 'c', 'd', 'e', np.nan, np.nan, 'f', 'g', np.nan, 'g']})

# print(s.isnull())
# print(df.notnull())
# print(df['value1'].notnull())

# 筛选非缺失值
s2 = s[s.isnull() == False]
df2 = df[df['value2'].notnull()]

### 删除缺失值 - dropna
# s.dropna(inplace=True)
# df2 = df['value1'].dropna()

# 填充/替换缺失数据 - fillna、replace
s.fillna(0, inplace=True)
df['value1'].fillna(method='pad', inplace=True)

s = pd.Series([1, 1, 1, 1, 2, 2, 2, 3, 4, 5,
              np.nan, np.nan, 66, 54, np.nan, 99])
s.replace(np.nan, '缺失数据', inplace=True)
s.replace([1, 2, 3], np.nan, inplace=True)

# 缺失值插补
# 几种思路：均值/中位数/众数插补，临近值插补、插值法
# （1）均值/中位数/众数插补
s = pd.Series([1, 2, 3, np.nan, 3, 4, 5, 5, 5, 5, np.nan,
              np.nan, 6, 6, 7, 12, 2, np.nan, 3, 4])

u = s.mean()
me = s.median()
mod = s.mode()

# 用均值填补
s.fillna(u, inplace=True)

# （2）临近值插补
# 用前值插补
s.fillna(method='ffill', inplace=True)

# （3）拉格朗日插值法
x = [3, 6, 9]
y = [10, 8, 4]
# print(lagrange(x, y)(10))

# （3）拉格朗日插值法，实际运用
data = pd.Series(np.random.rand(100) * 100)
data[6, 33, 56, 45, 66, 67, 80, 90] = np.nan
# 缺失数据
data_na = data[data.isnull()]
# 中位数填充缺失值
data_c = data.fillna(data.median())

fig, axes = plt.subplots(1, 4, figsize=(20, 5))
data.plot.box(ax=axes[0], grid=True, title='数据分布')
data.plot(kind='kde', style='--r',
          ax=axes[1], grid=True, title='删除缺失值', xlim=[-50, 150])
data_c.plot(kind='kde', style='--b',
            ax=axes[2], grid=True, title='缺失值填充中位数', xlim=[-50, 150])


def na_c(s, n, k=5):
    y = s[list(range(n - k, n + k + 1))]
    y = y[y.notnull()]
    return (lagrange(y.index, list(y))(n))


na_re = []
for i in range(len(data)):
    if data.isnull()[i]:
        data[i] = na_c(data, i)
        na_re.append(data[i])

# 清除插值后仍存在的缺失值
data.dropna(inplace=True)
data.plot(kind='kde', style='--k',
          ax=axes[3], grid=True, title='拉格朗日插值后', xlim=[-50, 150])

plt.show()
