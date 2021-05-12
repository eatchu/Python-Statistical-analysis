'''
문2) dataset.csv 파일을 이용하여 교차테이블과 누적막대차트를 그리시오.
  <조건1> 성별(gender)과 만족도(survey) 칼럼으로 교차테이블  작성 
  <조건2> 교차테이블 결과를 대상으로 만족도 1,3,5만 선택하여 데이터프레임 생성   
  <조건3> 생성된 데이터프레임 대상 칼럼명 수정 : ['seoul','incheon','busan']
  <조건4> 생성된 데이터프레임 대상  index 수정 : ['male', 'female']     
  <조건5> 생성된 데이터프레임 대상 누적가로막대차트 그리기
'''

import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv('C:/IITT/4_Python-II/data/dataset.csv')
dataset.info() # 217x7

# 조건1
tab = pd.crosstab(dataset['gender'],dataset['survey'])
print(tab)
'''
survey   1   2   3   4  5
gender                   
1       10  51  44  13  5
2        4  36  42  11  1
'''

# 조건2
tab2 = tab.loc[:,[1,3,5]]
print(tab2)

# 조건3
tab2.columns = ['seoul','incheon','busan']

# 조건4아이티윌
tab2.index = ['male', 'female']    
print(tab2)

# 조건5
tab2.plot(kind='barh',stacked=True)





