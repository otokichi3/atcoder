# https://atcoder.jp/contests/dp/tasks/dp_d
N, W = map(int, input().split())
dp = [[0] * (W + 1) for _ in range(N + 1)]
for i in range(N):
    w, v = map(int, input().split())
    for j in range(W + 1):
        # 選ぶ場合
        if j >= w:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - w] + v)
        # 選ばない場合
        else:
            dp[i + 1][j] = dp[i][j]
print(dp[N][W])
