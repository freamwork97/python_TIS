import pandas as pd

scores = pd.DataFrame(
    [
        [96, 76, 80, 64, 85],  # java
        [88, 90, 100, 40, 50],  # python
        [10, 20, 30, 50, 60]  # js
    ],
    index=["java", 'python', 'js']

)


print(scores)

student_number = [1, 2, 3, 4, 5]
scores = pd.DataFrame(
    [
        [96, 88, 10],
        [76, 92, 20],
        [60, 100, 30],
        [85, 55, 40],
        [80, 70, 50]
    ],
    index=student_number
)
print(scores)

scores = pd.DataFrame(
    {
        "java": [96, 76, 80, 64, 85],  # java
        "python": [88, 90, 100, 40, 50],  # python
        'js': [10, 20, 30, 50, 60]  # js
    },
    index=student_number
)
print(scores)

# 딕셔너리 데이터를 DataFrame으로 변환
scores_dict = {
    "java": [96, 76, 80, 64, 85],  # java
    "python": [88, 90, 100, 40, 50],  # python
    'js': [10, 20, 30, 50, 60]  # js
}

scores = pd.DataFrame(scores_dict)

print(scores)


scores = pd.DataFrame(
    {
        "java": [96, 76, 80, 64, 85],  # java
        "python": [88, 90, 100, 40, 50],  # python
        'js': [10, 20, 30, 50, 60]  # js
    },
    index=student_number
)
print(scores)

# 이름 데이터 추가
scores['이름'] = ['김파이', '이파이', '빅파이', '스몰파이', '미드파이']
print(scores)

# 데이터 추가
scores.loc[6] = [80, 80, 80, '조파이']
print(scores)

# 학번, 이름, 성적 모두 포함한 DataFrame선언

student_number = [1, 2, 3, 4, 5, 6]

scores = pd.DataFrame(
    {
        '이름': ['생선', '양고기', '닭고기', '나비탕', '곰탕', '보신탕'],
        "java": [96, 76, 80, 64, 85, 86],  # java
        "python": [88, 90, 100, 40, 50, 92],  # python
        'js': [10, 20, 30, 50, 60, 100]  # js
    },
    index=student_number
)
print(scores)

# index 기준 정렬
print(scores.sort_index())
# index 기준 내림차순
print(scores.sort_index(ascending=False))

# '이름' 열 기준 오름차순 정렬
print(scores.sort_values(by='이름', ascending=True))
# '이름' 열 기준 내림차순 정렬
print(scores.sort_values(by='이름', ascending=False))
# python 기준 오름차순 정렬
print(scores.sort_values(by='python', ascending=True))
# python 기준 내림차순 정렬
print(scores.sort_values(by='python', ascending=False))

# 첫 2줄만 조회
print(scores.head(2))
# 마지막 2줄만 조회
print(scores.tail(2))

# DataFrame을 csv로 내보내기
scores.to_csv('./09_pandas/scores.csv', encoding='utf-8-sig')
