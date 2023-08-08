#!/usr/bin/env python3
n, m = map(int, input().split())
s = [1] * n
for _ in range(m):
    a,b = map(int, input().split())
    s[b-1] = False
if sum(s) > 1:
    print(-1)
else:
    print(s.index(1)+1)