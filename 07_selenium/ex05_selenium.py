###########################################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
###########################################

# 크롬 실행
driver = webdriver.Chrome()

# 접속할 주소
driver.get("https://naver.com")

# 검색창 xpath 접근
search = driver.find_element(By.XPATH, '//*[@id="query"]')

# 검색어 입력
search.send_keys('오늘날씨')

# 검색버튼 클릭
# btn = driver.find_element(By.XPATH, '//*[@id="sform"]/fieldset/button')
# btn.click()
search.send_keys(Keys.RETURN)

time.sleep(15)
