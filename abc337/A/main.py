#!/usr/bin/env python3
n = int(input())
xsum = 0
ysum = 0
for _ in range(n):
    x, y = map(int, input().split())
    xsum += x
    ysum += y
if xsum > ysum:
    print("Takahashi")
elif xsum == ysum:
    print("Draw")
else:
    print("Aoki")