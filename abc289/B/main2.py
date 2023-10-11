#!/usr/bin/env python3
N, M = map(int, input().split())
if M == 0:
    print(*[i for i in range(1, N + 1)])
    exit()
a = list(map(int, input().split()))
l = []
L = 1
while L <= N:
    R = L
    while R in a:
        R += 1
    l.append([i for i in range(L, R + 1)])
    L = R + 1
ans = []
for x in l:
    for i in sorted(x, reverse=True):
        ans.append(i)
print(*ans)
