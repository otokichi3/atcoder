#!/usr/bin/env python3
N = int(input())
P = list(map(int, input().split()))
p1 = P[0]
if len(P) == 1:
    print(0)
    exit()
saikyo = max(P[1:])

if p1 > saikyo:
    print(0)
elif p1 == saikyo:
    print(1)
else:
    print(saikyo - p1 + 1)