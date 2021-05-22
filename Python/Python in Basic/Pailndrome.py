# 인덱스를 대칭 거꾸로 정렬

numbers = [2, 3, 5, 7, 11, 13, 17, 19]

for left in range(len(numbers) // 2):
    right = len(numbers) - left -1

    numbers[right], numbers[left] = numbers[left], numbers[right]

print("뒤집어진 리스트 : " + str(numbers))
