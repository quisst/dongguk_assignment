import random

n = int(input("랜덤 갯수를 입력하시오 : "))

arr = []
for i in range(n):
    arr.append(random.randint(1, 101))

print("랜덤으로 받은 수의 리스트")
print(arr)
print("*"*15)

arr_b, arr_s = [], []
avg = sum(arr) / len(arr)

for i in arr:
    if i > avg:
        arr_b.append(i)
    else:
        arr_s.append(i)

print("평균보다 큰 수 {} - 그 수는 {}이다.".format(len(arr_b), arr_b))
print("평균보다 작은 수 {} - 그 수는 {}이다.".format(len(arr_s), arr_s))