# Write

with open('../data/new_file.txt', 'a', encoding='UTF-8') as F:
    F.write("Hello, wolrd!\n")
    F.write("안녕!!\n")
    F.write("니하오!\n")

# 'w' --> 덮어 쓰기(write)
# 'a' --> 추가 하기(append)