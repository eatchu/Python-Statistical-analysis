'''
문02) winequality-both.csv 데이터셋을 이용하여 다음과 같이 처리하시오.
   <조건1> quality, type 칼럼으로 교차분할표 작성 
   <조건2> 교차분할표를 대상으로 white 와인 내림차순 정렬       
   <조건3> red 와인과 white 와인의 quality에 대한 두 집단 평균 검정
           -> 각 집단 평균 통계량 출력
   <조건4> alcohol 칼럼과 다른 칼럼 간의 상관계수 출력  
'''

import pandas as pd
from scipy import stats

wine = pd.read_csv('data/winequality-both.csv')
wine.info() # 6497 x 13

cross = pd.crosstab(wine['quality'],wine['type'])
'''
type     red  white
quality            
3         10     20
4         53    163
5        681   1457
6        638   2198
7        199    880
8         18    175
9          0      5
'''

cross2 = cross.sort_values(by=['white'],ascending=False)
'''
type     red  white
quality            
6        638   2198
5        681   1457
7        199    880
8         18    175
4         53    163
3         10     20
9          0      5
'''

red_wine = wine.loc[wine['type'] == 'red', 'quality']           
white_wine = wine.loc[wine['type'] == 'white', 'quality']      

t = stats.ttest_ind(red_wine,white_wine)
print('statistic=%.5f, pvalue=%.5f'%(t))
# statistic=-9.68565, pvalue=0.00000
# [해석] 와인의 종류에 따른 와인의 품질은 차이가 있다.



wine.corr()['alcohol']
'''
fixed acidity          -0.095452
volatile acidity       -0.037640
citric acid            -0.010493
residual sugar         -0.359415
chlorides              -0.256916
free sulfur dioxide    -0.179838
total sulfur dioxide   -0.265740
density                -0.686745
pH                      0.121248
sulphates              -0.003029
alcohol                 1.000000
quality                 0.444319
Name: alcohol, dtype: float64
'''

red_wine = wine.loc[wine['type'] == 'red', 'quality']           
white_wine = wine.loc[wine['type'] == 'white', 'quality']           




