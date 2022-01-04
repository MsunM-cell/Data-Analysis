import pandas as pd

data = pd.read_csv('./Introduction/Basis/Pokemon.csv')

# 使用普通函数
def div(n):
    return n / 2

# print(data.HP.apply(div))

# 使用Lambda函数
# data.HP.apply(lambda n: n / 2)

# 使用其他列创建新列
# data['total_power'] = data.Attack + data.Defense
# print(data.head())


