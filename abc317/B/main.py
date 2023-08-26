#!/usr/bin/env python3
n = int(input())
a = list(map(int, input().split()))
a.sort()
for i in range(n):
    if i == 0:
        continue
    if a[i] - a[i - 1] != 1:
        print(a[i] - 1)
        exit()
