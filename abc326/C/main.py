#!/usr/bin/env python3
N, M = map(int, input().split())
A = list(map(int, input().split()))
ma = max(sorted(A))
p = [0] * (ma + 1)
for a in A:
    p[a] += 1
ans = 0
for i in A:
    if i + M < ma:
        s = sum(p[i : i + M])
        ans = max(ans, s)
print(ans)
