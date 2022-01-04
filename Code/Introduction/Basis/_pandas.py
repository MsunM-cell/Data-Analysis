import pandas as pd
from pandas.core import series
import numpy as np

data = pd.read_csv('Pokemon.csv')

series = data['Defense']
print(type(series))
data_frame = data[['Defense']]
print(type(data_frame))

# print(series)
# print(data_frame)

# 过滤数据
x = data['Defense'] > 200
print(data[x])
print(data[np.logical_and(data['Defense']>200, data['Attack']>100)])

# 在pandas里，我们可以使用for循环显示索引和值
for index,value in data[['Attack']][0:10].iterrows():
    print(index," : ",value)