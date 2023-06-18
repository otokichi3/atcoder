#
# 3日後に何も見ずに解けるか？が大事
# hint: 有毒・無毒の二つの状態を管理する(2つの状態)
#
N = int(input())
# 十分に大きい定数INFを定義
INF = 10**18
# 長さNのdpリストを[-INF, -INF]で初期化する
dp = [[-INF, -INF] for _ in range(N + 1)]
# 食べる前は美味しさ0、毒なし
dp[0][0] = 0

# このDPの計算量は状態数O(N)*遷移数O(1)のためO(N)
# Nは高々3*10^5のため制限時間内に解ける
for i in range(N):
    X, Y = map(int, input().split())
    # 下げてもらった場合は次の状態=今の状態
    dp[i + 1][0] = dp[i][0]
    dp[i + 1][1] = dp[i][1]
    # 解毒剤
    if X == 0:
        dp[i + 1][0] = max(dp[i + 1][0], dp[i][0] + Y)
        dp[i + 1][0] = max(dp[i + 1][0], dp[i][1] + Y)
    # 毒入り
    else:
        dp[i + 1][1] = max(dp[i + 1][1], dp[i][0] + Y)
print(max(dp[N]))
