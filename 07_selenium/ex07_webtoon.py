###########################################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
###########################################


# 크롬 실행
driver = webdriver.Chrome()

# 접속할 주소
driver.get('https://comic.naver.com/webtoon')
# time.sleep(5)

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, '[class="text"]')))

# 네이버 웹툰 제목 요소 접근
webtoon = driver.find_elements(By.CSS_SELECTOR, '[class="text"]')

for i in webtoon:
    print(i.text)
print('전체 수 : ', len(webtoon))
