#!/usr/bin/env python3
N = int(input())
W = []
X = []
for _ in range(N):
    w, x = map(int, input().split())
    W.append(w)
    X.append(x)

ans = 0
for i in range(24):
    total = 0
    for j in range(N):
        t = (X[j] + i) % 24
        if 9 <= t <= 17:
            total += W[j]
    ans = max(ans, total)
print(ans)
