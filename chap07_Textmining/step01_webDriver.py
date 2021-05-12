# -*- coding: utf-8 -*-
"""
실습 순서
 1. naver image search page - url
 2. 이름 -> submit 버튼 -> image search page
 3. file save
"""

from selenium import webdriver # obejct 생성 

name = input("검색할 이미지 입력 : ") # 강동호, 이병헌 

# driver object 생성 
driver = webdriver.Chrome("D:\\NCS\\9_Python-II\\workspace\\chap07_TextMining\\lecture05_selenium\\data\\chromedriver")
driver.implicitly_wait(3) # driver 초기화 : 3초 대기시간

# 1. naver image search page - url
url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
# url 가져오기 
driver.get(url)


# 2. 이름 -> submit 버튼 -> image search page
driver.find_element_by_name('query').send_keys(name)
# 검색 버튼 클릭 : xpath("//tag[@속성='값']") -> 클릭 
driver.find_element_by_xpath("//button[@class='bt_search']").click()


# 3. file save
print('file 저장 중...')
import time
time.sleep(5) # 5초 대기 
driver.save_screenshot("data/"+name+"_imagepage.png")
print('file 저장 완료...')

driver.close() # 브라우저 닫기 

# [실습] www.google.com에서 강호동 이미지 페이지 file 저장 









