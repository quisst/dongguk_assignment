s = int(input("시작값 입력 : "))
e = int(input("끝값 입력 : "))
p = int(input("증가값 입력 : "))
print("{}에서 {}까지 {}씩 증가함 값의 합 : {}".format(s, e, p, sum(range(s, e+1, p))))