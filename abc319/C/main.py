#!/usr/bin/env python3
n = 3
nn = n * n
cs = [tuple(map(int, input().split())) for _ in range(n)]
cs = [e for ci in cs for e in ci]
line = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]
num = 0
den = 0
from itertools import permutations
for ko in permutations(range(nn)):
    den += 1
    ok = True
    for l in line:
        sl = sorted(l, key=lambda i: ko[i])
        if cs[sl[0]] == cs[sl[1]] != cs[sl[2]]:
            ok = False
    num += ok

ans = num / den
print(ans)

