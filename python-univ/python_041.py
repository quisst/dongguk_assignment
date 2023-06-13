while True:
    s_list = ['good', 'tiger', 'cat' , 'dog', 'cat', 'good', 'Python', 'cat', 'information', 'tiger']
    r = input("문자 입력 : ")
    if r == 'end':
        break
    if r in s_list:
        pos = []
        while r in s_list:
            a = s_list.index(r)
            pos.append(a)
            s_list[a] = ' '
        print("{}의 문자 위치는 {} 입니다.".format(r, pos))
    else:
        print("{}의 문자는 없습니다.".format(r))