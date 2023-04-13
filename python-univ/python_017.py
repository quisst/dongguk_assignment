first = input("Enter first name : ")
last = input("Enter last name : ")
user_id = first[:2] + last[-2:]
user_id = user_id.lower()
print(user_id)

print("Make a password as follows")
print(" - Must be at least 6 letters")
print(" - Alphabet and numbers only")

pw = input("Enter password : ")
if pw.isalnum() == True and len(pw) >= 9:
    print("Good password")
else:
    print("Wrong password")