num_lst = [int(input()) for i in range(3)]
ans = str(num_lst[0]*num_lst[1]*num_lst[2])
for i in range(10):
    print(ans.count(str(i)))
