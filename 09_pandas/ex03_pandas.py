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
