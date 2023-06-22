N = int(input())
# dp[i][0]: deliciousness if not poisoned
# dp[i][1]: deliciousness if poisoned
dp = [[0, 0] for _ in range(N)]
for i in range(N):
    x, y = map(int, input().split())
    if i == 0:
        if x == 0:  # 解毒剤
            dp[0][0] = max(0, y)
        else:  # 毒入り
            dp[0][1] = max(0, y)
    else:
        if x == 0:  # 解毒剤
            dp[i][0] += max(dp[i - 1][0], dp[i - 1][0] + y, dp[i - 1][1] + y)
            dp[i][1] = dp[i - 1][1]
        else:  # 毒入り
            dp[i][0] = dp[i - 1][0]
            dp[i][1] += max(dp[i - 1][1], dp[i - 1][0] + y)
print(max(dp[N - 1][0], dp[N - 1][1]))
