# Strip --> 화이트 스페이스를 없애줌 (\t,\n)

# print("           abc    def    ".strip())
# print("\t      abc    def \n\n\n\n\n\n".strip())
with open('../data/MonryDaTa.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        print(line.strip())

# split --> 리스트에 저장되는 값은 문자열 --> 형변환 작업을 해야함

my_srting = "1. 2. 3. 4. 5. 6"
print(my_srting.split(". "))

full_name = "kim, Yuna"
print(full_name.split(", "))

numbers = "\t   \n 3 4 6      2 5  \n\n".split()
print(numbers[0] + numbers[1]) # Split 문자열 저장
print(int(numbers[0]) + int(numbers[1])) # 각각 형 변환
