'''   
문5) iris.csv 파일을 읽어와서 다음과 같이 처리하시오.
   조건1> 1~4 칼럼 대상 vector 생성(col1, col2, col3, col4)    
   조건2> 1,4 칼럼 대상 합계, 평균, 표준편차 구하기 
   조건3> 1,2 칼럼과 3,4 칼럼을 대상으로 각 df1, df2 데이터프레임 생성
   조건4> df1과 df2 칼럼 단위 결합 iris_df 데이터프레임 생성      
'''

import pandas as pd

iris = pd.read_csv('C:\\IITT\\4_Python-II\\data\\iris.csv'')
print(iris.info())


# 조건1> 1~4 칼럼 대상 vector 생성(col1, col2, col3, col4)    
col1 = iris.iloc[:,0]
col2 = iris.iloc[:,1]
col3 = iris.iloc[:,2]
col4 = iris.iloc[:,3]


# 조건2> 1,4 칼럼 대상 합계, 평균, 표준편차 구하기 
print(col1.describe()[[1,2]],'\n sum \t',col1.sum())
print(col2.describe()[[1,2]],'\n sum \t',col2.sum())
print(col3.describe()[[1,2]],'\n sum \t',col3.sum())
print(col4.describe()[[1,2]],'\n sum \t',col4.sum())


# 조건3> 1,2 칼럼과 3,4 칼럼을 대상으로 각 df1, df2 데이터프레임 생성
df1 = pd.concat([col1,col2],axis=1)
print(df1)
df2 = pd.concat([col3,col4],axis=1)
print(df2)

# 조건4> df1과 df2 칼럼 단위 결합 iris_df 데이터프레임 생성
iris_df = pd.concat([df1,df2],axis=1)
print(iris_df)

