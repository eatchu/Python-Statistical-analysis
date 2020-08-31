'''
   문) 아래 url은  '다음'뉴스를 날자별로 검색하여 페이지 단위로 제공하는 사이트이다.
   url = 'https://media.daum.net/newsbox/?tab_cate=NE'
   
  url을 사용하여 어린이날(20190505)에 제공된 뉴스 기사를 1~5페이지 크롤링하는 
   크롤러 함수를 정의하고 크롤링 결과를 확인하시오.
   <조건1> 크롤러 함수의 파라미터(page번호, 날짜)
   <조건2> 크롤링 대상  : <a> 태그의 'class=link_txt' 속성을 갖는 내용 
   <조건3> 크롤링 결과 저장  : list에 저장
   <조건4> 크롤링 결과 확인  : 문장 갯수와  문장 콘솔 출력(한글 깨짐 확인)  
'''

import urllib.request as req  # url 가져오기 
from bs4 import BeautifulSoup

base_url = "https://media.daum.net/newsbox/?page={ipage}&tab_cate=NE&regDate={idate}"
crawling_news = [] # news 저장 

# 클로러 함수(페이지, 검색날자) 
def crawler_func(pages, date):
    
    # page 수 만큼 url 생성 
    for page in range(1, pages+1) : 
        # 1) url 작성 
        url = base_url.format(ipage = page, idate=date)
        # print(url)        
        
        # 2) url 요청 
        res = req.urlopen(url)
        data = res.read()
        
        # 3) decoding -> html parsing
        src = data.decode('utf-8')
        html = BeautifulSoup(src, 'html.parser')
        
        # 4) tag element 수집 -> 내용 -> list 저장 
        # 실시간 이슈 제외 
        '''
        <div id ="kakaoContent">
          <div id="cMain">
           <div id="mArticle">
        '''
        divs = html.select("div[id=kakaoContent] > div[id=cMain] > div[id=mArticle]")
        
        for div in divs :
            links = div.select("a[class=link_txt]")
            print(links)
         
         for link in links :
             cont = link.string
             crawling_news.append(str(cont).strip())            
        

# 클로러 함수 호출 
crawler_func(5, '20190505')

print('크롤링 news 수 =', len(crawling_news)) # 크롤링 news 수 = 380
print(crawling_news)
 

# 형태소 분석
from konlpy.tag import Kkma

kkma = Kkma() # object

str_news = str(crawling_news)
print(str_news)

ex_sent = kkma.sentences(str_news)
print(ex_sent)

from re import match

# 1. 문장 -> 단어 -> 전처리 -> 워드카운트 
news_count = {}
for sent in ex_sent :
    ex_noun = kkma.nouns(sent)
    for noun in ex_noun :
        if len(str(noun)) > 1 and not(match("^[0-9]", noun)) :
            news_count[noun] = news_count.get(noun, 0) + 1

print(news_count)
            
# 3. Counter object 
from collections import Counter

counter = Counter(news_count)            
top10_word = counter.most_common(10)
print(top10_word)
# [('의원', 7), ('북한', 7), ('발사', 7), ('미사일', 7), ('삼성', 7), ('무기', 7), ('트럼프', 6), ('뉴스', 6), ('영화', 6), ('전술', 6)]   
         
# 4. word cloud    

import pytagcloud

# tag에 color, size, tag 사전 구성 
word_count_list = pytagcloud.make_tags(top10_word, maxsize=80)
# maxsize : 최대 글자크기
print(word_count_list)

pytagcloud.create_tag_image(word_count_list,
                            'news_20190505.jpg', 
                            size=(900, 600), 
                            fontname='korean', rectangular=False)

from PIL import Image
import matplotlib.pyplot as plt

path = "D:\\NCS\\9_Python-II\\workspace\\chap07_TextMining\\example\\"
img = Image.open(path + "news_20190505.jpg")
plt.imshow(img)









