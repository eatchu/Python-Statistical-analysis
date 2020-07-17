# -*- coding: utf-8 -*-
"""
계층적 군집분석
 - 상향식(Bottom-up)으로 계층적 군집 형성
 - 유클리드안 거리계산식 이용
 - 숫자형 변수만 사용 가능
"""


import pandas as pd # DataFrame
from sklearn.datasets import load_iris # dataset
from scipy.cluster.hierarchy import linkage, dendrogram # 군집분석 관련 tool
import matplotlib.pyplot as plt # 시각화



# 1. dataset load
iris = load_iris()
iris.feature_names # 4개 변수명

x = iris.data
y = iris.target

iris_df = pd.DataFrame(x,columns=iris.feature_names)
sp = pd.Series(y)
# y 변수 추가
iris_df['species'] = sp
iris_df.info()


# 2. 계층적 군집분석
clusters = linkage(iris_df, method='complete', metric='euclidean')
'''
method = 'single' : 단순연결
method = 'complete' : 완전연결
method = 'average' : 평균연결
'''

clusters.shape # (149,4)


# 3. 덴드로그램 시각화
plt.figure(figsize=(20,5))
dendrogram(clusters, leaf_rotation=90, leaf_font_size=20,)
plt.show()



# 4. 클러스터 자르기/평가 : 덴드로그램으로 판단
from scipy.cluster.hierarchy import fcluster # cluster 자르기

# 1) 클러스터 자르기
cluster = fcluster(clusters, t=3, criterion='distance')
cluster # 각 y의 범주가 속하는 군집의 배열

# 2) DF 칼럼 추가
iris_df['cluster'] = cluster
iris_df.info()

# 3) 산점도 시각화
plt.scatter(x=iris_df['sepal length (cm)'],y=iris_df['petal length (cm)'],
            c = iris_df['cluster'], marker = 'o')
plt.show()

# 4) 관측치 vs 예측치
pd.crosstab(index=iris_df['species'], columns=iris_df['cluster'])
'''
cluster   1   2   3
species            
0        50   0   0
1         0   0  50
2         0  34  16
'''


# 5) 군집별 특성분석
# DF.groupby('집단변수')
cluster_grp = iris_df.groupby('cluster')
cluster_grp.size()
'''
cluster
1    50
2    34
3    66
'''
cluster_grp.mean()









