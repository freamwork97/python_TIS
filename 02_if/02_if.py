# 자바의 scanner처럼 실행 후 콘솔에서 숫자를 입력받아
# 홀수, 짝수 판별하여 출력하는 코드를 작성

num = int(input("숫자를 입력 : "))
if (num % 2 == 0):
    print("짝수")
else:
    print("홀수")
