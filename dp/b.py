N, K = map(int, input().split())
h = list(map(int, input().split()))
dp = [0, abs(h[0] - h[1])]
for i in range(2, N):
    d = float('inf')
    for j in range(1, K+1):
        if i - j >= 0:
            d = min(d, dp[i - j] + abs(h[i] - h[i - j]))
    dp.append(d)
print(dp[N - 1])