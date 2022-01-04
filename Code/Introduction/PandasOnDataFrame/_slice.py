import pandas as pd

data = pd.read_csv('./Introduction/Basis/Pokemon.csv')

# print(data[['HP']])

# 用索引切片
# print(data.loc[:10, 'HP':'Defense'])

# 反向切片
# print(data.loc[10:1:-2, 'HP':'Attack'])

# 从某一列开始到最后一列
print(data.loc[1:10, 'Speed':])