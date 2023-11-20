#!/usr/bin/env python3
n, m = map(int, input().split())
a = list(map(int, input().split()))

from collections import defaultdict
d = defaultdict(int)
ans = 0
ma = 0
for i in range(m):
    d[a[i]] += 1
    if ma < d[a[i]]:
        ans = a[i]
        ma = d[a[i]]
    if ma == d[a[i]] and ans > a[i]:
        ans = a[i]
            
    print(ans)