'''  
문4) tips.csv 파일을 읽어와서 다음과 같이 처리하시오.
   조건1> 파일 정보 보기 
   조건2> header를 포함한 앞부분 5개 관측치 보기 
   조건3> header를 포함한 뒷부분 5개 관측치 보기 
   조건4> 숫자 칼럼 대상 요약통계량 보기 
   조건5> 흡연자(smoker) 유무 빈도수 계산  
   조건6> 요일(day) 칼럼의 유일한 값 출력 
'''

import pandas as pd

tips = pd.read_csv('C:\\IITT\\4_Python-II\\data\\tips.csv', encoding='utf-8')

# 조건1 파일 정보 보기 
tips.info() # 244 x 7


# 조건2 header를 포함한 앞부분 5개 관측치 보기 
tips.head()
'''
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
'''


# 조건3 header를 포함한 뒷부분 5개 관측치 보기 
tips.tail()
'''
     total_bill   tip     sex smoker   day    time  size
239       29.03  5.92    Male     No   Sat  Dinner     3
240       27.18  2.00  Female    Yes   Sat  Dinner     2
241       22.67  2.00    Male    Yes   Sat  Dinner     2
242       17.82  1.75    Male     No   Sat  Dinner     2
243       18.78  3.00  Female     No  Thur  Dinner     2
'''


# 조건4 숫자 칼럼 대상 요약통계량 보기 
# 숫자칼럼 subset 만들기
tips_int = tips.iloc[[0,1,6],:]
print(tips_int)
# 요약 통계량
print(tips_int.describe())


# 조건5 흡연자(smoker) 유무 빈도수 계산 
print(tips['smoker'].value_counts()) # No:151 Yes:93

# 조건6 요일(day) 칼럼의 유일한 값 출력 
print(tips['day'].unique()) # ['Sun' 'Sat' 'Thur' 'Fri']






