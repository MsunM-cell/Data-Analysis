# def f():
#     """hello world"""
#     print('hello world')

# def tuble_ex():
#     """return defined t tuple"""
#     t = (1, 2, 3)
#     return t

# a, b, c = tuble_ex()
# print(a, b, c)
# # print注释内容
# print(tuble_ex.__doc__)

# help(tuble_ex)

# def f(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ' ', value)

# f(country = 'spain', capital = 'madrid', population = 123456)

# square = lambda x: x**2
# print(square(4))

# number_list = [1, 2, 3]
# map(func, seq): 对列表中的所有项应用函数
# y = map(lambda x: x**2, number_list)
# print(list(y))

# name = 'abcdef'
# it = iter(name)
# print(next(it))
# print(it)
# print(*it)

# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# z = zip(list1, list2)
# print(z)
# z_list = list(z)
# print(z_list)

# un_zip = zip(*z_list)
# un_list1, un_list2 = list(un_zip)
# print(un_list1)
# print(un_list2)
# print(type(un_list2))
# print(list(un_list1))

import numpy as np
import pandas as pd

data = pd.read_csv('./Introduction/Basis/Pokemon.csv')

threshold = sum(data.Speed) / len(data.Speed)
data['speed_level'] = ['high' if i > threshold else 'low' for i in data.Speed]
print(data.loc[:8, ['speed_level', 'Speed']])
