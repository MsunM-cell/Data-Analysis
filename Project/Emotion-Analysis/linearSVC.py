import pandas as pd

# 原始文本转化为tf-idf的特征矩阵
from sklearn.feature_extraction.text import TfidfVectorizer as TFIDF
from sklearn.svm import LinearSVC
from sklearn.calibration import CalibratedClassifierCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import warnings
warnings.filterwarnings('ignore')

reviews = pd.read_csv('reviews.csv')
reviews = reviews[['content', 'content_type']].drop_duplicates()

reviews['content_type'] = reviews['content_type'].map(lambda x: 1.0 if x == 'pos' else 0.0)

# 将有标签的数据集划分成训练集和测试集
train_X, valid_X, train_y, valid_y = train_test_split(reviews['content'], reviews['content_type'], test_size=0.2, random_state=42)

# 模型构建
model_tfidf = TFIDF(min_df=5, max_features=5000, ngram_range=(1, 3), use_idf=1, smooth_idf=1)
# 学习idf vector
model_tfidf.fit(train_X)
# 把文档转换成X矩阵（该文档中该特征词出现的频次），行是文档个数，列是特征词的个数
train_vec = model_tfidf.transform(train_X)
arr = train_vec.toarray()

# 模型训练
model_SVC = LinearSVC()
clf = CalibratedClassifierCV(model_SVC)
clf.fit(train_vec,train_y)

# 把文档转换成矩阵
valid_vec = model_tfidf.transform(valid_X)
# 验证
pre_valid = clf.predict_proba(valid_vec)

pre_valid = clf.predict(valid_vec)
print('正例: ', sum(pre_valid == 1))
print('负例: ', sum(pre_valid == 0))

score = accuracy_score(pre_valid, valid_y)
print("准确率: ", score)

