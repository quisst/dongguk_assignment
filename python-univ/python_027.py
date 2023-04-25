import random

while True:
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)
    c = random.randint(1, 1000)
    d = random.randint(1, 1000)
    e = random.randint(1, 1000)
    f = random.randint(1, 1000)
    g = random.randint(1, 1000)
    h = random.randint(1, 1000)
    i = random.randint(1, 1000)
    j = random.randint(1, 1000)
    print(
        "{}, {}, {}, {}, {}, {}, {}, {}, {}, {},".format(a, b, c, d, f, e, g, h, i, j)
    )
    print("*" * 15)
    one_cnt = 0
    ten_cnt = 0
    hun_cnt = 0

    if a // 100 >= 1:
        hun_cnt += 1
    elif a // 10 >= 1:
        ten_cnt += 1
    else:
        one_cnt += 1

    if b // 100 >= 1:
        hun_cnt += 1
    elif b // 10 >= 1:
        ten_cnt += 1
    else:
        one_cnt += 1

    if c // 100 >= 1:
        hun_cnt += 1
    elif c // 10 >= 1:
        ten_cnt += 1
    else:
        one_cnt += 1

    if d // 100 >= 1:
        hun_cnt += 1
    elif d // 10 >= 1:
        ten_cnt += 1
    else:
        one_cnt += 1

    if e // 100 >= 1:
        hun_cnt += 1
    elif e // 10 >= 1:
        ten_cnt += 1
    else:
        one_cnt += 1

    if f // 100 >= 1:
        hun_cnt += 1
    elif f // 10 >= 1:
        ten_cnt += 1
    else:
        one_cnt += 1

    if g // 100 >= 1:
        hun_cnt += 1
    elif g // 10 >= 1:
        ten_cnt += 1
    else:
        one_cnt += 1

    if h // 100 >= 1:
        hun_cnt += 1
    elif h // 10 >= 1:
        ten_cnt += 1
    else:
        one_cnt += 1

    if i // 100 >= 1:
        hun_cnt += 1
    elif i // 10 >= 1:
        ten_cnt += 1
    else:
        one_cnt += 1

    if j // 100 >= 1:
        hun_cnt += 1
    elif j // 10 >= 1:
        ten_cnt += 1
    else:
        one_cnt += 1

    print("1자리 숫자 : {}".format(one_cnt))
    print("2자리 숫자 : {}".format(ten_cnt))
    print("3자리 숫자 : {}".format(hun_cnt))

    re = input("다시 하시겠습니까? (Y/N) : ")
    if re in "Nn":
        print(" *** 수고하셨습니다 *** ")
        break
    elif re in "Yy":
        print(" *** 다시 하겠슴 *** ")
