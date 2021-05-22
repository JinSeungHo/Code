# print('Area 모듈 이름 : {}'.format(__name__))  # 직접실행 -->main
# from shapes import PI
# import shapes  # 상수를 사용하려면 shpes.PI 라고 사용

from mymath.shapes import PI

def circle(radius):
    return PI * radius * radius

def square(length):
    return length * length

# 스크립트에서 import시 코드가 전부 다 실행
# 직접 Area실행 시 print실행
if __name__ == "__main__":
    print(circle(2) == 12.56)
    print(circle(2) == 12.56)
    print(circle(2) == 12.56)
    print(circle(2) == 12.56)

# __name__
# __main__