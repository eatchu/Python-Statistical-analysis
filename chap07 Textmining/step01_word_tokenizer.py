# -*- coding: utf-8 -*-
"""
TfidfVectorizer class 특징 
 1. 단어벡터 생성기 : 문장 -> 단어 벡터 
 2. 단어 사전 : (word : 고유번호)
 3. 희소행렬 
"""

from sklearn.feature_extraction.text import TfidfVectorizer


sentences = [
    "Mr. Green killed Colonel Mustard in the study with the candlestick. Mr. Green is not a very nice fellow.",
    "Professor Plum has a green plant in his study.",
    "Miss Scarlett watered Professor Plum's green plant while he was away from his office last week."
]

# 1. 단어벡터 생성기 
tfidf = TfidfVectorizer() # object
# object.member() or member

tfidf_fit = tfidf.fit(sentences) # 문장 -> 단어 
print(tfidf_fit)

# 2. 단어 사전 
voc = tfidf_fit.vocabulary_
print('단어사전')
print(voc) # {'word' : 고유번호}
# {'mr': 14, 'green': 5, 'killed': 11, 'colonel': 2,  '''} 
print(len(voc)) # 31
'''
고유번호 
 1. 단어 영문자 오름차순으로 생성 
 2. 희소행렬 : 열의 차순 
'''

# 3. 희소행렬 : row(doc num) x col(고유번호) -> cell(tfidf 가중치)
tfidf_sparse = tfidf.fit_transform(sentences)
print(tfidf_sparse)
'''
  (row,column)    weight(tfidf)
  (0, 14)       0.4411657657527482  -> mr(2)
  (0, 5)        0.26055960805891015 -> green(4)
  (0, 11)       0.2205828828763741
  (1, 5)        0.2690399207469689
  (1, 9)        0.34643788271971976
  (1, 23)       0.34643788271971976
  (2, 12)       0.27054287522550385
  (2, 28)       0.27054287522550385  
'''
print(type(tfidf_sparse))
# <class 'scipy.sparse.csr.csr_matrix'>

# scipy 행렬 -> numpy 행렬 
tfidf_arr = tfidf_sparse.toarray()
print(type(tfidf_arr)) # <class 'numpy.ndarray'>

print(tfidf_arr)
'''
[[0.         0.22058288 0.22058288 0.22058288 0.         0.26055961
  0.         0.         0.         0.16775897 0.22058288 0.22058288
  0.         0.         0.44116577 0.22058288 0.22058288 0.22058288
  0.         0.         0.         0.         0.         0.16775897
  0.44116577 0.22058288 0.         0.         0.         0.
  0.22058288]
 [0.         0.         0.         0.         0.         0.26903992
  0.45552418 0.         0.34643788 0.34643788 0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.34643788 0.34643788 0.34643788 0.         0.34643788
  0.         0.         0.         0.         0.         0.
  0.        ]
 [0.27054288 0.         0.         0.         0.27054288 0.15978698
  0.         0.27054288 0.20575483 0.         0.         0.
  0.27054288 0.27054288 0.         0.         0.         0.
  0.27054288 0.20575483 0.20575483 0.20575483 0.27054288 0.
  0.         0.         0.27054288 0.27054288 0.27054288 0.27054288
  0.        ]]
 '''
print(tfidf_arr.shape) # (3, 31)

'''
1. scipy 희소행렬 : tensorflow model data
2. numpy 희소행렬 : sklearn model data
'''





