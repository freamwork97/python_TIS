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


query = input("검색어 입력 : ")


# 유튜브 접속
driver = webdriver.Chrome()
driver.get('https://www.youtube.com')

# 검색창 접근
search = driver.find_element(By.CSS_SELECTOR, '[name="search_query"]')

# 검색어 입력
search.send_keys(query)

# 엔터
search.send_keys(Keys.RETURN)
time.sleep(2)

# 필터버튼 접근
filter_button = driver.find_element(
    By.XPATH, '//*[@id="filter-button"]')

# 필터버튼 클릭
filter_button.click()

# 조회수 접근(full XPATH 사용)
fullxpath = '/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-search-filter-options-dialog-renderer/'
fullxpath += 'div[2]/ytd-search-filter-group-renderer[5]/ytd-search-filter-renderer[3]/a/div/yt-formatted-string'
hits = driver.find_element(By.XPATH, fullxpath)

# 조회수 클릭
hits.click()


# 무한스크롤 함수 호출
scroll_fun()

# 제목 가져오기
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

for i in titles:
    print(i.text)  # innerHTML 값
print("영상 갯수 : ", len(titles))
