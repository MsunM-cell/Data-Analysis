import pandas as pd
import numpy as np
import re
import jieba.posseg as psg
import matplotlib.pyplot as plt
from wordcloud import WordCloud

import warnings

import wordcloud
warnings.filterwarnings('ignore')

word = pd.read_csv('word.csv')

# 读入正面、负面情感评价词
pos_comment = pd.read_csv('正面评价词语（中文）.txt', header=None, sep='\n', encoding='utf-8', engine='python')
neg_comment = pd.read_csv('负面评价词语（中文）.txt', header=None, sep='\n', encoding='utf-8', engine='python')
pos_emotion = pd.read_csv('正面情感词语（中文）.txt', header=None, sep='\n', encoding='utf-8', engine='python')
neg_emotion = pd.read_csv('负面情感词语（中文）.txt', header=None, sep='\n', encoding='utf-8', engine='python')

# 合并情感词与评价词
positive = set(pos_comment.iloc[:, 0]) | set(pos_emotion.iloc[:, 0])
negative = set(neg_comment.iloc[:, 0]) | set(neg_emotion.iloc[:, 0])

intersection = positive & negative
positive = list(positive - intersection)
negative = list(negative - intersection)

positive = pd.DataFrame({'word': positive, 'weight': [1] * len(positive)})
negative = pd.DataFrame({'word': negative, 'weight': [-1] * len(negative)})

posneg = positive.append(negative)

# 将分词结果和正负面情感词表合并，定位情感词
data_posneg = posneg.merge(word, left_on='word', right_on='word', how='right')
data_posneg = data_posneg.sort_values(by=['index_content', 'index_word'])

# 载入否定词表
notdict = pd.read_csv('not.csv')

# 构造新列，作为否定词修正后的情感值
data_posneg['amend_weight'] = data_posneg['weight']
data_posneg['id'] = np.arange(0, len(data_posneg))

# 只保留有情感值的词语
only_inclination = data_posneg.dropna().reset_index(drop=True)
index = only_inclination['id']

for i in np.arange(0, len(only_inclination)):
    # 提取第i个情感词所在的评论
    review = data_posneg[data_posneg['index_content'] == only_inclination['index_content'][i]]
    review.index = np.arange(0, len(review))
    # 第i个情感值在该文档中的位置
    affective = only_inclination['index_word'][i]
    if affective == 1:
        ne = sum([i in notdict['term'] for i in review['word'][affective - 1]]) % 2
        if ne == 1:
            data_posneg['amend_weight'][index[i]] = -data_posneg['weight'][index[i]]
    elif affective > 1:
        ne = sum([i in notdict['term'] for i in review['word'][[affective - 1, affective - 2]]]) % 2
        if ne == 1:
            data_posneg['amend_weight'][index[i]] = -data_posneg['weight'][index[i]]

only_inclination = only_inclination.dropna()

# 计算每条评论的情感值
emotion_value = only_inclination.groupby(['index_content'], as_index=False)['amend_weight'].sum()
# 去除情感值为0的评论
emotion_value = emotion_value[emotion_value['amend_weight'] != 0]

# 给情感值大于0的赋予评论类型（content_type）为pos，小于0的为neg
emotion_value['a_type'] = ''
emotion_value['a_type'][emotion_value['amend_weight'] > 0] = 'pos'
emotion_value['a_type'][emotion_value['amend_weight'] < 0] = 'neg'

# 查看情感分析结果
result = emotion_value.merge(word, left_on='index_content', right_on='index_content', how='left')
result = result[['index_content', 'content_type', 'a_type']].drop_duplicates()

# 绘制情感倾向分析混淆矩阵，交叉表：统计分组频率的特殊透视表
confusion_matrix = pd.crosstab(result['content_type'], result['a_type'], margins=True)
precison = (confusion_matrix.iat[0, 0] + confusion_matrix.iat[1, 1]) / confusion_matrix.iat[2, 2]
# print(precison)

# 提取正负面评论信息
ind_pos = list(emotion_value[emotion_value['a_type'] == 'pos']['index_content'])
ind_neg = list(emotion_value[emotion_value['a_type'] == 'neg']['index_content'])

posdata = word[[i in ind_pos for i in word['index_content']]]
negdata = word[[i in ind_neg for i in word['index_content']]]

# 绘制词云
freq_pos = posdata.groupby('word')['word'].count()
freq_pos = freq_pos.sort_values(ascending=False)
background_image = plt.imread('pl.jpg')
wordcloud = WordCloud(font_path='hwkt.ttf', max_words=100, background_color='white', mask=background_image)
pos_wordcloud = wordcloud.fit_words(freq_pos)
plt.imshow(pos_wordcloud)
plt.axis('off')
plt.show()

freq_neg = negdata.groupby(by=['word'])['word'].count()
freq_neg = freq_neg.sort_values(ascending = False)
neg_wordcloud = wordcloud.fit_words(freq_neg)
plt.imshow(neg_wordcloud)
plt.axis('off') 
plt.show()

# 将结果写出，每条评论作为一行
posdata.to_csv("./posdata.csv", index = False, encoding = 'utf-8')
negdata.to_csv("./negdata.csv", index = False, encoding = 'utf-8')

