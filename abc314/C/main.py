#!/usr/bin/env python3
n, m = map(int, input().split())
s = input()
c = list(map(int, input().split()))
lst = [[] for _ in range(m + 1)]
for i in range(n):
    lst[c[i]].append(i)
ans = [None] * n
for i in lst:
    l = len(i)
    for j in range(l):
        ans[i[j]] = s[i[(j+l-1)%l]]
print("".join(ans))