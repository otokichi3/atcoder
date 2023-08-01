#!/usr/bin/env python3
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
lo, hi = 0, 10**9 + 2
while lo + 1 < hi:
    mi = (lo + hi) // 2
    na, nb = 0, 0
    for a in A:
        if a <= mi:
            na += 1
    for b in B:
        if b >= mi:
            nb += 1
    if na >= nb:
        hi = mi
    else:
        lo = mi
print(hi)
