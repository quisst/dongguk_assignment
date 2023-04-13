a = int(input("원하는 초(sec)를 입력하시오.>> "))
print("시간 => {0}".format(a // 3060))
a = a % 3600
print("분 => {0}".format(a // 60))
print("초 => {0}".format(a % 60))