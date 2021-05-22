# # init파일은 모듈과 연결하는 중간체
# # 상수변수를 한번만 정의 init 사용
# # 변수나 객체도 가능
# 상대경로 --> 절대경로보다 명확성이 떨어짐 --> 간단한 경우에만 사용


from .Area import *
from .volume import *

PI = 3.14