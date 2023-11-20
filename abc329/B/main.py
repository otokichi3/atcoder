#!/usr/bin/env python3
n = int(input())
a = list(map(int,input().split()))
a = sorted(a, reverse=True)
ma = max(a)
for i in range(n):
    if a[i] < ma:
        print(a[i])
        exit()