#!/usr/bin/env python3
from collections import deque

n, m = map(int, input().split())
g = [[] * m for _ in range(n)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    v1 -= 1
    v2 -= 1
    g[v1].append(v2)
    g[v2].append(v1)

# 条件1:辺の数はN-1本
if m != n - 1:
    print("No")
    exit()

# 条件2:すべての頂点の次数が2以下
for i in range(n):
    if len(g[i]) > 2:
        print("No")
        exit()

reach = [False] * n
que = deque()
reach[0] = True
que.append(0)

while que:
    u = que.popleft()
    for v in g[u]:
        if not reach[v]:
            reach[v] = True
            que.append(v)

# 条件3:連結である
for i in range(n):
    if not reach[i]:
        print("No")
        exit()

print("Yes")
