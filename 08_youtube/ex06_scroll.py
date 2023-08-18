# selenium으로 javascript 코드 적용
###########################################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
###########################################

###########################################
# while문을 적용하여 무한스크롤 구현하기     #
# while문 내부동작                         #
# 1. 처음 높이값 확인                      #
# 2. 높이만큼 스크롤 내리기                 #
# 3. 높이값 확인                           #
# 4. 높이가 같다면 break로 while문 중단     #
###########################################

driver = webdriver.Chrome()
driver.get('https://www.youtube.com')

# 스크롤 후 제목데이터를 리턴하는 함수로 정의


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

    # 제목 가져오기
    titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
    return titles


# 무한스크롤 함수 호출
titles = scroll_fun()

for i in titles:
    print(i.text)  # innerHTML 값
print("영상 갯수 : ", len(titles))
