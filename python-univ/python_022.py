n = int(input("enter n : "))
i = 2
is_su = True
while i < n**0.5:
    if n % i == 0:
        is_su = False
        break
    i += 1
if is_su:
    print("소수")
else:
    print("소수 아님")