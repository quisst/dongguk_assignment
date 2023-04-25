r = input("문자열 입력 : ")
cnt = 0
i = 0
while i < len(r):
    if r[i] in 'aeiouAEIOU':
        cnt += 1
    i += 1
print(cnt)