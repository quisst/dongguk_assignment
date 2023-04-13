def turn_C_to_F(a):
    return 9 * a / 5 + 32

x = int(input("섭씨온도 : "))
print("화씨온도 :", turn_C_to_F(x))