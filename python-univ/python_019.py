h = int(input("Enter time : "))
if h > 8:
    fee = 8 * 5000 + (h - 8) * 7500
else:
    fee = h * 5000
print(fee)
