def hello():
    print("나의 이력은:")
    name = input("이름을 입력하시오 : ")
    age = input("나이를 입력하시오 : ")
    print("My name is", name, '나이는' + age + "입니다.")

print("Here is Main")

print("")
print("Before function call")
print("**********")
hello()
print("**********")
print("After funcion call")