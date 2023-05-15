parking = ["", "", "", "", ""]
top = 0
while True:
    ans = input("<1> 주차하기 <2> 자동차 빼기 <3> 끝 : ")
    if ans == '1':
        num = input("자동차 번호를 4자리를 입력하세요 : ")
        parking[top] = num
        top += 1
        print("{} 자동차 들어감. 주차장 상태 ==> ".format(num), end="")
        print(parking[:top])
    elif ans == '2':
        print("{} 자동차 나감. 주차장 상태 ==> ".format(parking[top - 1]), end="")
        parking[top - 1] = ""
        top -= 1
        print(parking[:top])
    else:
        break