#!/usr/bin/env python3
S = list(input())
n = len(S)
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if S[i] != ")":
            dp[i + 1][j + 1] += dp[i][j]
        if j != 0 and S[i] != "(":
            dp[i + 1][j - 1] += dp[i][j]
print(dp[n][0] % 998244353)
