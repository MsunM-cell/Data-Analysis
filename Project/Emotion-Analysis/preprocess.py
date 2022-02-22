import pandas as pd
import numpy as np
import re
import jieba.posseg as psg
import matplotlib.pyplot as plt
from wordcloud import WordCloud

import warnings
warnings.filterwarnings('ignore')

reviews = pd.read_csv('reviews.csv')
# print(reviews.shape)
# print(reviews.head())

# 评论去重
reviews = reviews[['content', 'content_type']].drop_duplicates()
content = reviews['content']

# 数据清洗
strinfo = re.compile('[0-9a-zA-Z]|京东|美的|电热水器|热水器|')
content = content.apply(lambda x: strinfo.sub('', x))

# 分词
worker = lambda s: [(x.word, x.flag) for x in psg.cut(s)]
seg_word = content.apply(worker)
# print(seg_word.head())

n_word = seg_word.apply(lambda x: len(x))
n_content = [[x + 1] * y for x, y in zip(list(seg_word.index), list(n_word))]

index_content = sum(n_content, [])
seg_word = sum(seg_word, [])

# 词 / 词性
word = [x[0] for x in seg_word]
nature = [x[1] for x in seg_word]

# 评论类型
content_type = [[x] * y for x, y in zip(list(reviews['content_type']), list(n_word))]
content_type = sum(content_type, [])
# print(content_type)

result = pd.DataFrame({"index_content": index_content,
                        "word": word,
                        "nature": nature,
                        "content_type": content_type})
# print(result.head())

# 删除标点符号
result = result[result['nature'] != 'x']
# 删除停用词
stop_path = open('stoplist.txt', 'r', encoding='UTF-8')
stop = stop_path.readlines()
stop = [x.replace('\n', '') for x in stop]
word = list(set(word) - set(stop))
result = result[result['word'].isin(word)]

# 构造各词在对应评论的位置列
n_word = list(result.groupby(by=['index_content'])['index_content'].count())
index_word = [list(np.arange(0, y)) for y in n_word]
# 词语在该评论中的位置
index_word = sum(index_word, [])
# 合并评论id
result['index_word'] = index_word

# 提取含有名词类的评论，即词性含有“n”的评论
ind = result[['n' in x for x in result['nature']]]['index_content'].unique()
result = result[[x in ind for x in result['index_content']]]

frequencies = result.groupby('word')['word'].count()
frequencies = frequencies.sort_values(ascending=False)
background_image = plt.imread('pl.jpg')

# 绘制词云
wordcloud = WordCloud(font_path='hwkt.ttf', max_words=100, background_color='white', mask=background_image)
my_wordcloud = wordcloud.fit_words(frequencies)
plt.imshow(my_wordcloud)
plt.axis('off')
plt.show()

# 将结果保存为csv
result.to_csv("word.csv", index=False, encoding='utf-8')