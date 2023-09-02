#!/usr/bin/env python3
n, m, p = map(int, input().split())
ans = 0
for i in range(n):
    if m + (p * i) <= n:
        ans += 1
print(ans)
