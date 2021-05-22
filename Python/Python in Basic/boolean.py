# boolean함수

print(bool(7>3))
print("----------")
# 그냥 bool함수를 적으면 출력명령어가 없기 때문에 출력이 안된다.

# AND연산 ~이고 둘다 참이어야 참(true) 나머지 거짓(false)
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print("----------")

# OR연산 ~또는 둘다 거짓이아야 거짓(false) 나머지 참(true)
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print("----------")

# NOT연산 반대 연산
print(not True)
print(not False)
print("----------")

# 예제(숫자형)
print(2 > 1)
print(2 < 1)
print(3 >= 2)
print(3 <= 3)
print(2 == 2)   # (==) 등호가 두개일 경우 --> 2는 2와 같다
print(2 != 2)
print("----------")

# 예제(문자형)
print("hello" == "hello")
print("hello" != "hello")
print("----------")

# 예제(복합)
print(2 >1 and "hello" == "hello")
print(not not True)
print(not not False)
print(7 == 7 or (4 < 3 and 12 > 10))
print("----------")

x = 3
print (x > 4 or not (x < 2 or x == 3))