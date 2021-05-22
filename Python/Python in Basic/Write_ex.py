# 단어장 만들기 (Write 예제)

with open("../data/Word_list.txt", "w") as F:
    while True:
        English = input("영어 단어를 입력하세요: ")
        if English == "q":
            break
        Korean = input("뜻을 입력하세요: ")
        if Korean == "q":
            break

        F.write("{}: {}\n".format(English, Korean))




