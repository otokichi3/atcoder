#!/usr/bin/env python3
n, m = map(int, input().split())
A = list(map(int, input().split()))
P = []
l = 1
while l <= n:
    r = l
    while r in A:
        r += 1
    for i in range(r, l - 1, -1):
        P.append(i)
    l = r + 1
print(*P)
