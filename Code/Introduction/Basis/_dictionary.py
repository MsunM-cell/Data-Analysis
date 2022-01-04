# 创建一个字典
dictionary = {'spain': 'madrid', 'usa': 'vegas'}

# 打印字典中的keys和values
print(dictionary.keys())
print(dictionary.values())

dictionary['spain'] = 'barcelona'
print(dictionary)
dictionary['france'] = 'paris'
print(dictionary)
del dictionary['spain'] # 删除键是'spain'的条目
print(dictionary)
print('france' in dictionary)
dictionary.clear() # 清空字典所有条目
print(dictionary)