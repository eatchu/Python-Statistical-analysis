'''
외식업종 관련 data set 분석
 - 2년 이내 폐업에 영향을 미치는 변수를 분석하기 위한 data set

문) food_df를 대상으로 다음과 같이 xgboost 모델을 생성하시오.
   <조건1> 6:4 비율 train/test set 생성 
   <조건2> y변수 ; 폐업_2년, x변수 ; 나머지 20개 
   <조건3> 중요변수에 대한  f1 score 출력
   <조건4> 중요변수 시각화  
   <조건5> accuracy와 model report 출력 
'''
import pandas as pd
from sklearn import model_selection, metrics # model 평가 
from sklearn.preprocessing import minmax_scale # 정규화[0-1] 함수 
from xgboost import XGBClassifier # xgboost 모델 생성 
from xgboost import plot_importance # 중요변수 시각화 

# 중요변수 시각화 
from matplotlib import pyplot
from matplotlib import font_manager, rc # 한글 지원
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# 외식업종 관련 data set
food = pd.read_csv("C:/ITWILL/4_Python-II/data/food_dataset.csv", encoding="utf-8", thousands=',')

# 결측치 제거
food=food.dropna()  
print(food.info())
'''
Int64Index: 68796 entries, 0 to 70170
Data columns (total 21 columns):
'''
 
print('정규화 전')
print(food.head(5)) # 0    43.00
 
# 변수 정규화/DataFrame 형변환  
food_nor = minmax_scale(food) # 정규화 
print(type(food_nor)) # <class 'numpy.ndarray'>
 
 
# 칼럼명 적용 DataFrame 생성 
# x, y 변수 선택 
oriCol=list(food.columns)
print('food 칼럼수 : ', len(oriCol)) # food 칼럼수 :  21
print('전체 칼럼명 : ', oriCol) # ['소재지면적','위생업태명','주변','주변동종','기간평균',...,'폐업_2년']
 
food_df = pd.DataFrame(food_nor, columns=oriCol) # numpy -> pandas
print(food_df.info())
print('정규화 후')
print(food_df.head(5)) # 0 ~ 20 칼럼명으로 수정됨  
# print(food_df['소재지면적'][:5]) # 0    0.007144
 
 
# 6:4 비율 data set 생성  
train_set, test_set = model_selection.train_test_split(
    food_df, test_size=0.4)
print("train_set 사이즈:",train_set.shape)
print("test_set 사이즈:",test_set.shape)
'''
train_set 사이즈: (41277, 21)
test_set 사이즈: (27519, 21)
'''
 
 
# x, y변수 선택 
y_name=oriCol.pop(-1) # 마지막 칼럼 추출(제거)
print('y 변수 : ', y_name) # y 변수 :  폐업_2년(2년 기준 폐업 유무)
x_name=oriCol # 20개 변수 
print("기존 x변수 개수:",len(x_name)) # 기존 x변수 개수: 20
 
# model 생성
food_XGB = XGBClassifier()
food_XGB.fit(train_set[x_name],train_set[y_name])
pred = food_XGB.predict(test_set[x_name]) # 예측치 생성 
 
# f1 score 보기 
fscore = food_XGB.get_booster().get_fscore()
print("fscore:",fscore) # fscore: {'소재지면적': 108, '주변': 91, ...,'위생업태명': 11}
print('len=', len(fscore)) # len= 19
print('refined_XGB=',food_XGB) # model 정보 
  
# 중요변수 시각화
plot_importance(food_XGB) 
# 중요변수 4 : 소재지면적, 주변외식업수, 주변외식업평균기간, 금리(bank), 유동인구(pop)
pyplot.show()
 
# confusion matrix/accuracy 
con_mat=pd.crosstab(pred,test_set[y_name],rownames=["예측치"],colnames=["관측치"])
print(con_mat)

test_set[y_name].value_counts()
'''
0.0    21731
1.0     5788
'''
acc = metrics.accuracy_score(test_set[y_name], pred)
print('분류정확도 =', acc)
# 분류정확도 = 0.8378825226958456

report = metrics.classification_report(test_set[y_name], pred)
print('모델 report')
print(report)



