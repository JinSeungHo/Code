# 예제
# 자릿수 더하기
#
# def sum_digit(num):
#     total = 0
#     str_num = str(num)
#
#     for i in range(len(str_num)):
#         digit = str_num[i]
#         total += int(digit)
#     return total
#
# print(sum_digit(12))

# 주민등록번호 뒷 네자리 암호화

# def mask_security_number(security_number):
#     # 코드를 입력하세요.
#     new_security_number = list(security_number)
#
#     for i in range(len(new_security_number)-4, len(security_number)):
#         new_security_number[i] = "*"
#
#     total_str = ""
#     for i in range(len(new_security_number)):
#         total_str += new_security_number[i]
#     return total_str

def mask_security_number(security_number):
    return security_number[:-4] + "****"


# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("880720-1234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("761214-2357111"))