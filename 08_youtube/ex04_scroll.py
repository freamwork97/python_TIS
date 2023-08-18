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
# h1: 처음 페이지 열었을 때 높이 값
h1 = driver.execute_script("return document.documentElement.scrollHeight")
print('처음높이 : ', h1)

# 스크롤을 현재높이 만큼 내리기
driver.execute_script(
    "window.scrollTo(0,document.documentElement.scrollHeight)")
time.sleep(2)

# 스크롤 내린 뒤 높이 값
h2 = driver.execute_script("return document.documentElement.scrollHeight")
print("두번째 높이 : ", h2)
time.sleep(2)

driver.execute_script(
    "window.scrollTo(0,document.documentElement.scrollHeight)")
time.sleep(2)

h3 = driver.execute_script("return document.documentElement.scrollHeight")
time.sleep(2)
print("세번째 높이 : ", h3)
time.sleep(2)
