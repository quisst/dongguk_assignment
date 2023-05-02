string = input("Enter string : ")
v_cnt = 0
c_cnt = 0
for i in string:
    if i in 'aeiouAEIOU':
        v_cnt += 1
    else:
        c_cnt += 1
print("number of vowels : {}".format(v_cnt))
print("number of consonants : {}".format(c_cnt))