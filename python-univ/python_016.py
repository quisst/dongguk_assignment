user_id = input("Enter id : ")
if user_id.lower() == 'admin':
    pw = input("Enter password : ")
    if pw == '1234':
        print("Welcome, admin")
    else:
        print("Wrong password")
else:
    print("You are not admin")