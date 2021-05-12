'''
문1) iris.csv 파일을 이용하여 다음과 같이 차트를 그리시오.
    <조건1> iris.csv 파일을 iris 변수명으로 가져온 후 파일 정보 보기
    <조건2> 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그리기
    <조건3> 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그린 후  5번 칼럼으로 색상 적용 
'''

import pandas as pd
import matplotlib.pyplot as plt

# 조건 1
iris = pd.read_csv('C:/IITT/4_Python-II/data/iris.csv')
print(iris.info())

# 조건 2
plt.scatter(iris.iloc[:,0],iris.iloc[:,2])

# 조건 3
cdata = []
for i in iris.iloc[:,4]:
    if i == 'setosa':
        cdata.append(1)
    elif i == 'versicolor':
        cdata.append(2)
    else:
        cdata.append(3)
plt.scatter(iris.iloc[:,0],iris.iloc[:,2], c=cdata)

