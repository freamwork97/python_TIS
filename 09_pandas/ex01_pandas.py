import pandas as pd

# 시리즈 선언
seris1 = pd.Series([2, 4, 5, 6, 10])
print(seris1)

# index 지정
seris2 = pd.Series([2, 4, 5, 6, 10], index=[1, 2, 3, 4, 5])
print(seris2)

# range로 index 지정
seris3 = pd.Series([2, 4, 6, 7, 10], index=range(1, 6))
print(seris3)

# index용 리스트
index_value = [10, 11, 12, 13, 14]
seris4 = pd.Series([2, 4, 6, 7, 19], index=index_value)
print(seris4)

# 데이터, index 따로 선언 후 활용
data_value = [1, 43, 25, 224, 75]
index_value = [10, 11, 12, 13, 14]
seris5 = pd.Series(data_value, index=index_value)
print(seris5)
