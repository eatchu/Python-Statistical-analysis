# -*- coding: utf-8 -*-
"""
kMeans 알고리즘
 - 비계층적(확인적) 군집분석
 - 군집수(k) 알고 있는 경우 이용
"""

import pandas as pd # dataframe 생성
import numpy as np # array object 생성
from sklearn.cluster import KMeans # model
import matplotlib.pyplot as plt # 시각화


# 1. dataset
# text file -> numpy 
def dataMat(file):
    dataset = [] # data mat 저장
    
    f = open(file,mode='r') # file object
    lines = f.readlines()
    for line in lines: # x y
        cols = line.split('\t') # x y split
        
        rows=[]
        for col in cols: # x -> y
            rows.append(float(col)) # [x, y]
        
        dataset.append(rows) # [[rows],[rows],...]
    return np.array(dataset) # 2차원

dataset = dataMat('data/testSet.txt')
dataset.shape # (80,2)
dataset[:5]
'''
array([[ 1.658985,  4.285136],
       [-3.453687,  3.424321],
       [ 4.838138, -1.151539],
       [-5.379713, -3.362104],
       [ 0.972564,  2.924086]])
'''

# numpy -> pandas
dataset_df = pd.DataFrame(dataset,columns=['x','y'])
dataset_df.info() # (80,2)
dataset_df[:5]
'''
          x         y
0  1.658985  4.285136
1 -3.453687  3.424321
2  4.838138 -1.151539
3 -5.379713 -3.362104
4  0.972564  2.924086
'''



# 2. kMeans model : k=4
kmeans = KMeans(n_clusters=4, algorithm='auto')
model = kmeans.fit(dataset_df)
pred = model.predict(dataset_df)
pred # 0~3



# 각 cluster의 center
centers=model.cluster_centers_





# 3. 시각화
dataset_df['cluster'] = pred
dataset_df.head()

plt.scatter(x=dataset_df['x'],y=dataset_df['y'],
            c=dataset_df['cluster'],marker='o')


# 중심점
plt.scatter(x=centers[:,0], y=centers[:,1],
            c='red',marker='o')

plt.show()










