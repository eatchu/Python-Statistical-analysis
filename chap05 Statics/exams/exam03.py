'''
문1) score_iq.csv 데이터셋을 이용하여 단순선형회귀모델을 생성하시오.
   <조건1> y변수 : score, x변수 : academy      
   <조건2> 회귀모델 생성과 결과확인(회귀계수, 설명력, pvalue, 표준오차) 
   <조건3> 회귀선 적용 시각화 
   
문2) irsi.csv 데이터셋을 이용하여 다중선형회귀모델을 생성하시오.
   <조건1> 칼럼명에 포함된 '.' 을 '_'로 수정
   iris = pd.read_csv('../data/iris.csv')
   iris.columns = iris.columns.str.replace('.', '_')
   <조건2> y변수 : 1번째 칼럼, x변수 : 2~4번째 칼럼    
   <조건3> 회귀계수 확인 
   <조건4> 회귀모델 세부 결과 확인  : summary()함수 이용 
'''

from scipy import stats
import pandas as pd
import statsmodels.formula.api as sm


##### 문제 1 #####
score = pd.read_csv('data/score_iq.csv')
score.info()

# 조건 1
score.corr()
x = score.academy
y = score.score
# 조건 2
model = stats.linregress(x,y)
model
'''
slope=4.847829398324446 기울기
intercept=68.23926884996192 절편
rvalue=0.8962646792534938 설명력
pvalue=4.036716755167992e-54 유의성검정
stderr=0.1971936807753301 표준오차
'''
y_pred = x*model.slope + model.intercept
err = (y - y_pred)**2
err
# 조건 3
from pylab import plot, legend, show
plot(x,y,'b.') # (x적절성,y만족성) : 산점도
plot(x,y_pred,'r.-') # 회귀선
legend(['x,y scatter','regress model line'])
show()




##### 문제 2 #####
iris = pd.read_csv('data/iris.csv')
# 조건 1
iris.columns = iris.columns.str.replace('.','_')
iris.info()
# 조건 2
iris.corr()
formula = "Sepal_Length ~ Sepal_Width + Petal_Length + Petal_Width"

model = sm.ols(formula, data=iris).fit()
model # object info
model.summary() # 분석결과
'''
Adj. R-squared:                  0.856
F-statistic:                     295.5 (-1.96 ~ +1.96)
Prob (F-statistic):           8.59e-62
'''


# 기울기, 절편
model.params
'''
Intercept       1.855997
Sepal_Width     0.650837
Petal_Length    0.709132 -> t의 검정통계량을 확인했을때 영향력이 가장 높음
Petal_Width    -0.556483
'''


# Y 예측치
y_pred = model.fittedvalues # y_pred 예측치를 별도로 가지고 있음
y_true = iris['Sepal_Length']

err = (y_true - y_pred)**2
err # 각각의 예측치와 관측치에 대한 오차율을 볼 수 있음

y_true.mean() # 5.843333333333335
y_pred.mean() # 5.843333333333335

# 차트 확인 
import matplotlib.pyplot as plt

plt.plot(y_true, 'b', label='real values')
plt.plot(y_pred, 'r', label='y prediction')
plt.legend(loc='best')
plt.show()










