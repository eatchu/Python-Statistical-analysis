'''
 문) load_breast_cancer 데이터 셋을 이용하여 다음과 같이 Decision Tree 모델을 생성하시오.
 <조건1> 75:25비율 train/test 데이터 셋 구성 
 <조건2> y변수 : cancer.target, x변수 : cancer.data 
 <조건3> 중요변수 확인 

'''
import pandas as pd
from sklearn import model_selection
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.tree.export import export_text

# 데이터 셋 load 
cancer = load_breast_cancer()
print(cancer)
print(cancer.DESCR)
cancer.target_names # ['malignant', 'benign']
name = cancer.feature_names

# 변수 선택 
X = cancer.data
y = cancer.target

X.shape # (569, 30)
y.shape # (569,)

# split
x_train, x_test, y_train, y_test = model_selection.train_test_split(X,y)
x_train.shape # (426, 30)
x_test.shape # (426, 30)

# model 
dtc = DecisionTreeClassifier(criterion='entropy', max_depth=2)
model = dtc.fit(x_train,y_train)
tree.plot_tree(model)
print(export_text(model,list(name))) 
'''
|--- worst perimeter <= 115.35
|   |--- worst concave points <= 0.15
|   |   |--- class: 1
|   |--- worst concave points >  0.15
|   |   |--- class: 0
|--- worst perimeter >  115.35
|   |--- mean concavity <= 0.06
|   |   |--- class: 0
|   |--- mean concavity >  0.06
|   |   |--- class: 0
'''

# 중요변수
# 'worst perimeter' 'worst concave points' 'worst concavity'

