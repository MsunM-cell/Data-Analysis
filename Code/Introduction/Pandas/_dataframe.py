import pandas as pd

# 从字典中构建dataframe
country = ['Spain', 'France']
population = ['11', '12']
list_label = ['country', 'population']
list_col = [country, population]

zipped = list(zip(list_label, list_col))
# print(zipped)
data_dict = dict(zipped)
# print(data_dict)
df = pd.DataFrame(data_dict)
# print(df)

# 添加新列
df['capital'] = ['madrid', 'paris']
# print(df)

# 广播（Broadcasting）
df['income'] = 0
print(df)
