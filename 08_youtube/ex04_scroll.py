# selenium으로 javascript 코드 적용
###########################################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
###########################################


# 크롬 실행
driver = webdriver.Chrome()

# 검색결과 페이지 바로 접속
driver.get('https://www.youtube.com/')


# javascript로 현재 페이지 높이값 가져오기
# excute_script(): javascript 코드 실행해주는 함수
# javascript 실행값을 파이썬 변수로 받으려면 return을 작성해야한다
h = driver.execute_script("return document.documentElement.scrollHeight")
print(h)
