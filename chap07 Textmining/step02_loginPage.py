# -*- coding: utf-8 -*-
"""
1. 인증 페이지 접속 
2. 인증(id/pwd)
3. 인증 성공 -> server 접속 
4. 검색어(1~10) crawling
"""

from selenium import webdriver
from bs4 import BeautifulSoup

uid = input("id 입력 : ")
pwd = input("pwd 입력 : ")

driver = webdriver.Chrome("D:\\NCS\\9_Python-II\\workspace\\chap07_TextMining\\lecture05_selenium\\data\\chromedriver")
driver.implicitly_wait(3) # driver 초기화 : 3초 대기시간

url = "D:\\NCS\\9_Python-II\\workspace\\chap07_TextMining\\lecture05_selenium\\data\\login.html"
driver.get(url) # url

src = driver.page_source # text
html = BeautifulSoup(src, "html.parser")

form = html.find("form")
# <form name="frm"  method="post" action="http://www.naver.com"
server = form.attrs['action']
print('server : ', server)
# http://www.naver.com

# id/pwd 입력상자 element -> id/pwd 입력 
eid = driver.find_element_by_id('id')
eid.clear() # 입력상 지우기 
eid.send_keys(uid) # id 입력 

epwd = driver.find_element_by_id('pwd')
epwd.clear()
epwd.send_keys(pwd)

# submit 버튼 -> [인증] -> server 
# selector("tag.selector[속성=값]")
btn = driver.find_element_by_css_selector("input.login_b[type=submit]")
btn.submit() # submit 버튼 클릭 

# server(www.naver.com) -> 실시간검색어(top10)
driver.get(server)

src = driver.page_source
html = BeautifulSoup(src, "html.parser")
print(html)

# 1순위 tag(ul) 
ul_tag = html.select_one("ul[data-list='1to10']")

# 2순위 tag(li)
lis = ul_tag.find_all('li')

# 3순위
search_word = []
for li in lis : 
    word = li.select_one("span[class=ah_k]")
    search_word.append(str(word.string).strip())
    
# 1~10 검색어     
#print(search_word)

cnt = 0 
for word in search_word : 
    cnt += 1
    print(cnt, '->', word)

