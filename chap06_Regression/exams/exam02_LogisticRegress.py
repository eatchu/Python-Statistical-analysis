'''
문) load_wine() 함수를 이용하여 와인 데이터를 다항분류하는 로지스틱 회귀모델을 생성하시오. 
  조건1> train/test - 7:3비울
  조건2> y 변수 : wine.data 
  조건3> x 변수 : wine.data
  조건4> 모델 평가 : confusion_matrix, 분류정확도[accuracy]
'''

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

# 1. wine 데이터셋 
wine = load_wine()

# 2. 변수 선택 
wine_x = wine.data # x변수 
wine_y = wine.target # y변수
wine_y # 0,1,2 다항분류

# 3. train/test split(7:3)
x_train,x_test,y_train,y_test = train_test_split(wine_x,wine_y,test_size=0.3,random_state=123)
x_train.shape # (124,13)
x_test.shape # (54,13)

# 4. model 생성  : solver='lbfgs', multi_class='multinomial'
lr = LogisticRegression(solver='lbfgs', multi_class='multinomial',random_state=123)
model = lr.fit(x_train,y_train)
model

# 5. 모델 평가 : accuracy, confusion matrix
y_pred = model.predict(x_test)
y_pred

acc = metrics.accuracy_score(y_test,y_pred)
acc # 0.9629629629629629

con_max = metrics.confusion_matrix(y_test,y_pred)
con_max 
type(con_max) # numpy.ndarray
'''
[[13,  1,  0]
 [ 0, 18,  0]
 [ 0,  1, 21]]
'''

acc = (con_max[0,0]+con_max[1,1]+con_max[2,2])/con_max.sum()
acc # 0.9629629629629629

# 6. 시각화
import seaborn as sn # heatmap - Accuracy Score
import matplotlib.pyplot as plt

# confusion matirx heatmap
plt.figure(figsize=(6,6)) # chart size
sn.heatmap(con_max, annot=True, fmt='.1f', linewidths=.5, square=True)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
all_sample_title = 'Accuracy Score: {0}'.format(acc)
plt.title(all_sample_title,size=10)
plt.show()



















