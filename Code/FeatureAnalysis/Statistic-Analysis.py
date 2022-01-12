import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False


# 1、集中趋势度量
# 指一组数据向某一中心靠拢的倾向，核心在于寻找数据的代表值或中心值 —— 统计平均数
# 算数平均数、位置平均数
# （1）算数平均数
# data = pd.DataFrame({'value': np.random.randint(
#     100, 120, 100), 'f': np.random.rand(100)})
# data['f'] = data['f'] / data['f'].sum()

# mean = data['value'].mean()
# print('简单算数平均值为：%.2f' % mean)

# mean_w = (data['value'] * data['f']).sum() / data['f'].sum()
# print('加权算数平均值为：%.2f' % mean_w)

# （2）位置平均数
# m = data['value'].mode()
# print('众数为：', m.tolist())

# med = data['value'].median()
# print('中位数为%i' % med)

# data['value'].plot(kind='kde', style='--k', grid=True)
# plt.axvline(mean, color='r', linestyle='--', alpha=0.8)
# plt.text(mean + 5, 0.005, '简单算数平均值为：%.2f' % mean, color='r')

# plt.axvline(mean_w, color='b', linestyle="--", alpha=0.8)
# plt.text(mean + 5, 0.01, '加权算数平均值：%.2f' % mean_w, color='b')

# plt.axvline(med, color='g', linestyle="--", alpha=0.8)
# plt.text(mean + 5, 0.015, '中位数：%i' % med, color='g')
# plt.show()

# 2、离中趋势度量
# （1）极差、分位差
data = pd.DataFrame({'A_sale': np.random.rand(
    30) * 1000, 'B_sale': np.random.rand(30) * 1000}, index=pd.period_range('20170601', '20170630'))

a_r = data['A_sale'].max() - data['B_sale'].min()
b_r = data['B_sale'].max() - data['B_sale'].min()
print('A销售额的极差为：%.2f, B销售额的极差为：%.2f' % (a_r, b_r))

sta = data['A_sale'].describe()
stb = data['B_sale'].describe()
print(sta)

a_iqr = sta.loc['75%'] - sta.loc['25%']
b_iqr = stb.loc['75%'] - stb.loc['25%']
print('A销售额的分位差为：%.2f, B销售额的分位差为：%.2f' % (a_iqr, b_iqr))

# color = dict(boxes='DarkGreen', whiskers='DarkOrange',
#              medians='DarkBlue', caps='Gray')
# data.plot.box(vert=False, grid=True, color=color, figsize=(10, 3))
# plt.show()

# （2）方差与标准差
a_std = sta.loc['std']
b_std = stb.loc['std']
a_var = data['A_sale'].var()
b_var = data['B_sale'].var()
print('A销售额的标准差为：%.2f, B销售额的标准差为：%.2f' % (a_std, b_std))
print('A销售额的方差为：%.2f, B销售额的方差为：%.2f' % (a_var, b_var))

fig = plt.figure(figsize=(12, 4))
ax1 = fig.add_subplot(1, 2, 1)
data['A_sale'].plot(kind='kde', style='k--', grid=True, title='A密度曲线')
plt.axvline(sta.loc['50%'], color='r', linestyle="--", alpha=0.8)
plt.axvline(sta.loc['50%'] - a_std, color='b', linestyle="--", alpha=0.8)
plt.axvline(sta.loc['50%'] + a_std, color='b', linestyle="--", alpha=0.8)

ax2 = fig.add_subplot(1, 2, 2)
data['B_sale'].plot(kind='kde', style='k--', grid=True, title='B密度曲线')
plt.axvline(stb.loc['50%'], color='r', linestyle='--', alpha=0.8)
plt.axvline(stb.loc['50%'] - b_std, color='b', linestyle="--", alpha=0.8)
plt.axvline(stb.loc['50%'] + b_std, color='b', linestyle="--", alpha=0.8)

plt.show()
