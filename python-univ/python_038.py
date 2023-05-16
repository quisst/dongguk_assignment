arr = []
arr_len = []
for i in range(5):
    arr.append(input("{} Enter word : ".format(i+1)))
for i in arr:
    arr_len.append(len(i))
max_pos = max(arr_len)
print("longest word ; {}".format(arr[max_pos]))
print("length : {}".format(max(arr_len)))