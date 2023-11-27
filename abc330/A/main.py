#!/usr/bin/env python3
n, l = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for x in a:
    if x >= l:
        ans += 1
print(ans)
