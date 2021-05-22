with open("../data/Impormation.txt", "w", encoding="UTF-8") as File:

    while True:
        question = input("문제를 입력하세요 : ")
        if question == "q" or question == "ㅂ":
            break
        answer = input("답을 입력하세요' : ")
        if answer == "q" or answer == "ㅂ":
            break
        File.write("{} : {}\n".format(question, answer))