#!/usr/bin/env python3
m = int(input())
d = list(map(int, input().split()))
dsum = sum(d)
mi = dsum // 2 + 1
mi_month = 0
for i in range(m):
    mi -= d[i]
    if mi <= 0:
        mi_month = i
        break
print(mi_month + 1, d[mi_month] - abs(mi))
