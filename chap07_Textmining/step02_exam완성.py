'''
문) Crawler 함수에서 추출된 유기동물 유형(kind)을 대상으로
    단어 빈도수 구하고, 단어 구름으로 시각화 하시오.
'''

import pandas as pd 

crawling = pd.read_csv("../data/crawling_df.csv") 
print(crawling.info())


# 문1) 유기동물유형에 대한 단어 빈도수 
ani_kind = crawling['kind']
cnt = ani_kind.value_counts()
print(cnt)

# 문2) 단어 빈도수 -> 단어 구름 시각화(top5) 
import matplotlib.pyplot as plt

# 한글 지원 : 한글 깨짐 방지 
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

cnt.plot(kind = 'barh' , title = 'animal kind')
plt.show()
 
# 단어 빈도수 
word_count = {} # 빈 dict - 단어 빈도수

for word in ani_kind : 
    word_count[word] = word_count.get(word, 0) + 1
 

# 단어구름 시각화 
from collections import Counter
import pytagcloud

word_count2 = Counter(word_count)
word_count_top5 = word_count2.most_common(5) # top5

# tag에 color, size, tag 사전 구성 
word_count_list = pytagcloud.make_tags(word_count_top5, maxsize=80)
# maxsize : 최대 글자크기
print(word_count_list)

pytagcloud.create_tag_image(word_count_list,
                            'animal_wordcloud.jpg', 
                            size=(900, 600), 
                            fontname='korean', rectangular=False)   

