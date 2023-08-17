from ex03_function import *

run = True
while run:
    num = int(input("숫자를 입력 : "))
    if num == 1:
        mul1()
    elif num == 2:
        mul2()
    elif num == 3:
        print("종료")
        run = False
