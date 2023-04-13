age = int(input("나이를 입력하세요. : "))

if age < 8:
    print("8세 이상이어야 입장 가능합니다.")

else:
    height = int(input("키를 입력하세요. : "))

    if height >= 120:
        print("입장 가능합니다.")
    else:
        print("키가 120cm 이상이어야 입장 가능합니다.")