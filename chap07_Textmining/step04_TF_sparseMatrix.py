# -*- coding: utf-8 -*-
"""
csv file -> sparse matrix
 1. csv file read
 2. texts, target 전처리 
 3. max_feature : 열의 차수 결정 - max_feature = 4000 제한
 4. sparse matrix
"""

from sklearn.feature_extraction.text import TfidfVectorizer
import string
import pandas as pd
from sklearn.model_selection import train_test_split

# 1. csv file read
spam_data = pd.read_csv("../data/sms_spam.csv", encoding='iso-8859-1')
print(spam_data.info())
print(spam_data)

# 2. texts, target 전처리 
target = spam_data['type']
texts = spam_data['text']

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


# 3. max_feature : 열의 차수 결정
tfidf_fit = TfidfVectorizer().fit(re_texts) # 문장 -> 단어벡터 생성기 

voc = tfidf_fit.vocabulary_ # 단어 사전 
print(len(voc)) # 8569
print(voc)

max_feature = 6000 # 6000 단어 

# 4. sparse matrix
tfidf = TfidfVectorizer(stop_words ='english', max_features = max_feature)

sparse_matrix = tfidf.fit_transform(re_texts)
print(sparse_matrix.shape) # (5558, 6000)
print(sparse_matrix)

# numpy sparse matrix 
sparse_matrix_arr = sparse_matrix.toarray()
print(type(sparse_matrix_arr)) # <class 'numpy.ndarray'>
print(sparse_matrix_arr[:5,4000:4100])

# 0 -> 0, 0.1~ -> 1
for i in range(5558) : # i = row
    for j in range(6000) : # j = column
        item = sparse_matrix_arr[i, j] 
        if item > 0 :
            sparse_matrix_arr[i, j] = 1

print(sparse_matrix_arr[0, 2000:2100])            
            

# csv file save
# numpy -> pandas 
import pandas as pd

sparse_df = pd.DataFrame(sparse_matrix_arr)
print(sparse_df.info())
'''
RangeIndex: 5558 entries, 0 to 5557
Columns: 6000 entries, 0 to 5999
'''

# y,x bind
target = pd.Series(target)
sms_spam_data = pd.concat([target, sparse_df], axis = 1)
            
sms_spam_data.to_csv("../data/sms_spam_data.csv", index = None,
                     encoding = 'utf-8')        

spam_data = pd.read_csv("../data/sms_spam_data.csv", encoding = 'utf-8')
print(spam_data.info())



