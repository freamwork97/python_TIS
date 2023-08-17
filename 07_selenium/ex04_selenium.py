###########################################
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
###########################################

# 크롬 실행
driver = webdriver.Chrome()

# 접속할 주소
driver.get("https://naver.com")

# 로그인 버튼 xpath 접근
login_button = driver.find_element(By.XPATH, '//*[@id="account"]/div/a')

# 로그인 버튼 클릭
login_button.click()

login2 = driver.find_element(By.XPATH, '//*[@id="log.login"]')
login2.click()

time.sleep(15)
