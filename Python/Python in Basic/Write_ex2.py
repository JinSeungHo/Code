import random

# with open("data/Word_list.txt", "r") as F:
#     for line in F:
#         data = line.split(": ")
#         # print(data)
#         Korean = data[1].strip() # -->다음줄 리스트 사이에 \n이 붙여져서 strip사용
#         English = data[0]
#
#         quiz = input("{}: ".format(Korean))
#
#         while True:
#             if quiz == English:
#                 print("정답!")
#                 break
#             else:
#                 print("땡! 정답은 {}입니다.".format(English))
#                 break

# import random
#
# vocab = {}
# with open("data/Word_list.txt", "r") as F:
#     for line in F:
#         data = line.strip().split(": ")
#         English, Korean = data[0], data[1]
#         vocab[English] = Korean # keys - value 지정
#
# keys = list(vocab.keys())
#
# while True:
#     index = random.randint(0, len(keys) - 1) # --> 랜덤 수의 범위정하기
#     English = keys[index]
#     Korean = vocab[English]
#
#     guess = input("{}: ".format(Korean))
#
#     if guess == "q" or guess == "ㅂ":
#         break
#
#     if guess == English:
#         print("정답입니다.")
#     else:
#         print("땡! 정답은 {}입니다".format(English))

























