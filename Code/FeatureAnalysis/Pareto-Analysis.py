# 帕累托分析
# 一个思路：通过二八原则，去寻找关键的那20%决定性因素！

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.Series(np.random.randn(10) * 1200 + 3000, index=list('ABCDEFGHIJ'))

# 由大到小排列
data.sort_values(ascending=False, inplace=True)

plt.figure(figsize=(10, 4))
data.plot(kind='bar', color='g', alpha=0.5, width=0.7)
plt.ylabel('revenue')

# 创建累计占比，Series
p = data.cumsum() / data.sum()
# 找到累计占比超过80%时候的index
key = p[p > 0.8].index[0]
# 找到key所对应的索引位置
key_num = data.index.tolist().index(key)

p.plot(style='--ko', secondary_y=True)
plt.axvline(key_num, color='r', linestyle='--', alpha=0.8)
plt.text(key_num + 0.2, p[key], 'cumulative-proporation: %.3f%%' % (p[key] * 100), color='r')
plt.ylabel('revenue-proporation')

plt.show()

# 核心产品
key_product = data.loc[:key]
print(key_product)