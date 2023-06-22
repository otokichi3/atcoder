N = int(input())
INF = 10 ** 18
dp = [[-INF, -INF] for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    X, Y = map(int, input().split())
    dp[i+1][0] = dp[i][0]
    dp[i+1][1] = dp[i][1]
    if X == 0:
        dp[i+1][0] = max(dp[i+1][0], dp[i][0] + Y)
        dp[i+1][0] = max(dp[i+1][0], dp[i][1] + Y)
    else:
        dp[i+1][1] = max(dp[i+1][1], dp[i][0] + Y)
print(max(dp[N]))