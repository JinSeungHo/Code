# Aliasing (별명, 가명)

# x = 5
# y = x
# y = 3
# print(x)
# print(y)
# print("--------")

# x = [2, 3, 5, 7, 11]
# y = x          # y는 x의 별칭(Aliasing)
# y[2] = 4
# print(x)
# print(y)
# print("---------")

x = [2, 3, 5, 7, 11]
y = list(x)          # y에 리스트 x 복사
y[2] = 4
print(x)
print(y)
print("---------")