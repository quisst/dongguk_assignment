s = input("Enter one string : ")
c = input("Enter one character : ")
cnt = 0
for i in s:
    if s == c:
        cnt += 1
print("count : {}".format(cnt))
# s = input("Enter one string : ")
# c = input("Enter one character : ")
# cnt = 0
# pos = []
# for i in range(len(s)):
#     if s[i] == c:
#         cnt += 1
#         pos.append(i)
# print("count : {}".format(cnt))
# print("{}번째에 있음".format(pos))