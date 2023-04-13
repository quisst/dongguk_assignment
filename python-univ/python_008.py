a = int(input())
print("오만원 {}".format(a // 50000))
a = a % 50000
print("만원 {}".format(a // 10000))
a = a % 10000
print("천원 {}".format(a // 1000))
