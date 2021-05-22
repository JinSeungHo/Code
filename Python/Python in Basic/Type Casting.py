# Type Castiong // Type Conversion(형 변환)

print(int(3.8)) # int (정수) --> 3
print(float(3)) # float(소수) --> 3.0
print(int("2") + int("5")) # " " 문자열을 정수형으로 변환
print(float("3") + float("4")) # " "문자열을 소수형으로 변환
print(str(2) + str(4)) # str(문자열) 2와 4을 출력
print("----------")

# 실습예제1
age = 7
# print("제 나이는" + age + "살 입니다.")
# 형 변환을 하지 않으면 오류가 뜬다.
# 문자열과 정수는 연산이 불가!

print("제 나이는 " + str(age) + "살 입니다.")
print("----------")

# 실습예제2

# 오늘은 2021년 03월 13일 입니다.

year = 2021
month = 3
day = 13

print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day) + "일 입니다.")
# 코드가 길어지고 번거로움

# format 함수 사용
print("오늘은 {}년 {}월 {}일 입니다.".format(year, month, day))

# 추상화 // 캡슐화
date_string = "오늘은 {}년 {}월 {}일 입니다."
print(date_string.format(year, month, day))