from scipy.interpolate import lagrange
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# 数据标准化
# （1）0-1标准化
# x = (x - Min) / (Max- Min)

df = pd.DataFrame({'value1': np.random.rand(10) * 20,
                  'value2': np.random.rand(10) * 100})


def data_norm(df, *cols):
    df_n = df.copy()
    for col in cols:
        ma = df_n[col].max()
        mi = df_n[col].min()
        df_n[col + '_n'] = (df_n[col] - mi) / (ma - mi)
    return df_n

# df_n = data_norm(df, 'value1', 'value2')
# print(df_n.head())

# （2）Z-score标准化
# z = (x - μ) / σ

# def data_Znorm(df, *cols):
#     df_n = df.copy()
#     for col in cols:
#         u = df_n[col].mean()
#         std = df_n[col].std()
#         df_n[col + '_Zn'] = (df_n[col] - u) / std
#     return df_n

# df_z = data_Znorm(df, 'value1', 'value2')
# u_z = df_z['value1_Zn'].mean()
# std_z = df_z['value1_Zn'].std()
# 经过处理后的数据符合标准正态分布
# print(df_z)


# 案例应用
# 去除数据的单位限制
df = pd.DataFrame({"value1": np.random.rand(10) * 30,
                  'value2': np.random.rand(10) * 100},
                  index=list('ABCDEFGHIJ'))

df_n1 = data_norm(df, 'value1', 'value2')
df_n1['f'] = df_n1['value1_n'] * 0.6 + df_n1['value2_n'] * 0.4
df_n1.sort_values(by='f', inplace=True, ascending=False)
df_n1['f'].plot(kind='line', style='--.k', alpha=0.8, grid=True)

plt.show()