# 실행하면 콘솔에서 1또는2를 입력받고 1은 세로형구구단, 2는 가로형구구단을 각각 출력한다.
# 구구단은 각각 함수로 정의하도록 한다.


def mul(num):
    if num == 1:
        for i in range(2, 10):
            for j in range(1, 10):
                print(i, "x", j, "=", i*j)
    elif num == 2:
        for i in range(2, 10):
            for j in range(1, 10):
                print(i, "x", j, "=", i*j, end=" ")
            print()


num = int(input("숫자를 입력 : "))
mul(num)
