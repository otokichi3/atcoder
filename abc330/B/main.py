#!/usr/bin/env python3
n, l, r = map(int, input().split())
a = list(map(int, input().split()))
ans = []
for i in range(n):
    if a[i] <= l:
        ans.append(l)
    elif l < a[i] < r:
        ans.append(a[i])
    else:
        ans.append(r)
print(" ".join(list(map(str, ans))))
