# Scope(범위) --> 전역변수(글로벌변수) //지역변수 (로컬변수)
x = 3
def my_function():
    x = 5
    print(x)

my_function()
print(x)  # --> x는 함수 내에서 정의 (로컬변수)
