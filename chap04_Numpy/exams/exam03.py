'''
step03_reshape 관련문제
문) 다음과 같이  단계별로 자료구조를 생성하시오.
    단계1 : 1~84 정수를  이용하여 벡터 생성
    단계2 : 벡터를 대상으로 7x3x4 구조의 3차원 배열로 모양 변경
    단계3 : 3차원 배열을 대상으로 (행,면,열) 축의 순서로 구조 변경
'''

import numpy as np

# 1. vector 생성 
num1 = np.arange(1,85)
num1.shape # (84,)
print(num1)

# 2. 3차원 배열 
num2 = num1.reshape(7,3,4)
num2.shape # (7, 3, 4)
print(num2)

# 3. transpose(행,면,열)
# (면0,행1,열2) -> (행1,면0,열2)
num3 = num2.transpose(1,0,2)
num3.shape # (3, 7, 4)
print(num3)


