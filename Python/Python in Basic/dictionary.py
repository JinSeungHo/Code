# # 사전 (dictionary)
# # key-value pair (키-값 쌍)
#
# my_dictionary = {
#     5: 25,
#     2: 4,
#     3: 9
# }
# print(my_dictionary[3]) # dic[key]
#
# my_dictionary[9] = 81
# print(my_dictionary)
# # 인덱스랑 사전 차이점
# # 인덱스 --> 순서 key 정수만(0-ing)
# # 사전 --> 순서X key정수 값아니어도 됨

# 사전 활용법
my_family = {
    '엄마': '김자옥',
    '아빠': '이석진',
    '아들': '이동민',
    '딸': '이지영'
}

# print(my_family.values()) # 값 출력
# print(my_family.keys()) # 키값 출력
# print('이지영' in my_family.values()) # 값이 있는지 없는지(boolean)
# for value in my_family.values():
#     print(value)

# for문 key/value 값 출력

# for key in my_family.keys():
#     value = my_family[key] # 사전[키] = 값(value) 출력
#     print(key, value)

# #사전 key 값과 value값 바꾸기

def reverce_dict(Redict):
    new_Redict = {}

    for value, key in my_family.items():
        new_Redict[key] = value
    return new_Redict

def origin_dict(dict):
    new_dict = {}
    for key, value in my_family.items():
        new_dict[key] = value
    return new_dict

reverce = reverce_dict(my_family)
dict = origin_dict(my_family)

for key, value in dict.items():
    print(key, value)
print("------------")

for key, value in reverce.items():
    print(key, value)

# # 투표 결과 리스트
# votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', \
# '최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기', \
# '강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']
#
# # 후보별 득표수 사전
# vote_counter = {}
#
# for name in votes:
#     if name not in vote_counter:
#         vote_counter[name] = 1
#     else:
#         vote_counter[name] += 1
#
# print(vote_counter)


