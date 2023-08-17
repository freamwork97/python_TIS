# 실행하면 콘솔에서 1또는2를 입력받고 1은 세로형구구단, 2는 가로형구구단을 각각 출력한다.
# 구구단은 각각 함수로 정의하도록 한다.

def mul1():
    for i in range(2, 10):
        for j in range(1, 10):
            print(i, "x", j, "=", i*j)


def mul2():
    for i in range(2, 10):
        for j in range(1, 10):
            print(i, "x", j, "=", i*j, end=" ")
        print()


run = True

while run:
    num = int(input("숫자입력 : "))

    if num == 1:
        print("1번")
        mul1()
    elif num == 2:
        print("2")
        mul2()
    elif num == 3:
        print("종료")
        break
