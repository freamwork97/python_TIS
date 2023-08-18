###########################################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
###########################################

###########################################
# 1. 유튜브 홈페이지 접속
# 2. 검색어 입력
# 3. 엔터
# 4. 필터 클릭
# 5. 조회수 클릭
# 6. 무한 스크롤
# 7. 제목 수집
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
driver.get('https://www.youtube.com/')
time.sleep(2)

# 무한스크롤 함수 호출
scroll_fun()

# 제목 요소 접근
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

for i in titles:
    if i.get_attribute("aria-label") and i.text:  # shorts 영상을 걸러내기 위한 조건문
        # aria_label 속성값 가져오기
        aria_label = i.get_attribute("aria-label")

        print(aria_label)

        start_index = aria_label.rfind("조회수")+4
        end_index = aria_label.rfind("회")
        hits = aria_label[start_index:end_index]
        hits = int(hits.replace(",", ""))
        print('제목', i.text)
        print('조회수', hits)
