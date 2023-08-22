#!/usr/bin/env python3
# BFS+トポロジカルソート解法
from collections import deque

n = int(input())
g = [[] for _ in range(n)]
indegree = [0] * n
for i in range(n):
    cp = list(map(int, input().split()))
    for v in cp[1:]:
        g[i].append(v - 1)
        indegree[v - 1] += 1


# bfs
dque = deque()
dque.append(0)
seen = [False] * n
while dque:
    v = dque.popleft()
    seen[v] = True
    for nv in g[v]:
        if not seen[nv]:
            dque.append(nv)

# topological sort
tque = deque()
for i in range(len(indegree)):
    if indegree[i] == 0:
        tque.append(i)
path = []
while tque:
    v = tque.popleft()
    path.append(v)
    for nv in g[v]:
        indegree[nv] -= 1
        if indegree[nv] == 0:
            tque.append(nv)

# get v in path if v are seen
ans = []
for i in path:
    if seen[i]:
        ans.append(i + 1)

ans.pop(0)
print(*ans[::-1])
