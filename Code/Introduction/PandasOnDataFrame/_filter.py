import pandas as pd

data = pd.read_csv('./Introduction/Basis/Pokemon.csv')

# 创建一个布尔序列
boolean = data.HP > 200
print(data[boolean])

# 多重过滤
first_filter = data.HP > 200
second_filter = data.Speed > 35
print(data[first_filter & second_filter])

# 基于其它过滤列的过滤
data.HP[data.Speed < 20]