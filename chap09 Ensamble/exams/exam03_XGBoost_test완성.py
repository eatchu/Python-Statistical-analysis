'''
 문) iris dataset을 이용하여 다음과 같은 단계로 XGBoost model을 생성하시오.
'''

import pandas as pd # file read
from xgboost import XGBClassifier # model 생성 
from xgboost import plot_importance # 중요변수 시각화  
import matplotlib.pyplot as plt # 중요변수 시각화 
from sklearn.model_selection import train_test_split # dataset split
from sklearn.metrics import confusion_matrix, accuracy_score,classification_report # model 평가 


# 단계1 : data set load 
iris = pd.read_csv("C:/ITWILL/4_Python-II/data/iris.csv")

# 변수명 추출 
cols=list(iris.columns)
col_x=cols[:4] # x변수명 
col_y=cols[-1] # y변수명 

# 단계2 : 훈련/검정 데이터셋 생성
train_set, test_set = train_test_split(iris, test_size=0.25)


# 단계3 : model 생성 : train data 이용
xgb = XGBClassifier(random_state=1)
model = xgb.fit(train_set[col_x], train_set[col_y])
model # objective='multi:softprob' -> 다항분류 

# 단계4 :예측치 생성 : test data 이용  
y_pred = model.predict(test_set[col_x])
y_pred2 = model.predict_proba(test_set[col_x])
y_pred2.shape # (38, 3) - [0.9 0.05 0.05] = 1
y_pred2.sum(axis = 1)

# 확률값 : [0.9 0.05 0.05] -> 10진수 : 0 
y_pred2_dit = y_pred2.argmax(axis = 1)
y_pred2_dit.shape # (38,)

y_true = test_set[col_y]

# 단계5 : 중요변수 확인 & 시각화  
fscore = model.get_booster().get_fscore()
fscore 
'''
{'Petal.Length': 118,
 'Sepal.Width': 106,
 'Sepal.Length': 44,
 'Petal.Width': 64}
'''
plot_importance(model)
plt.show()