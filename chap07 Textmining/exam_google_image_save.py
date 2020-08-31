# -*- coding: utf-8 -*-
"""
[실습] www.google.com에서 강호동 이미지 페이지 file 저장
      중고급 : 1~5 이미지 file 저장  
"""
from selenium import webdriver

name = input("검색할 이름 입력 : ")
# image url
url = "https://www.google.co.kr/imghp?hl=ko&tab=wi"
driver = webdriver.Chrome("D:\\NCS\\9_Python-II\\workspace\\chap07_TextMining\\lecture05_selenium\\data\\chromedriver")

# 1. naver image search page - url
driver.get(url) # url 가져오기 


# 2. 이름 -> submit 버튼 -> image search page
driver.find_element_by_name('q').send_keys(name)
# 검색 버튼 클릭 : xpath("//tag[@속성='값']") -> 클릭 
driver.find_element_by_xpath("//button[@class='Tg7LZd']").click()


# 3. file save
print('file 저장 중...')
import time
time.sleep(5) # 5초 대기 
driver.save_screenshot("data/"+name+"_googleImagepage.png")
print('file 저장 완료...')

driver.close() # 브라우저 닫기 