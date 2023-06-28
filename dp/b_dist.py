# 配るDP
N, K = map(int, input().split())
h = list(map(int, input().split()))
INF = float('inf')
dp = [INF] * N
dp[0] = 0
for i in range(0, N):
    # i+1,i+2,...,i+Kについて解く
    for j in range(1, K+1):
        if i + j < N:
            dp[i+j] = min(dp[i+j], dp[i] + abs(h[i] - h[i+j]))
print(dp[N-1])