# https://drken1215.hatenablog.com/entry/2020/12/21/153600
# 上記のPython焼き直し版
N = int(input())
p = list(map(int, input().split()))
W = 10000
dp = [[False] * (W + 1) for _ in range(N + 1)]
dp[0][0] = True

for i in range(N):
    for j in range(W):
        if not dp[i][j]:
            continue
        dp[i + 1][j] = True
        if j + p[i] <= W:
            dp[i + 1][j + p[i]] = True
ans = 0
for i in range(W):
    if dp[N][i]:
        ans += 1
print(ans)
