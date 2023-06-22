N, M = map(int, input().split())
dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 1
ng = [False] * (N + 1)
for m in range(M):
    a = int(input())
    ng[a] = True
for i in range(2, N + 1):
    if not ng[i]:
        dp[i] = dp[i - 1] + dp[i - 2]
print(dp[N] % 1000000007)
