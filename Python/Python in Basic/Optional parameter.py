# optional parameter (옵셔널파라미터)
# 함수를 호출할 떄 기본값을 설정--> 필수로 넘겨줄 필요X

def myself(name, age, nationality = "한국"): # 옵셔널 파라미터 "한국"
    print("내 이름은 {}".format(name))
    print("나이는 {}살".format(age))
    print("국적은 {}".format(nationality))

myself("코드잇", 1, "미국") # 임의로 변경 "미국" --> 옵셔널 파라미터를 제공
myself("코드잇", 26)

