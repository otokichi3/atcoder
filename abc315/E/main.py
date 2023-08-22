#!/usr/bin/env python3
# DFS帰りがけ解法
import sys

sys.setrecursionlimit(10**6)
n = int(input())
g = [[] for _ in range(n)]
for i in range(n):
    cp = list(map(int, input().split()))
    for v in cp[1:]:
        g[i].append(v - 1)
seen = [False] * n
ans = []


def dfs(v):
    seen[v] = True
    for nv in g[v]:
        if not seen[nv]:
            dfs(nv)
    ans.append(v + 1)


dfs(0)
ans.pop(-1)
print(*ans)
