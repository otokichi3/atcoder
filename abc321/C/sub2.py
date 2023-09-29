#!/usr/bin/env python3
ans = []
for i in range(2, 1 << 10):
    x = 0
    for j in range(9, -1, -1):
        if i & (1 << j):
            x *= 10
            x += j
    ans.append(x)
ans.sort()

K = int(input())
print(ans[K - 1])
