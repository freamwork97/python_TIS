# 딕셔너리(dictionary):매핑형(key:value)

word_dic = {'dog': '강아지',
            'cat': '고양이',
            'tiger': "호랑이",
            'lion': '사자'
            }

print(word_dic)
print(word_dic['cat'])
# 기존 value 수정
word_dic['cat'] = '나비탕'
# 새로운 데이터 추가
word_dic['bear'] = '곰'

print(word_dic['bear'])

word_dic['dog'] = '보신탕'
word_dic['bear'] = '곰탕'