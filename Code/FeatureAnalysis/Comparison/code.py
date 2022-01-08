import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.io.formats import style

# data = pd.DataFrame(np.random.rand(
#     30, 2) * 1000, columns=['A_sale', 'B_sale'], index=pd.period_range('20170601', '20170630'))

# print(data.head())

# data.plot(kind='line', style='--.', alpha=0.8, figsize=(10, 3), title='AB产品销量对比-折线图')
# data.plot(kind='bar', width=0.8, alpha=0.8, figsize=(10, 3), title='AB产品销量对比-折线图')

# plt.show()

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

# fig3 = plt.figure(figsize=(10, 6))
# plt.subplots_adjust(hspace=0.3)
# # 创建子图及间隔设置

# ax1 = fig3.add_subplot(2, 1, 1)
# x = range(len(data))
# y1 = data['A_sale']
# y2 = -data['B_sale']
# plt.bar(x, y1, width=1, facecolor='yellowgreen')
# plt.bar(x, y2, width=1, facecolor='lightskyblue')
# plt.title('AB产品销量对比-堆叠图')
# plt.grid()
# plt.xticks(range(0, 30, 6))
# ax1.set_xticklabels(data.index[::6])

# ax2 = fig3.add_subplot(2, 1, 2)
# y3 = data['A_sale'] - data['B_sale']
# plt.plot(x, y3, '--go')

# plt.grid()
# plt.title('AB产品销量对比-差值折线')
# plt.xticks(range(0, 30, 6))
# ax2.set_xticklabels(data.index[::6])

# plt.show()

data = pd.DataFrame({'A_sale': np.random.rand(30) * 1000,
                    'B_sale': np.random.rand(30) * 200},
                    index=pd.period_range('20170601', '20170630'))

# 结构分析
# 计算每天的营收占比
# data['A_per'] = data['A_sale'] / data['A_sale'].sum()
# data['B_per'] = data['B_sale'] / data['B_sale'].sum()

# # 转换为百分数
# data['A_per%'] = data['A_per'].apply(lambda x: '%.2f%%' % (x * 100))
# data['B_per%'] = data['B_per'].apply(lambda x: '%.2f%%' % (x * 100))

# fig, axes = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
# data[['A_sale', 'B_sale']].plot(kind='line', style='--.', alpha=0.8, ax=axes[0])
# axes[0].legend(loc='upper right')

# data[['A_per', 'B_per']].plot(kind='line', style='--.', alpha=0.8, ax=axes[1])
# axes[1].legend(loc='upper right')

# plt.show()

# 比例分析
# data = pd.DataFrame({'consumption':np.random.rand(12)*1000 + 2000,
#                     'salary':np.random.rand(12)*500 + 5000},
#                    index = pd.period_range('2017/1','2017/12',freq = 'M'))
# print(data.head())
# print('------')
# # 创建数据 → 某人一年内的消费、工资薪水情况
# # 消费按照2000-3000/月随机，工资按照5000-5500/月随机

# data['c_s'] = data['consumption'] / data['salary']
# print(data.head())
# # 比例相对数 → 消费收入比

# data['c_s'].plot.area(color = 'green',alpha = 0.5,ylim = [0.3,0.6],figsize=(8,3),grid=True)
# # 创建面积图表达

# plt.show()

# 空间比较分析（横向对比分析）
# data = pd.DataFrame({'A': np.random.rand(30) * 5000,
#                     'B': np.random.rand(30) * 2000,
#                      'C': np.random.rand(30) * 10000,
#                      'D': np.random.rand(30) * 800},
#                     index=pd.period_range('20170601', '20170630'))
# data.sum().plot(kind='bar', color=['r', 'g', 'b', 'k'], alpha=0.8, grid=True)
# for i, j in zip(range(4), data.sum()):
#     plt.text(i - 0.25, j + 2000, '%.2f' % j, color='k')

# data[:10].plot(kind='bar', color=['r', 'g', 'b', 'k'],
#                alpha=0.8, grid=True, figsize=(12, 4), width=0.8)

# 动态对比分析（纵向对比分析）
# 同一现象在不同时间上的指标数值进行对比，反应现象的数量随着时间推移而发展变动的程度及趋势
# 最基本方法，计算动态相对数->发展速度
# 动态相对数 = 某一现象的报告期数值 / 同一现象的基期数值
# 基期：用来比较的基础时期
# 报告期：所要研究的时期，又称计算期

data = pd.DataFrame({'A': np.random.rand(30) * 2000 + 1000},
                    index=pd.period_range('20170601', '20170630'))

data['base'] = 1000
data['l_growth'] = data['A'] - data['base']
data['z_growth'] = data['A'] - data.shift(1)['A']
data[data.isnull()] = 0 # 替换缺失值

data[['l_growth', 'z_growth']].plot(figsize=(10, 4), style='--.', alpha=0.8)
plt.legend(loc='lower left')
plt.grid()
# 通过折线图查看增长量情况

data['lspeed'] = data['l_growth'] / data['base']
data['zspeed'] = data['z_growth'] / data.shift(1)['A']
data[['lspeed','zspeed']].plot(figsize = (10,4),style = '--.',alpha = 0.8)  

plt.grid()
plt.show()