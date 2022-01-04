import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Introduction/Basis/Pokemon.csv')

# print(data.describe())

# data.boxplot(column='Attack',by='Legendary')
# plt.show()

# data_new = data[10:15]
# melted = pd.melt(data_new, id_vars='Name', value_vars=['Attack', 'Defense', 'Speed'])
# print(melted.pivot(index = 'Name', columns = 'variable',values='value'))

# data1 = data.head(3)
# data2 = data.tail(3)
# conc_data = pd.concat([data1, data2], axis=0, ignore_index=True)
# print(conc_data)

# print(type(data['Attack'].head(3)))
# print(data.dtypes)

# 将str转化成categorical，将int转化成float
# data['Type 1'] = data['Type 1'].astype('category')
# data['Speed'] = data['Speed'].astype('float')
# print(data.dtypes)

# 看一下pokemon数据集是否存在NaN值
# print(data.info())
# print(data['Type 2'].value_counts(dropna=False))

# data1 = data
# data1.dropna(inplace=False)
# print(data1.dropna().head(6))

# print(data1.head(6))

# assert data1['Type 2'].notnull().all()

# data['Type 2'].fillna('empty', inplace=False)
# print(data.head(6))

# print(data.Speed.dtypes)
# assert data.Speed.dtypes == np.int