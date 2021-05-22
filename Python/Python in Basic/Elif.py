# Elif문

temperature = 19

if temperature <= 10:
    print("자켓을 입는다.")
    print("---------")
else:
    if temperature <= 15:
        print("긴 팔을 입는다.")
        print("---------")
    else:
        print("반팔을 입는다.")
        print("---------")

if temperature <= 10:
    print("자켓을 입는다.")
    print("---------")
elif temperature <= 15:
    print("긴 팔을 입는다.")
    print("---------")
else:
    print("반팔을 입는다.")
    print("---------")