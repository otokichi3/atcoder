#!/usr/bin/env python3
a, m, l, r = map(int, input().split())
l -= a
r -= a
ln = (l - 1) // m
rn = r // m
print(rn - ln)
