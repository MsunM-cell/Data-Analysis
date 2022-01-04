import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./Introduction/Basis/Pokemon.csv')

data1 = data.loc[:, ['Attack', 'Defense', 'Speed']]
# data1.plot(kind='scatter', x='Attack', y='Defense', color='red')
# plt.show()

# data1.plot(kind="hist", y="Defense", bins=50, range=(0, 250), density=True)
# plt.show()

# 统计直方图
# fig, axes = plt.subplots(nrows=2, ncols=1)
# data1.plot(kind="hist", y="Defense", bins=50,
#            range=(0, 250), density=True, ax=axes[0])
# # 累计直方图
# data1.plot(kind="hist", y="Defense", bins=50, range=(
#     0, 250), density=True, ax=axes[1], cumulative=True)
# plt.savefig('graph.png')
# plt.show()


