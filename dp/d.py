N, W = map(int, input().split())
dp = [[0] * (W + 1) for _ in range(N + 1)]
item = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    w = item[i][0]
    v = item[i][1]
    for j in range(W + 1):
        # i番目の品物を選ぶ場合
        if j >= w:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - w] + v)
        # i番目の品物を選ばない場合
        else:
            dp[i + 1][j] = dp[i][j]

print(dp[N][W])