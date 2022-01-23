import numpy as np
import pandas as pd
import numpy.linalg as nlg
from math import sqrt
from numpy import eye, asarray, dot, sum, diag
from numpy.linalg import svd

# 初始化构建数据
data = pd.DataFrame(np.random.randint(50, 100, size=(5, 10)))
data.columns = ["特征1", "特征2", "特征3", "特征4",
                "特征5", "特征6", "特征7", "特征8", "特征9", "特征10"]
data.index = ['对象1', '对象2', '对象3', '对象4', '对象5']

# 将原始数据标准化处理
data = (data - data.mean()) / data.std()

# 计算相关系数矩阵
C = data.corr()
# print(C)

# 计算相关矩阵的特征值和特征向量
eig_value, eig_vector = nlg.eig(C)
eig = pd.DataFrame()
eig['names'] = data.columns
eig['eig_value'] = eig_value

# 确定公共因子个数
for k in range(1, 11):
    if eig["eig_value"][:k].sum() / eig["eig_value"].sum() >= 0.8:
        # print(k)
        # print(eig["eig_value"][:k].sum() / eig["eig_value"].sum())
        break

# 构造初始因子载荷矩阵
col0 = list(sqrt(eig_value[0])*eig_vector[:, 0])
col1 = list(sqrt(eig_value[1])*eig_vector[:, 1])
col2 = list(sqrt(eig_value[2])*eig_vector[:, 2])
A = pd.DataFrame([col0, col1, col2]).T
A.columns = ['factor1', 'factor2', 'factor3']
# print(A)

# 建立因子模型
h = np.zeros(10)  # 变量共同度，反映变量对共同因子的依赖程度，越接近1，说明公共因子解释程度越高，因子分析效果越好
D = np.mat(np.eye(10))  # 特殊因子方差，因子的方差贡献度 ，反映公共因子对变量的贡献，衡量公共因子的相对重要性
A = np.mat(A)  # 将因子载荷阵A矩阵化

for i in range(10):
    a = A[i, :]*A[i, :].T  # A的元的行平方和
    h[i] = a[0, 0]  # 计算变量X共同度,描述全部公共因子F对变量X_i的总方差所做的贡献，及变量X_i方差中能够被全体因子解释的部分
    D[i, i] = 1-a[0, 0]  # 因为自变量矩阵已经标准化后的方差为1，即Var(X_i)=第i个共同度h_i + 第i个特殊因子方差

# 对初始因子载荷矩阵A进行旋转变换
# 将因子表示成变量的线性组合


def varimax(Phi, gamma=1.0, q=10, tol=1e-6):  # 定义方差最大旋转函数
    p, k = Phi.shape  # 给出矩阵Phi的总行数，总列数
    R = eye(k)  # 给定一个k*k的单位矩阵
    d = 0
    for i in range(q):
        d_old = d
        Lambda = dot(Phi, R)  # 矩阵乘法

        u, s, vh = svd(dot(Phi.T, asarray(Lambda)**3 - (gamma/p) *
                       dot(Lambda, diag(diag(dot(Lambda.T, Lambda))))))  # 奇异值分解svd

        R = dot(u, vh)  # 构造正交矩阵R
        d = sum(s)  # 奇异值求和

    if d_old != 0 and d/d_old:
        return dot(Phi, R)  # 返回旋转矩阵Phi*R


rotation_mat = varimax(A)  # 调用方差最大旋转函数
rotation_mat = pd.DataFrame(rotation_mat)  # 数据框化
# print(rotation_mat)

# 计算因子得分
data = np.mat(data)  # 矩阵化处理
factor_score = (data).dot(A)  # 计算因子得分
factor_score = pd.DataFrame(factor_score)  # 数据框化
factor_score.columns = ['因子A', '因子B', '因子C']  # 对因子变量进行命名
factor_score.to_excel('a.xls')  # 打印输出因子得分矩阵
