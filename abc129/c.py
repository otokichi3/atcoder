N, M = map(int, input().split())
ng = [False] * (N + 2)
dp = [0] * (N + 2)
# 1 0が与えられたとき0を返してしまうため1
dp[0] = 1
# 壊れた階段の配列aを配列dpと同じ長さにする
# ->ループで扱いやすくなる
for _ in range(M):
    a = int(input())
    ng[a] = True

# DP本体
# - 次に踏む階段が壊れていなければ、その段数に今までの組み合わせの数を加算する
# - 壊れている段は初期値0のままとなる
# - 2段連続で壊れている箇所があれば、その箇所以降はすべて0+=0となり、答えであるdp[N]は0となる
for i in range(N):
    # 1段先
    if not ng[i + 1]:
        dp[i + 1] += dp[i]
    # 2段先
    if not ng[i + 2]:
        dp[i + 2] += dp[i]
print(dp[N] % 1000000007)
