a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

max_v = a
if max_v < b:
    max_v = b
if max_v < c:
    max_v = c

print("Max value : {}".format(max_v))