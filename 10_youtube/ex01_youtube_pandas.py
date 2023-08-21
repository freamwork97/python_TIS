###########################################
# 크롤링 결과 DataFrame저장하기
###########################################
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
###########################################

###########################################
# 1. 유튜브 인기급상승 접속
# 2. 무한 스크롤
# 3. 제목 수집
###########################################


def scroll_fun():
    while (True):

        # 스크롤 하기 전 높이
        h1 = driver.execute_script(
            "return document.documentElement.scrollHeight")

        # 스크롤을 현재높이 만큼 내리기
        driver.execute_script(
            "window.scrollTo(0,document.documentElement.scrollHeight)")
        time.sleep(2)

        # 스크롤 내린 뒤 높이 값
        h2 = driver.execute_script(
            "return document.documentElement.scrollHeight")

        # 스크롤 전, 후 높이 비교
        if h1 == h2:
            break


# 크롬 실행
driver = webdriver.Chrome()

# 접속할 주소
driver.get('https://www.youtube.com/feed/trending')
time.sleep(2)

# 무한스크롤 함수 호출
scroll_fun()

# 제목 요소 접근
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

# 제목 저장 리스트
title_list = []
# 조회수 저장 리스트
hits_list = []

for i in titles:
    if i.get_attribute("aria-label") and i.text:  # shorts 영상을 걸러내기 위한 조건문
        # aria_label 속성값 가져오기
        aria_label = i.get_attribute("aria-label")

        start_index = aria_label.rfind("조회수")+4
        end_index = aria_label.rfind("회")
        hits = aria_label[start_index:end_index]
        hits = int(hits.replace(",", ""))

        # 제목, 조회수 리스트에 담기
        # append() 리스트에 데이터 추가
        title_list.append(i.text)
        hits_list.append(hits)

# 제목, 조회수 리스트가 담긴 딕셔너리
crawling_result = {
    "title": title_list,
    "hits": hits_list
}

result = pd.DataFrame(crawling_result)
# Dataframe을 csv로 저장
# result.to_csv('./10_youtube/result.csv', encoding='utf-8-sig')
# 조회수 내림차순으로 정렬 후 csv로 저장
result.sort_values(by=['hits'], ascending=False).to_csv(
    './10_youtube/result2.csv', encoding='utf-8-sig')
