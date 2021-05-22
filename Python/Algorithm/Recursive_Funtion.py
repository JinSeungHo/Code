# 재귀함수(recursive_Funtion)

def countdown(n):
    if n > 0:
        print(n)
        countdown(n - 1)

def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n
# n번째 피보나치 수를 리턴
def fib(n):
    # if n == 0:
    #     return 0
    # return fib(n - 1) + n
    if n < 3:
        return 1

    # recursive case
    return fib(n - 1) + fib(n - 2)
def sum_digits(n):
    # base case
    if n < 10:
        return n

    # recursive case
    return n % 10 + sum_digits(n // 10)

countdown(4)
print("----------")
print(factorial(4))
print("----------")
# 테스트: fib(1)부터 fib(10)까지 출력
for i in range(1, 11):
    print(fib(i))

print("----------")
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))