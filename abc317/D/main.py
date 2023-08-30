#!/usr/bin/env python3
n = int(input())
d = []
for i in range(n):
    d.append(list(map(int, input().split())))
d = sorted(d, key=lambda x: x[1] - x[0] // 2)
print(d)
