#!/usr/bin/env python3
n=int(input())
d = {}
for i in range(n):
    d[i] = [int(input()), list(map(int, input().split()))]
x = int(input())
ans = []
min = 38
cnt = 0
for v in d.values():
    cnt += 1
    if x in v[1]:
        if min > v[0]:
           ans = []
           min = v[0] 
           ans.append(cnt)
        elif min == v[0]:
           ans.append(cnt)
print(len(ans))
print(*ans)