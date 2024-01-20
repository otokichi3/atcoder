#!/usr/bin/env python3
n = int(input())
p = list(map(int, input().split()))
l = {}
head = -1
for i in range(n):
    l[p[i]] = i+1
    if p[i] == -1:
        head = i + 1
ans = []
for _ in range(n):
    ans.append(str(head))
    if head in l:
        head = l[head]
print(" ".join(ans))