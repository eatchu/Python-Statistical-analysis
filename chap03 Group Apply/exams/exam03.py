import pandas as pd

election = pd.read_csv('data/election_2012.csv', encoding='ms949')
print(election.info()) # 1001731 x 16
'''
cand_id : 대선 후보자 id
cand_nm : 대선 후보자 이름
contbr_nm : 후원자 이름 
contbr_occupation : 후원자 직업군 
contb_receipt_amt : 후원금 
'''

# DF 객체 생성 
name = ['cand_nm', 'contbr_occupation', 'contb_receipt_amt'] 
# subset 생성 
election_df = pd.DataFrame(election, columns= name)
print(election_df.info())
print(election_df.head())
print(election_df.tail())


# 중복되지 않은 대선 후보자 추출 
unique_name = election_df['cand_nm'].unique()
print(len(unique_name)) # 13
print(unique_name) 

# 중복되지 않은 후원자 직업군 추출 
unique_occ =  election_df['contbr_occupation'].unique()
print(len(unique_occ)) # 45074
print(unique_occ)


#############################################
#  Obama, Barack vs Romney, Mitt 후보자 분석 
#############################################

# 1. 두 후보자 관측치만 추출 : isin()
two_cand_nm=election_df[election_df.cand_nm.isin(['Obama, Barack','Romney, Mitt'])]
print(two_cand_nm.info())
print(two_cand_nm.head())
print(two_cand_nm.tail())
print(len(two_cand_nm)) # 700975
'''
문1) two_cand_nm 변수를 대상으로 피벗테이블 생성하기 
    <조건1> 교차셀 칼럼 : 후원금, 열 칼럼 : 대선 후보자,
             행 칼럼 : 후원자 직업군, 적용함수 : sum
    <조건2> 피벗테이블 앞부분 5줄 확인   
문2) 피벗테이블 대상 필터링 : 2백만달러 이상 후원금 대상     
'''

# 문1)
cand_pivot = pd.pivot_table(two_cand_nm, index='contbr_occupation',
                           columns='cand_nm', values='contb_receipt_amt',
                           aggfunc='sum')
cand_pivot.head()

# 문2)
cand2 = cand_pivot[cand_pivot.sum(axis=1)>=2000000]
print(cand2)


# 논리식 + 관계식
# and
import numpy as np
each_over = cand_pivot[np.logical_and
                       (cand_pivot['Obama, Barack']>=2000000,
                        cand_pivot['Romney, Mitt']>=2000000)]
print(each_over)

# or
each_over2 = cand_pivot[np.logical_or
                       (cand_pivot['Obama, Barack']>=2000000,
                        cand_pivot['Romney, Mitt']>=2000000)]
print(each_over2)

