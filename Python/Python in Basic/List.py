# 리스트 (list)

# numbers = [2, 3, 5, 7, 11, 13]
# names = ["윤수", "혜린", "태호", "영훈"]

# print(numbers)
# print(names)
#
# 인덱싱 (indexing)

# print(names[1])  # 인덱스는 "0" 부터 사용!
#
# print(numbers[1] + numbers[3])
# print("----------")
# # 리스트 슬라이싱 (list silcing)

# print(numbers[2:4])
# print("----------")

# 리스트 편집

# numbers[0] = 7

# List 함수

# numbers = []
# numbers.append(5) # 리스트에 1개의 값 추가 (추가연산)
# numbers.append(6)
# numbers.extend([3, 4, 5, 6]) # 리스트에 여러개 값 추가
# del numbers[3] # 리스트 삭제
# numbers.insert(4, 57) # 원하는 위치에 값 삽입 (삽입연산)
# print(numbers)

# 리스트 정렬
#
# numbers = [3, 65, 43, 24, 75, 22, 31]
# new_list = sorted(numbers) # 오름차순 정렬(sorted)
# new_list = sorted(numbers, reverse=True) # 내림차순 정렬
# # sorted --> 기존의 리스트를 건들지 않고 정렬된 새로운 리스트 리턴
# print(new_list)
# print("------------------------")
# # 아무것도 리턴하지 않고, 기존 리스트를 정렬
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)

