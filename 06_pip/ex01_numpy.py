import numpy as np

# numpy 배열 선언

arr = np.array([8, 4, 7, 1, 3, 2, 5, 6])
print(arr)
print('-----------------')

# 정렬
arr = np.sort(arr)
print(arr)
print('-----------------')

# 2개의 배열 합침
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
arr3 = np.concatenate((arr1, arr2))
print(arr3)
print('-----------------')

# 배열 연산
arr11 = arr+10
print("arr11 : ", arr11)
print('-----------------')
arr12 = arr1-arr2
print(f'arr12 : {arr12}')

# 배열 슬라이싱(특정 인덱스 범위 접근하기)
arr4 = np.arange(1, 11)
print(arr4[:2])  # 0~1번 인덱스
print(arr4[1:2])  # 1번 인덱스
print(arr4[3:8])  # 3~7번 인덱스
print(arr4[6:])  # 6번인덱스 부터
