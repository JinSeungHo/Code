# 리스트 문제

# greetings = ["안녕", "나하오", "워아이니", "하이", "반가워"]

# i = 0
#
# while i < len(greetings):
#     print(greetings[i])
#     i += 1

# 리스트 반복 문제
# 섭씨를 화씨로 면환하는 함수 (사용자 정의)
# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5 / 9
#
# temperature_list = [40, 15, 32, 64, -4, 11]
# print("화씨 온도 리스트: " + str(temperature_list)) # 화씨 온도 출력
#
# i = 0
# while i < len(temperature_list):
#     temperature_list[i] = round(fahrenheit_to_celsius(temperature_list[i]),1)
#     i += 1
#
# print("섭씨 온도 리스트: {}".format(temperature_list))

# 환전서비스
# 원화(￦)에서 달러($)로 변환하는 함수
# def krw_to_usd(krw):
#     return krw / 1000  # 1,000원 당 1달러
#
#
# # 달러($)에서 엔화(￥)로 변환하는 함수
# def usd_to_jpy(usd):
#     return usd / 8 * 1000 # 1000엔 당 8달러
#
#
# # 원화(￦)로 각각 얼마인가요?
# prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
# print("한국 화폐: " + str(prices))
#
# # prices를 원화(￦)에서 달러($)로 변환하기
# i = 0
# while i < len(prices):
#     prices[i] = krw_to_usd(prices[i])
#     i += 1
#
# # 달러($)로 각각 얼마인가요?
# print("미국 화폐: " + str(prices))
#
# # prices를 달러($)에서 엔화(￥)로 변환하기
# i = 0
# while i < len(prices):
#     prices[i] = usd_to_jpy(prices[i])
#     i += 1
#
# # 엔화(￥)로 각각 얼마인가요?
# print("일본 화폐: " + str(prices))








