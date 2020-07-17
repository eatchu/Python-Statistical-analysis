# -*- coding: utf-8 -*-
"""
SVD 알고리즘 적용 - 추천시스템
"""

import pandas as pd # csv file 
from surprise import SVD, accuracy # model 생성/평가 
from surprise import Reader, Dataset # dataset 생성 

# 1. 데이터 가져오기 
ratings = pd.read_csv('C:/ITWILL/4_Python-II/data/movie_rating.csv')
print(ratings) #  평가자[critic]   영화[title]  평점[rating]

# 2. rating dataset 생성 
reader = Reader(rating_scale=(1, 5))
data = Dataset(reader)
dataset = data.load_from_df(ratings[['critic','title','rating']], reader)

# train/test 
train = dataset.build_full_trainset()
test = train.build_anti_testset()

svd = SVD()
model = svd.fit(train)

# 3. 전체 사용자 대상 예측치 
pred = model.test(test)
pred
# uid='Jack', iid='Just My', r_ui=3.225806451612903, est=3.046417620945913,
# uid : 사용자, iid : 영화, r_ui : 실제 평점, est : 예측치 평점 

# uid='Toby'
'''
uid='Toby', iid='Lady', r_ui=3.225806451612903, est=2.9524439574190273
uid='Toby', iid='The Night', r_ui=3.225806451612903, est=3.432112698605785 - 1
uid='Toby', iid='Just My', r_ui=3.225806451612903, est=3.005451912950208
'''

# 4. 개별 사용자 대상 예측치 
user_id = 'Toby' # 추천 대상자 
items_id = ['The Night', 'Just My', 'Lady'] # 추천 item 
actual_rating = 0 # 실제 평점 

for item in items_id :
    print(model.predict(user_id, item, actual_rating))
    
'''
user: Toby       item: The Night  r_ui = 0.00   est = 3.43   {'was_impossible': False}
user: Toby       item: Just My    r_ui = 0.00   est = 3.01   {'was_impossible': False}
user: Toby       item: Lady       r_ui = 0.00   est = 2.95   {'was_impossible': False}
'''








