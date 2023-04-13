user_id = input()
user_id = user_id.lower()
if user_id == "admin":
    print("Hi, admin! Please check log files.")
else:
    print("Welcome! {0}".format(user_id))
