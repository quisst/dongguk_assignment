a = [90, 98, 67, 92, 76, 100, 77, 80, 95, 57, 92]
cnt = 0
for i in a:
    if i >= 90:
        cnt += 1
print("L : {}".format(a))
print("count : {}".format(cnt))
#print("avg : {}, max : {}, min : {}".format(sum(a) / len(a), max(a), min(a)))

# n = int(input("총 학생들의 수를 입력하세요 : "))
# a = []
# cnt = 0
# for i in range(n):
#     a.append(int(input("점수를 입력하세요 : ")))
# for i in a:
#     if i >= 90:
#         cnt += 1
# print("L : {}".format(a))
# print("count : {}".format(cnt))