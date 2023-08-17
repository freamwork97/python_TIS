# 구구단 함수 ex03_function.py에 각각 작업하고
# main에서 1,2 번 선택을 받아 세로형 가로형을 각각
# 출력

def mul1():
    for i in range(2, 10):
        for j in range(1, 10):
            print(f'{i} * {j} = {i*j}')


def mul2():
    for i in range(2, 10):
        for j in range(1, 10):
            print(f'{i} * {j} = {i*j}', end=' ')
        print()
