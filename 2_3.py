def print_calc(a, b):
    print("두 수의 연산을 보여줍니다.")
    result = a + b
    print(a, "+", b, "=", result)
    result = a - b
    print(a, "-", b, "=", result)
    result = a * b
    print(a, "*", b, "=", result)
    result = a / b
    print(a, "/", b, "=", result)

x = int(input("Enter X (첫번째 숫자 입력) : "))
y = int(input("Enter Y (두번째 숫자 입력) : "))
print("**********")
print_calc(x, y)