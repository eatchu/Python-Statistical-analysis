'''
 문) 아래 url을 이용하여 어린이날(20200505)에 제공된 뉴스 기사를 
   1~5페이지 크롤링하는 크롤러 함수를 정의하고 크롤링 결과를 확인하시오.
   
   base_url = "https://news.daum.net/newsbox?regDate="   
   
   <조건1> 크롤러 함수의 파라미터(page번호, 날짜)
   <조건2> 크롤링 대상  : <a> 태그의 'class=link_txt' 속성을 갖는 내용 
   <조건3> 크롤링 결과 확인  : news 갯수와  문장 출력(한글 깨짐 확인)  
'''

import urllib.request as req  # url 가져오기 
from bs4 import BeautifulSoup

base_url = "https://news.daum.net/newsbox?regDate="

# 클로러 함수(페이지, 검색날자) 
def crawler_func(pages, date):
    crawling_news = [] # news 저장 
    
    # 내용 채우기 
    url = base_url + str(date)
    final_url = [url + '&page=' + str(p) for p in range(1,pages+1)]
    
    for u in final_url:
        # 1. url 요청
        res = req.urlopen(u)
        src = res.read() # source
           
        # 2. html 파싱
        src = src.decode('utf-8')
        html = BeautifulSoup(src, 'html.parser')
            
        # 3. tag[속성='값'] -> 'a[class="link_txt"]'
        links = html.select('a[class="link_txt"]')   
        one_page = []
        
        for link in links :
            link_str = str(link.string) # 내용 추출
            one_page.append(link_str.strip()) # 문장 끝 불용어 처리(\n, 공백)
            
        crawling_news.extend(one_page)
        
    return crawling_news # list


# 클로러 함수 호출 
crawling_news=crawler_func(5, '20200505')

# 크롤링 결과 확인
print('크롤링 news 수 =', len(crawling_news)) 
print(crawling_news)



    
