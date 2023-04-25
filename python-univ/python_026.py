while True:
    r = input("Enter id : ")
    if len(r) < 8:
        print("아이디는 8자 미만입니다.")
        print("-" * 30)
    else:
        if r[0] not in "abcdefghijklmnopqrstuvwxyz":
            print("첫 글자가 영어 소문자 아님")
            print("-" * 30)
        else:
            if r[-1] not in "1234567890" or r[-2] not in "1234567890":
                print("두글자가 숫자가 아님")
                print("-" * 30)
            else:
                print("{} -> 적합한 아이디 입니다.".format(r))
                break
