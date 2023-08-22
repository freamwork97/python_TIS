###############################
from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import pymysql
###############################
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


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


# 크롬 실행
driver = webdriver.Chrome()

# 접속할 주소
driver.get('https://www.youtube.com/feed/trending')
time.sleep(2)

# 무한스크롤 함수 호출
scroll_fun()

# 제목 요소 접근
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

# 제목 저장 리스트
title_list = []
# 조회수 저장 리스트
hits_list = []

for i in titles:
    if i.get_attribute("aria-label") and i.text:  # shorts 영상을 걸러내기 위한 조건문
        # aria_label 속성값 가져오기
        aria_label = i.get_attribute("aria-label")

        start_index = aria_label.rfind("조회수")+4
        end_index = aria_label.rfind("회")
        hits = aria_label[start_index:end_index]
        hits = int(hits.replace(",", ""))

        # 제목, 조회수 리스트에 담기
        # append() 리스트에 데이터 추가
        title_list.append(i.text)
        hits_list.append(hits)

# 제목, 조회수 리스트가 담긴 딕셔너리
crawling_result = {
    "title": title_list,
    "hits": hits_list
}

result = pd.DataFrame(crawling_result)
# Dataframe을 csv로 저장
# result.to_csv('./10_youtube/result.csv', encoding='utf-8-sig')
# 조회수 내림차순으로 정렬 후 csv로 저장
result.sort_values(by=['hits'], ascending=False).to_csv(
    './13_youtube_crawling/result.csv', encoding='utf-8-sig')

conn = pymysql.connect(
    host='127.0.0.1',
    user='user_python',
    password='1234',
    db='db_python',
    charset='utf8mb4')

cur = conn.cursor()
sql = "insert into `table1`(title, hit) values(%s, %s);"
tuple_result = list(zip(title_list, hits_list))
cur.executemany(sql, tuple_result)

conn.commit()


okt = Okt()

word_list = []


# 명사(Noun), 형용사(Adjective만 추출
for t in title_list:
    for word, tag in okt.pos(t):
        if tag in ['Noun', 'Adjective']:
            print(word, tag)
            word_list.append(word)

# 같은 단어 노출 빈도
word_list_count = Counter(word_list)


# 단어로 이루어진 리스트 생성
words = []
for word, count in word_list_count.most_common(10):
    words.append(word)

# words = [word for word, count in word_list_count.most_common(5)]
# 횟수로 이루어진 리스트 생성
counts = [count for word, count in word_list_count.most_common(10)]
plt.bar(words, counts)
plt.show()

# 워드클라우드 객체 생성
wc = WordCloud(font_path='./12_wordcloud/NanumGothic.ttf',
               width=400, height=400)

# Counter로 분석한 데이터를 워드클라이드로 만들기
result = wc.generate_from_frequencies(word_list_count)


# matplotlib로 이미지 출력
plt.axis('off')  # x,y축 생략

# 결과 이미지로 출력할 준비
plt.imshow(result)

# 이미지 출력
plt.show()
