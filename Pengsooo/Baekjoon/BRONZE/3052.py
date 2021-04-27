least_lst = []
cnt = 0
for i in range(10):
    a=int(input())%42
    if a not in least_lst:
        cnt += 1
        least_lst.append(a)
print(cnt)
