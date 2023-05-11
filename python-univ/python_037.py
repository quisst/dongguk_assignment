num_list = [35, 140, 85, 12, 8, 172, 32, 1547, 1, 450]
o_arr, t_arr, h_arr, th_arr = [], [], [], []
for i in num_list:
    if i // 1000 != 0:
        th_arr.append(i)
    elif i // 100 != 0:
        h_arr.append(i)
    elif i // 10 != 0:
        t_arr.append(i)
    else:
        o_arr.append(i)
print(f"한자리수 : {o_arr}")
print(f"두자리수 : {t_arr}")
print(f"세자리수 : {h_arr}")
print(f"네자리수 : {th_arr}")