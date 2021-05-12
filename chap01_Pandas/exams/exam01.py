''' 
step02 관련문제 
문1) score.csv 파일을 읽어와서 다음과 같이 처리하시오.
   조건1> tv 칼럼이 0인 관측치 2개 삭제 (for, if문 이용)
   조건2> score, academy 칼럼만 추출하여 DataFrame 생성
   조건3> score, academy 칼럼의 평균 계산 
   - <<출력 결과 >> 참고    
   
<<출력 결과 >>
   score  academy
1     75        1
2     77        1
3     83        2
4     65        0
5     80        3
6     83        3
7     70        1
9     79        2
score      76.500
academy     1.625   
'''

import pandas as pd
score = pd.read_csv('C:\\IITT\\4_Python-II\\data\\score.csv', encoding='utf-8')
print(score)

# 특정 값이 들어있는 특정 행 제거
score2 = score.drop(score[score.tv == 0].index)
score2
# score[score.tv != 0]
for i, c in enumerate(score.tv):
    print(i,c)
    if c == 0 :
        score_df = score.drop(i)



# 특정 칼럼 추출
score3 = score2[['score','academy']]
score3

# 칼럼 평균 계산
print('score 평균=',round(score3.score.mean(),2))
print('academy 평균=',round(score3.academy.mean(),2))

# 열단위 평균
score3.mean(axis=0)


# 평균 행 추가
score3.loc['평균'] = score3.mean(axis=0)

# index 재정렬
len(score3)
score3.index = range(1,9)

# 소숫점 정리



# 완성
'''
    score  academy
1    75.0    1.000
2    77.0    1.000
3    83.0    2.000
4    65.0    0.000
5    80.0    3.000
6    83.0    3.000
7    70.0    1.000
8    79.0    2.000
평균   76.5    1.625
'''








