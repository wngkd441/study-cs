N = int(input()) # 일하는 날
day_lst = []
pay_lst = []
dp = []
for i in range(N):
    day, pay = map(int, input().split())
    day_lst.append(day)
    pay_lst.append(pay)
    dp.append(dp)
dp.append(0)

for i in range(N-1, -1, -1):
    if day_lst[i] + i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], pay_lst[i] + dp[i + day_lst[i]])
print(dp[0])
