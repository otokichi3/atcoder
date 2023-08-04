#!/usr/bin/env python3
s = input()
n = len(s)
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if s[i] == "(" or s[i] == "?":
            dp[i + 1][j + 1] += dp[i][j]
        if s[i] == ")" or s[i] == "?":
            dp[i + 1][j - 1] += dp[i][j]
print(dp[n][0] % 998244353)
