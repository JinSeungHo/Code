# Paramiter 와 Return의 차이점
# print 와 return의 차이점

# def get_square(x):
#     print(x*x)

# print(get_square(2)+get_square(3))

# print는 값을 보여주는 함수이기는 하지만
# 연산을 하기 위해서는 Return을 사용하야한다.

def get_square(x):
    return x*x
def print_square(x):
    print(x*x)

print(get_square(2)+get_square(4))
print(print_square(3))  #-->print는 종료 할수가 없어서 none출력
print(get_square(4))
print("---------")

# return문 // 역활 값을 돌려주기 // 즉시 종료하기

def hello(x):
    print("함수 호출!")
    return x * x
    print("함수 호출 후") # dead Code(의미없는 코드)

print(hello(2))
print("----------")





