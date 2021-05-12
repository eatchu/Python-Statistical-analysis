'''
step04_axis_dot 관련문제 : 
문) 다음 같은 입력 x와 가중치 w를 이용하여 hidden node를 구하시오.  
    <조건1> w(3,3) * x(3,1) = h(3,1)  
    <조건2> weight : 표준정규분포 난수 
    <조건3> X : 1,2,3    
'''

import numpy as np
li = [1,2,3]
x = np.array(li)
x.shape
w = np.random.randn(3,3)
h = x.dot(w)

print('weight data',w)

print('x data',x)

print('hidden',h)








