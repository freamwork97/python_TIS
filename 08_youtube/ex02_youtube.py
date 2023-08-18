###########################################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
###########################################


# 크롬 실행
driver = webdriver.Chrome()

# 유튜브 접속할 주소
# driver.get('https://www.youtube.com/')


# 검색결과 페이지 바로 접속
driver.get('https://www.youtube.com/results?search_query=콜오브듀티')

###########################################
# 엔터 활용
# 검색창 접근
# search = driver.find_element(By.CSS_SELECTOR, '[name="search_query"]')

# # 검색어 입력
# search.send_keys('콜오브듀티')
# search.send_keys(Keys.RETURN)
###########################################

###########################################
# 검색창 접근
# search_input = driver.find_element(By.CSS_SELECTOR, 'input#search')

# 검색어 입력
# search_input.send_keys('콜오브듀티')
# search_button = driver.find_element(
#     By.CSS_SELECTOR, 'button#search-icon-legacy')
# search_button.click()
###########################################

# 제목 요소 접근
titles = driver.find_elements(
    By.XPATH, '//*[@id="video-title"]')

for i in titles:
    print(i.text)  # innerHTML 값

time.sleep(5)
