###########################################
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
###########################################

# 검색어 입력
query = input("검색어 입력 : ")

# 크롬 실행
driver = webdriver.Chrome()

# 검색결과 페이지 바로 접속
driver.get('https://www.youtube.com/results?search_query='+query)

# 제목 요소 접근
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

for i in titles:
    print(i.text)  # innerHTML 값

time.sleep(5)
