N, W = map(int, input().split())
# [重さ, 価値]
dp = [[0, 0] * N for _ in range(N)]
print('dp:')
print(dp)
item = [list(map(int, input().split())) for _ in range(N)]
print('item:')
print(item)
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        # 重さが足してW以下、かつ価値が大きくなるように
        if dp[i][j] + item[j] <= W:
            dp[i+1][j] = dp[i][j] + item[j]