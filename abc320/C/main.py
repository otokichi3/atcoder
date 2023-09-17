#!/usr/bin/env python3
m = int(input())
s1 = list(input())
s2 = list(input())
s3 = list(input())


def win(s1, s2, s3):
    d = {str(i): -1 for i in range(10)}
    for i in range(m):
        if d[s1[i]] == -1:
            d[s1[i]] = i
    s = sorted(d.items(), key=lambda x:x[1])
    return s[0]


ans = 10**8
from itertools import permutations
for p in permutations((s1, s2, s3), 3):
    res = win(p[0], p[1], p[2])
    ans = min(ans, res[1])
print(ans)