# 나열형 list, tuple, range
# list타입

int_list = [1, 2, 3, 4, 5]

print(int_list)
print(int_list[0])
print(int_list[3])
int_list[3] = 500
print(int_list)

print('------------------------')
# 문자열
str_list = ['hello', '안녕', 'ㅂㄷㅇㅁㅇ']
print(str_list)
print(str_list[0])
print(str_list[2])

print('------------------------')
# 다양한 자료형 섞인 리스트
mix_list = [1, "hello", 10, 2.2, 30, '안녕']
print(mix_list)
print(mix_list[1])
print(mix_list[2])
print(mix_list[3])

print('------------------------')
# 리스트 내에 리스트
list_in_list = [100, 200, ['내부리스트', 10], 'ㅁㅇㅁㅈㅇ', '1.253']
print(list_in_list)
print(list_in_list[2])
print(list_in_list[2][0])
print(list_in_list[4])
print(list_in_list[1])
