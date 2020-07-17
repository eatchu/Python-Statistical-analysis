'''
 문) digits 데이터 셋을 이용하여 다음과 단계로 Pipeline 모델을 생성하시오.
  <단계1> dataset load
  <단계2> Pipeline model 생성
          - scaling : StndardScaler 클래스, modeing : SVC 클래스    
  <단계3> GridSearch model 생성
          - params : 10e-2 ~ 10e+2, 평가방법 : accuracy, 교차검정 : 5겹
          - CPU 코어 수 : 2개 
  <단계4> best score, best params 출력 
'''

from sklearn.datasets import load_digits # dataset 
from sklearn.svm import SVC # model
from sklearn.model_selection import GridSearchCV # gride search model
from sklearn.pipeline import Pipeline # pipeline
from sklearn.preprocessing import StandardScaler # dataset scaling(z공식)



# 1. dataset load
digits = load_digits()
X = digits.data
y = digits.target
X.min()
X.max()

# 2. pipeline model : data 표준화 -> model 
pipe_svc = Pipeline([('scaler',StandardScaler()),('svc',SVC(random_state=1))])


# 3. gride search model 
params = [0.01,0.1,1.0,10.0,100.0]
params_grid = [{'svc__C':params, 'svc__kernel':['linear']}, # 선형
               {'svc__C':params, 'svc__gamma':params, 'svc__kernel':['rbf']}] # 비선형
gs = GridSearchCV(estimator = pipe_svc,param_grid = params_grid, scoring = 'accuracy',cv=5, n_jobs=2) # n_jobs=CPU

model = gs.fit(X,y)

# 교차검정 결과 
model.cv_results_["mean_test_score"]

# 4. best score, best params
# best score
model.best_score_ # 0.956032188177035

# best parameter
model.best_params_
# {'svc__C': 10.0, 'svc__gamma': 0.01, 'svc__kernel': 'rbf'}

