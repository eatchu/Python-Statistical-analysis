# -*- coding: utf-8 -*-
"""
문) wine dataset을 이용하여 다음과 같이 다항분류 모델을 생성하시오. 
 <조건1> tree model 200개 학습
 <조건2> tree model 학습과정에서 조기 종료 100회 지정
 <조건3> model의 분류정확도와 리포트 출력   
"""
from xgboost import XGBClassifier # model
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine # 다항분류
from sklearn.metrics import accuracy_score, classification_report


#################################
## 1. XGBoost Hyper Parameter
#################################

# 1. dataset load
wine = load_wine()
print(wine.feature_names) # 13개 
print(wine.target_names) # ['class_0' 'class_1' 'class_2']

X, y = load_wine(return_X_y=True)

# 2. train/test 생성  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
type(X_train) # numpy.ndarray


# 3. model 객체 생성
obj = XGBClassifier()
print(obj) # parameter 확인 
obj = XGBClassifier(colsample_bytree=1,
                    learning_rate=0.1, max_depth=3, 
                    min_child_weight=1,
                    n_estimators=200, 
                    objective="multi:softprob",
                    num_class=3)


# 4. model 학습 조기종료 
evals = [(X_test, y_test)]
model = obj.fit(X_train, y_train, eval_metric='merror',
                early_stopping_rounds=100, eval_set=evals, verbose=True)

model # objective='multi:softprob'

# 5. model 평가 
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print('accuracy =', acc) # accuracy = 0.944444444444444444

report = classification_report(y_test, y_pred)
print(report)


