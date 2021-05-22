# 변수 이해하기! 지정연산자 이해
name = "진승호"
x=2
x = x + 1
print(x,name)
print("----------")

def square(x):
    return x*x

print("함수 호출 전")
print(square(3) + square(4))
print("함수 호출 후")

