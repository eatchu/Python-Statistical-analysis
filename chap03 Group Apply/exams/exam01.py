'''
문1) movie_rating.csv 파일을 대상으로 다음과 같이 단계별로 그룹화 하시오.
   <단계1> 평가자(critic), 영화제목(title) -> 평점(rating) 그룹화    
   <단계2> table 생성 -> 행 : critic, 열 : title, 셀 : 평점(rating) 합계          
   
 <<출력 결과>>
         rating                                      
title   Just My Lady Snakes Superman The Night You Me
critic                                               
Claudia     3.0  NaN    3.5      4.0       4.5    2.5
Gene        1.5  3.0    3.5      5.0       3.0    3.5
Jack        NaN  3.0    4.0      5.0       3.0    3.5
Lisa        3.0  2.5    3.5      3.5       3.0    2.5
Mick        2.0  3.0    4.0      3.0       3.0    2.0
Toby        NaN  NaN    4.5      4.0       NaN    1.0    
'''
import pandas as pd
import os
print(os.getcwd())

rating = pd.read_csv('data/movie_rating.csv')
print(rating.info()) # 31 x 3
print(rating.head())

critic_title = rating.groupby(['critic','title'])
critic_title.sum().unstack()
