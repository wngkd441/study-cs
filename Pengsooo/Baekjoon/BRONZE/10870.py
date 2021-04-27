n = int(input()) # index

dp = [0,1]
for i in range(2, 21):
    dp.append(dp[i-2]+dp[i-1])

print(dp[n])