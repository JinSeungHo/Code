# Format 함수

print("저는 {}, {}, {}를 좋아합니다!".format("박지성", "유재석", "빌 게이츠"))

# 프로그래밍 0 1 2 3 ~ 순서 인덱스
print("저는 {1}, {0}, {2}를 좋아합니다!".format("박지성", "유재석", "빌 게이츠"))

# 실습예제
num_1 = 1
num_2 = 3

print("{0} 나누기 {1}은 {2:.2f} 입니다.".format(num_1, num_2, num_1/num_2))

# round 함수 이용
print("{0} 나누기 {1}은 {2} 입니다.".format(num_1, num_2, round(num_1 / num_2, 2)))