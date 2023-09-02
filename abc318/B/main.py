#!/usr/bin/env python3
n = int(input())
base = [[False] * 100 for _ in range(100)]
for i in range(n):
    s = list(map(int, input().split()))
    x1, x2 = s[0], s[1]
    y1, y2 = s[2], s[3]
    for j in range(x1, x2):
        for k in range(y1, y2):
            base[j][k] = True

ans = 0
for i in range(100):
    for j in range(100):
        if base[i][j]:
            ans += 1
print(ans)
