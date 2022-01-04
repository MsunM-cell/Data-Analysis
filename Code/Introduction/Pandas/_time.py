# time_list = ["1992-03-08","1992-04-12"]
# print(type(time_list[1])) # 此时日期是str类型
# # 我们希望能将它变为datatime类型
# datetime_object = pd.to_datetime(time_list)
# print(datetime_object)

import pandas as pd
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('./Introduction/Basis/Pokemon.csv')

data2 = data.head()
date_list = ["1992-01-10","1992-02-10","1992-03-10","1993-03-15","1993-03-16"]
datetime_object = pd.to_datetime(date_list)
data2['date'] = datetime_object
# 设置日期作为索引
data2 = data2.set_index('date')
# print(data2)

# print(data2.loc["1993-03-16"])
# print(data2.loc["1992-03-10":"1993-03-16"])

print(data2.resample('Y').mean())