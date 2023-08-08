#!/usr/bin/env python3
n = int(input())
p = list(map(int, input().split()))
if len(p) == 1:
    print(0)
else:
    m = max(p[1:])
    print(max(0, m + 1 - p[0]))
