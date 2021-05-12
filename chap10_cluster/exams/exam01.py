'''
 문) 중학교 1학년 신체검사(bodycheck.csv) 데이터 셋을 이용하여 다음과 같이 군집모델을 생성하시오.
  <조건1> 악력, 신장, 체중, 안경유무 칼럼 대상 [번호 칼럼 제외]
  <조건2> 계층적 군집분석의 완전연결방식 적용 
  <조건3> 덴드로그램 시각화 
  <조건4> 텐드로그램을 보고 3개 군집으로 서브셋 생성  
'''

import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram # 계층적 군집 model
import matplotlib.pyplot as plt

# data loading - 중학교 1학년 신체검사 결과 데이터 셋 
body = pd.read_csv("data/bodycheck.csv", encoding='ms949')
print(body.info())

# <조건1> subset 생성 - 악력, 신장, 체중, 안경유무 칼럼  이용 
body_df = body.iloc[:,1:]
body_df.info()

# <조건2> 계층적 군집 분석  완전연결방식  
clusters = linkage(body_df, method='complete', metric='euclidean')

# <조건3> 덴드로그램 시각화 : 군집수는 사용 결정 
plt.figure(figsize=(20,5))
dendrogram(clusters, leaf_rotation=90, leaf_font_size=20,)
plt.show()

# <조건4> 텐드로그램을 보고 3개 군집으로 서브셋 생성
from scipy.cluster.hierarchy import fcluster # cluster 자르기

cluster = fcluster(clusters, t=3, criterion='distance')
cluster 

body_df['cluster'] = cluster
'''
cluster1 - 9 3 7 0 14
cluster2 - 10 2 4 5 13
cluster3 - 1 8 12 6 11
'''


plt.scatter(x=body_df['악력'],y=body_df['신장'],
            c = body_df['cluster'], marker = 'o')
plt.show()









