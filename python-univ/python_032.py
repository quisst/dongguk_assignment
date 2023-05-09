L = [1, 2, 3, 2, 1]
# if L == L[::-1]:
#     print("same")
# else:
#     print("not same")

is_same = True
for i in range(len(L) // 2 + 1):
    if L[i] != L[-i-1]:
        is_same = False
        break
if is_same:
    print("same")
else:
    print("not same")