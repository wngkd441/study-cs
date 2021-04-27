def solve(n):
    cnt = 0
    for i in range(1,n+1):
        num_lst = list(map(int, str(i)))
        if i >= 100:
            if num_lst[0] - num_lst[1] == num_lst[1] - num_lst[2]:
                cnt += 1
            else:
                continue
        else:
            cnt += 1
    print(cnt)
    return 0
solve(int(input()))
