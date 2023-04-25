r = input("enter : ")
i = 0
u_cnt = 0
l_cnt = 0
b_cnt = 0
n_cnt = 0
while i < len(r):
    if r[i].isupper():
        u_cnt += 1
    elif r[i].islower():
        l_cnt += 1
    elif r[i] == " ":
        b_cnt += 1
    elif r[i] in "1234567890":
        n_cnt += 1
    i += 1
print("대문자 {}, 소문자 {}, 스페이스 {}, 숫자 {}".format(u_cnt, l_cnt, b_cnt, n_cnt))