import pandas as pd

data = pd.read_csv('./Introduction/Basis/Pokemon.csv')
# data = data.set_index('#')

# 方括号索引
# print(data['HP'][1])

# 使用列属性和行标签
# print(data.HP[1])

# 使用loc访问器
# print(data.loc[1, ['HP']])

# 只选取某些列
# print(data[['HP', 'Attack']])

# data.index.name = 'index_name'
# print(data.index.name)

# data3 = data.copy()
# data3.index = range(100, 900, 1)
# print(data3.head())

# 我们可以设置其中一列作为索引
# data = data.set_index('#')
# # 或者
# data.index = data['#']

# 分级索引
# 设置索引：type 1是外部索引，type 2是内部索引
# data1 = data.set_index(['Type 1', 'Type 2'])
# print(data1.head(20))

dic = {"treatment":["A","A","B","B"],"gender":["F","M","F","M"],"response":[10,45,5,9],"age":[15,4,72,65]}
df1 = pd.DataFrame(dic)
# mean sum std max min
print(df1.groupby('treatment').max())