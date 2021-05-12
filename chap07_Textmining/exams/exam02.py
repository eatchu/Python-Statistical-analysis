# -*- coding: utf-8 -*-
'''
# 문) 2019년11월 ~ 2020년2월 까지(4개월) daum 뉴스기사를 다음과 같이 크롤링하고, 단어구름으로 시각화 하시오.
# <조건1> 날짜별 5개 페이지 크롤링
# <조건2> 불용어 전처리 
# <조건3> 단어빈도수 분석 후 top 20 단어 단어구름 시각화 
'''

import urllib.request as req # url 요청
from bs4 import BeautifulSoup # html 파싱
import pandas as pd # 시계열 date


# 1. 날짜별 5개 페이지 크롤링
date = pd.date_range("2019-11-01", "2020-02-29")
len(date) # 121
date[0] # '2019-11-01 00:00:00'

import re # sub('pattern','',string)
sdate = [re.sub('-','',str(d))[:8] for d in date]
sdate[:10]

final = []
for date in sdate:
    for page in range(1,6):
        url = f"https://news.daum.net/newsbox?regDate={date}&page={page}"
        try:
             # url 요청
            res = req.urlopen(url)
            src = res.read() # source
               
             # html 파싱
            src = src.decode('utf-8')
            html = BeautifulSoup(src, 'html.parser')
                
             # tag[속성='값'] -> 'a[class="link_txt"]'
            links = html.select('a[class="link_txt"]')   
            
            one_page_data = [] # 빈 list
            
            for link in links :
                link_str = str(link.string) # 내용 추출
                one_page_data.append(link_str.strip()) # 문장 끝 불용어 처리(\n, 공백)
            final.extend(one_page_data[:40])
        
        except Exception as e:
            print('오류발생:',e)    

len(final) # 121x5x40 = 24200
final[:10]
type(final) # list



# 2. 불용어 전처리
from konlpy.tag import Kkma # class
from wordcloud import WordCloud
import pickle


# object 생성
kkma = Kkma()
ex_sent = [kkma.sentences(sent)[0] for sent in final]


from re import match, split
sentence_nouns = [] 
for sent in ex_sent: 
    word_vec = ""
    for noun in kkma.nouns(sent): # 문장 -> 명사 추출
        if len(noun) > 1 and not (match('^[0-9]',noun)):
            word_vec += noun + " " # 단어마다 공백으로 구분           
    sentence_nouns.append(word_vec)

sentence_nouns[:10]

# 3. 단어빈도수 분석 후 top 20 단어 단어구름 시각화 

# 불필요 단어 제거
word_count = {}
for sent in sentence_nouns:
    for word in sent.split(sep=' '):
        if len(word) > 1 and not (match('^[0-9]',noun)):
            word_count[word] = word_count.get(word,0) + 1

len(word_count) # 19143


from collections import Counter # class


counter = Counter(word_count)
top20_word = counter.most_common(20)
top20_word
'''
[('종합', 3469),
 ('코로나', 1433),
 ('한국', 1081),
 ('정부', 700),
 ('중국', 657),
 ('단독', 641),
 ('검찰', 587),
 ('대통령', 556),
 ('수사', 469),
 ('신종', 436),
 ('사망', 424),
 ('환자', 413),
 ('트럼프', 409),
 ('진자', 404),
 ('경찰', 399),
 ('논란', 391),
 ('조사', 389),
 ('국회', 332),
 ('서울', 328),
 ('총선', 321)]
'''



# wordcloud 시각화
wc= WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',
              width=500, height=400,
              max_words=100, max_font_size=150,
              background_color='white')
wc_result = wc.generate_from_frequencies(dict(top20_word)) # dict

import matplotlib.pyplot as plt
plt.imshow(wc_result)



