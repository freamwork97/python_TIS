###############################
from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
###############################

okt = Okt()

text = '안녕하세요. 파이썬 입니다. 저는 파이썬을 배우고 있어요'
text += '파이썬이 너무 좋아요 재밌어요 파이썬 만세 파이썬을 사랑합니다.'
text += '안녕하세요 크롤링 재미있어요.'

word_list = []

# 명사(Noun), 형용사(Adjective만 추출
for word, tag in okt.pos(text):
    if tag in ['Noun', 'Adjective']:
        print(word, tag)
        word_list.append(word)

# 같은 단어 노출 빈도
word_list_count = Counter(word_list)

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

# 워드 클라우드 파일저장
wc.to_file('wordcloud_result.png')
