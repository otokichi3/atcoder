N = int(input())
h = list(map(int, input().split()))
dp = [0, abs(h[0] - h[1])]
for i in range(2, N):
    j1 = dp[i - 1] + abs(h[i] - h[i - 1])
    j2 = dp[i - 2] + abs(h[i] - h[i - 2])
    dp.append(min(j1, j2))
print(dp[N - 1])
