with open("data/total.txt", "r", encoding='UTF-8') as F:

    total_revenue = 0
    total_days = 0

    for line in F:
        # strip() --> 화이트 스페이스를 없애주는 속성
        # split(___) --> 데이터가 나뉘는 구역 설정
        data = line.strip().split(": ")
        revenue = int(data[1])

        total_revenue += revenue
        total_days += 1

    print(total_days)
    print(total_revenue)