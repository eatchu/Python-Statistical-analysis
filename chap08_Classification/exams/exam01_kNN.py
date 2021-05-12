'''
문) 다음과 같은 3개의 범주를 갖는 6개의 데이터 셋을 대상으로 kNN 알고리즘을 적용하여 
      특정 품목을 분류하시오.
   (단계1 : 함수 구현  -> 단계2 : 클래스 구현)  
      
    <조건1> 데이터 셋  
    -------------------------
   품목     단맛 아삭거림 분류범주
    -------------------------
    grape   8   5     과일
    fish    2   3     단백질 
    carrot  7   10    채소
    orange  7   3     과일 
    celery  3   8     채소
    cheese  1   1     단백질 
    ------------------------
    
   <조건2> 분류 대상과 k값은 키보드 입력  
   
  <<출력 예시 1>> k=3인 경우
  -----------------------------------
    단맛 입력(1~10) : 8
    아삭거림 입력(1~10) : 4
  k값 입력(1 or 3) : 3
  -----------------------------------
  calssCount: {'과일': 2, '단백질': 1}
   분류결과: 과일
  -----------------------------------
  
  <<출력 예시 2>> k=1인 경우
  -----------------------------------
   단맛 입력(1~10) : 2
   아삭거림 입력(1~10) :3
  k값 입력(1 or 3) : 1
  -----------------------------------
  calssCount: {'단백질': 1}
   분류결과 : 단백질
  -----------------------------------
'''

import numpy as np

grape = [8, 5]
fish = [2, 3]
carrot = [7, 10]
orange = [7, 3]
celery = [3, 8]
cheese = [1, 1]
class_category = ['과일', '단백질', '채소', '과일', '채소', '단백질']

class knn_algo:   
    def data_set(self):
        sweet, crisp, self.k = map(int, input('단맛, 아삭거림, k값입력').split(','))
        self.know = np.array([grape,fish,carrot,orange,celery,cheese]) # 알려진 집단 
        self.unknow = np.array([sweet, crisp]) # 알려지지 않은 집단
        self.cate = np.array(class_category) # 정답(분류범주)
        
    def knn_classfy(self):
        # 단계1 : 거리식 계산
        square_diff = (self.know-self.unknow)**2
        sum_square = square_diff.sum(axis=1)
        distance = np.sqrt(sum_square)
        # 단계2 : 오름차순 정렬
        sortDist = distance.argsort()
        # 단계3 : 최근접 이웃
        self.classify_re = {}
        for i in range(self.k):
            key = self.cate[sortDist[i]] 
            self.classify_re[key] = self.classify_re.get(key,0) + 1
        return self.classify_re 
    
    def vote(self):
        self.v = [key for key in self.classify_re.keys() 
                  if self.classify_re[key] == max(self.classify_re.values())]
        return self.v[0]
    

a = knn_algo()
a.data_set()
a.knn_classfy() 
a.vote()
# max(class_result,key=class_result.get)




