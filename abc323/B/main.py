#!/usr/bin/env python3
from functools import cmp_to_key


def cmp(a, b):
    w1 = a[1]
    w2 = b[1]
    if w1 == w2:
        return 1 if a[0] < b[0] else -1
    elif w1 > w2:
        return 1
    else:
        return -1


N = int(input())
P = {k + 1: 0 for k in range(N)}
S = [input() for _ in range(N)]
for i in range(N):
    for s in S[i]:
        if s == "o":
            P[i + 1] += 1
sorted = sorted(P.items(), key=cmp_to_key(cmp), reverse=True)
ans = []
for s in sorted:
    ans.append(s[0])
print(*ans)
