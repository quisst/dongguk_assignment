r = input("Enter word : ")
i = 0
cnt = 0
while i < len(r):
    if r[i] in 'aeiouAEIOU':
        print("{} 번째 {}".format(i, r[i]))
        cnt += 1
    i += 1
print("*"*15)
print("총 모음의 개수 : {}".format(cnt))