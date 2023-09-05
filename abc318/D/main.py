#!/usr/bin/env python3
N = int(input())
D = [[0] * N for _ in range(N)]
for i in range(N-1):
    d = list(map(int,input().split()))
    for k in range(N-1-i):
        j = i + k + 1
        D[i][j] = D[j][i] = d[k]
dp = [0 for _ in range(1<<N)]
for b in range((1<<N)-1):
    l = -1
    for i in range(N):
        if not b >> i & 1:
            l = i
            break
    for i in range(N):
        if not b >> i & 1:
            nb = b | (1<<l) | (1<<i)
            dp[nb] = max(dp[nb], dp[b] + D[l][i])
print(dp[-1])