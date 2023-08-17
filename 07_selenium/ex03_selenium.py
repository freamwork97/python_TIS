###########################################
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
###########################################

# 크롬 실행
driver = webdriver.Chrome()

# 접속할 주소
driver.get("https://selenium.dev")

# id = main_vavber요소 접근
id_element = driver.find_element(By.ID, "main_naver")


print(id_element.text)

# 10초 동안 현재 상태에서 대기
time.sleep(30)
