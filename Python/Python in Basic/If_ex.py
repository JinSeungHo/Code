# 자연수 100이하인 수 중에서 8의 배수 이면서 12의 배수가 아닌 값을 출력

# i = 1
#
# while i <= 100:
#     if i % 8 == 0 and i % 12 != 0:
#         print(i)
#     i += 1  # i 값이 증가는 것은 if문 밖에 있어야 한다.(무한루프)

# 1000미만의 자연수 2와 또는 3의 배수를 더한 결과 출력

# i = 1
# total = 0
#
# while i < 1000:
#     if i % 2 == 0 or i % 3 == 0:
#         total += i
#     i += 1
# print(total)

# 정수 120의 약수를 모두 출력하고, 총 몇개의 약수가 있는지 출력하는 프로그램을 써 보세요.
#
# N = 120
# i = 1
# count = 0
#
# while i <= N:
#     if N % i == 0:
#         print(i)
#         count += 1
#     i += 1
# print("{}의 약수는 총 {}개입니다.".format(N, count))

# 상수정의 (대문자로!)

# INTEREST_RATE = 0.12
# APERTMENT_PRICE_2016 = 1100000000

# 변수정의 (소문자)

# year = 1988
# bank_balance = 50000000
#
# while year < 2016:
#     bank_balance = bank_balance * (1 + INTEREST_RATE)
#     year += 1
# if bank_balance > APERTMENT_PRICE_2016:
#     print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(int(bank_balance - APERTMENT_PRICE_2016)))
# else:
#     print("{}원 차이로 미란 아저씨 말씀이 맞습니다.".format(int(APERTMENT_PRICE_2016 - bank_balance)))

# 피보나치 수열

# i = 1
# current = 1
# previous = 0
#
# while i <= 50:
#     print(current)
#     temp = previous
#     previous = current
#     current = current + temp
#     i += 1

# 구구단 만들기

i = 1
j = 1

while i <= 9:
    j = 1
    while j <= 9:
        print("{} * {} = {}".format(i, j, i*j))
        j += 1
    i += 1





























