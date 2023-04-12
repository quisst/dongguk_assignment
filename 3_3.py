a = int(input("첫번째 수를 입력하세요 : "))
cal = input("계산할 연산자를 입력하세요 : ")
b = int(input("두번째 수를 입력하세요 : "))

if cal == '+':
    print("{} + {} = {} 입니다.".format(a, b, a + b))
elif cal == '-':
    print("{} - {} = {} 입니다.".format(a, b, a - b))
elif cal == '*':
    print("{} * {} = {} 입니다.".format(a, b, a * b))
elif cal == '/':
    print("{} / {} = {} 입니다.".format(a, b, a / b))
else:
    print("알 수 없는 연산자 입니다.")