###########################################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
###########################################


# 크롬 실행
driver = webdriver.Chrome()

# 접속할 주소
driver.get('https://www.naver.com/')
time.sleep(2)


###########################################
# 엔터 활용
# 검색창 접근
search = driver.find_element(By.XPATH, '//*[@id="query"]')

# 검색어 입력
search.send_keys('애플')
search.send_keys(Keys.RETURN)
###########################################

# 뉴스 더보기
many = driver.find_element(
    By.XPATH, '//*[@id="main_pack"]/section[1]/div/div[3]/a')
many.send_keys(Keys.RETURN)


# 제목 요소 접근
titles = driver.find_elements(By.CLASS_NAME, 'news_tit')
# //*[@id="sp_nws_all2"]/div/div/a
for i in titles:
    print(i.text)  # innerHTML 값
    # print(i.tag_name)  # 해당 요소의 태그 이름
    # print(i.get_attribute("aria-label"))  # 해당 요소의 aria-label 속성값 가져오기
