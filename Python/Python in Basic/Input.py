# input ( 사용자 입력받기 )

# name = input("이름을 입력하세요 : ")
# print(name)
# x = int(input("숫자를 입력하세요 : ")) # input은 문자열 출력 -->변환해야함
# print(x + 5)

# # 숫자 맞히기 게임
# import random
# # 상수
# ANSWER = random.randint(1, 20)
# CHANCE = 4
# # 변수
# guess = -1
# tries = 0
#
# while guess != ANSWER and tries < CHANCE:
#     guess = int(input("기회가 {}번 남았습니다. (1-20) : ".format(CHANCE - tries)))
#     tries += 1
#
#     if ANSWER > guess:
#         print("up")
#     elif ANSWER < guess:
#         print("down")
# if guess == ANSWER:
#     print("축하합니다. {}번 만에 숫자를 맞히셧습니다.".format(tries))
#
# else:
#     print("아쉽습니다. 정답을 {}입니다.".format(ANSWER))