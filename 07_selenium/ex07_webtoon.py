###########################################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
###########################################


# 크롬 실행
driver = webdriver.Chrome()

# 접속할 주소
driver.get('https://comic.naver.com/webtoon')
time.sleep(5)

webtoon = driver.find_elements(By.CSS_SELECTOR, '[class="text"]')

for i in webtoon:
    print(i.text)
