#!/usr/bin/env python3
n, m = map(int, input().split())
s = [0] * n
for _ in range(m):
    a, b = map(int,input().split())
    s[b-1] += 1
print(s)
if s.count(0) == 1:
    print(s.index(0)+1)
else:
    print(-1)
    