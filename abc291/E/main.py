#!/usr/bin/env python3
n, m = map(int, input().split())
g = [[] for _ in range(n)]
ind = [0] * n
for _ in range(m):
    x, y = map(lambda x: int(x) - 1, input().split())
    g[x].append(y)
    ind[y] += 1

l = []
ans = [[] for _ in range(n)]
cnt = 0
for i in range(n):
    if ind[i] == 0:
        l.append(i)
while l:
    if len(l) != 1:
        print("No")
        exit()
    v = l.pop(0)
    cnt += 1
    ans[v] = cnt
    for nv in g[v]:
        ind[nv] -= 1
        if ind[nv] == 0:
            l.append(nv)
print("Yes")
print(*ans)
