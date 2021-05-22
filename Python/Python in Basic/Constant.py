# 상수(constants)

PI = 3.14 # 상수) 절대로 바꾸지 않을 값 대문자로 사용 -->관례

# 반지름을 받아서 원의 넓이 계산
def calaulate_area(r):
    return PI * r * r

redius = 4 # 반지름
print("반지름이 {}이면, 넓이는 {}".format(redius, calaulate_area(redius)))

redius = 6 # 반지름
print("반지름이 {}이면, 넓이는 {}".format(redius, calaulate_area(redius)))

redius = 7 # 반지름
print("반지름이 {}이면, 넓이는 {}".format(redius, calaulate_area(redius)))
