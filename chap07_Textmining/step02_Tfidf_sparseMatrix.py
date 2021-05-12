# -*- coding: utf-8 -*-
"""
csv file -> sparse matrix
 1. csv file read
 2. texts, target 전처리 
 3. max_feature : 열의 차수 결정 
 4. sparse matrix
"""

from sklearn.feature_extraction.text import TfidfVectorizer
import string
import pandas as pd

# 1. csv file read
spam_data = pd.read_csv("../data/temp_spam_data.csv", header = None,
            encoding='utf-8')
print(spam_data.info())
print(spam_data)

# 2. texts, target 전처리 
target = spam_data[0]
texts = spam_data[1]

print(target)
# target dummy(spam=1, ham=0)
target = [ 1 if t == 'spam' else 0 for t in target]
print(target) # [0, 1, 0, 1, 0]

# texts 전처리
def text_prepro(texts):
    # Lower case
    texts = [x.lower() for x in texts]
    # Remove punctuation
    texts = [''.join(c for c in x if c not in string.punctuation) for x in texts]
    # Remove numbers
    texts = [''.join(c for c in x if c not in string.digits) for x in texts]
    # Trim extra whitespace
    texts = [' '.join(x.split()) for x in texts]
    return texts

re_texts = text_prepro(texts)
print(re_texts)
'''
['우리나라 대한민국 우리나라 만세', '비아그라 gram 정력 최고', '나는 대한민국 사람', '보험료 원에 평생 보장 마감 임박', '나는 홍길동']
'''

# 3. max_feature : 열의 차수 결정
tfidf_fit = TfidfVectorizer().fit(re_texts) # 문장 -> 단어벡터 생성기 

voc = tfidf_fit.vocabulary_ # 단어 사전 
print(len(voc)) # 16
# {'우리나라': 9, '대한민국': 2, '만세': 4, '비아그라': 7, 'gram': 0, '정력': 12, '최고': 13, '나는': 1, '사람': 8, '보험료': 6, '원에': 10, '평생': 14, '보장': 5, '마감': 3, '임박': 11, '홍길동': 15}
print(voc)

max_feature = len(voc) # 16 단어 
#max_feature = 10
'''
전체 단어 16개 중에서 max_feature = 10 일 때
10 단어로 짤라서 열의 차수 결정 
'''

# 4. sparse matrix
#help(TfidfVectorizer)
# encoding='utf-8', stop_words=None, max_features=None

tfidf = TfidfVectorizer(max_features = max_feature) # object
tfidf_sparse = tfidf.fit_transform(re_texts) # 문서 -> 희소행렬 

print(tfidf_sparse.shape) # (5, 16) -> (doc, max_feature)
print(tfidf_sparse)
'''
  (0, 9)        0.8413381201263408 -> 우리나라
  (0, 2)        0.3393931489111758 -> 대한민국
  (0, 4)        0.4206690600631704
'''

# scipy 희소행렬 -> numpy 희소행렬 
tfidf_sparse_arr = tfidf_sparse.toarray()
print(tfidf_sparse_arr)
print(tfidf_sparse_arr.shape) # (5, 16)











