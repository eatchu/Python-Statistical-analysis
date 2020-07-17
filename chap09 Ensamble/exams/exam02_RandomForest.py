'''
 문) 당료병(diabetes.csv) 데이터 셋을 이용하여 다음과 같은 단계로 
     RandomForest 모델을 생성하시오.

  <단계1> 데이터셋 로드
  <단계2> x,y 변수 생성 : y변수 : 9번째 칼럼, x변수 : 1 ~ 8번째 칼럼
  <단계3> 500개의 트리를 random으로 생성하여 모델 생성 
  <단계4> 5겹 교차검정/평균 분류정확도 출력
  <단계5> 중요변수 시각화 
'''

from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import matplotlib.pyplot as plt # 중요변수 시각화 

# 단계1. 테이터셋 로드  
dia = pd.read_csv('data/diabetes.csv', header=None) # 제목 없음  
print(dia.info()) 
print(dia.head()) 

# 단계2. x,y 변수 생성 
x_data = dia.loc[:, 0:7] # 숫자 -> label 해석 
y_data = dia.loc[:, 8]
x_data.shape # (759, 8)
y_data.shape # (759,)

# 단계3. model 생성
rf = RandomForestClassifier(n_estimators=500)
model = rf.fit(x_data, y_data)

# 단계4. 교차검정 model 예측/평가 
score = model_selection.cross_validate(model, x_data, y_data, cv=5)
score

print('평균 점수 =', score['test_score'].mean())

# 단계5. 중요변수 시각화 
x_size = x_data.shape[1]
plt.barh(range(x_size), model.feature_importances_)# (y, x)
plt.xlabel('importance')
plt.show()


