###########################################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
###########################################


# 크롬 실행
driver = webdriver.Chrome()

# 접속할 주소
driver.get('https://www.youtube.com/')

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="video-title"]')))


# 제목 요소 접근
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

for i in titles:
    # print(i.text)  # innerHTML 값
    # print(i.tag_name)  # 해당 요소의 태그 이름
    print(i.get_attribute("aria-label"))  # 해당 요소의 aria-label 속성값 가져오기
