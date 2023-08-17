###########################################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
###########################################


# 크롬 실행
driver = webdriver.Chrome()

# 접속할 주소
driver.get(
    'https://prod.danawa.com/list/?cate=112758&shortcutKeyword=노트북')

# 노트북 상품명 접근
notebook_name = driver.find_elements(By.CSS_SELECTOR, '[name="productName"]')

for i in notebook_name:
    print(i.text)
time.sleep(15)
