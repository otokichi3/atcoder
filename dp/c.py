N = int(input())
dp = [[0, 0, 0] for _ in range(N + 1)]
for i in range(N):
    a, b, c = map(int, input().split())
    dp[i + 1][0] = max(dp[i][1], dp[i][2]) + a
    dp[i + 1][1] = max(dp[i][0], dp[i][2]) + b
    dp[i + 1][2] = max(dp[i][0], dp[i][1]) + c
print(max(dp[N]))
