n = int(input())
for i in range(n):
    score_lst = list(map(int,input().split()))
    avg = (sum(score_lst)-score_lst[0])/score_lst[0]
    cnt = 0
    for element in score_lst:
        if element > avg:
            cnt += 1
    print('{:.3f}%'.format(round(cnt/score_lst[0]*100),3))
