N, INF = int(input()), 10**18
a = list(map(int, input().split()))
dp = [-INF] * N
dp[0] = 0
dp[1] = abs(a[1] - a[0])
# dp[i]は、i-1番目の柱からとi-2番目の柱からの移動コストのうち、小さい方を格納する
for i in range(2, N):
    # i-1番目の柱から移動した場合のコスト
    cost1 = dp[i - 1] + abs(a[i] - a[i - 1])
    # i-2番目の柱から移動した場合のコスト
    cost2 = dp[i - 2] + abs(a[i] - a[i - 2])
    dp[i] = min(cost1, cost2)
print(dp[N - 1])