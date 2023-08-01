#!/usr/bin/env python3
N = int(input())
A = list(map(lambda x: int(x) - 1, input().split()))
visited = [False] * N
path = []
v = 0  # 始点
while not visited[v]:
    visited[v] = True
    path.append(v)
    v = A[v]
i = path.index(v)
ans = path[i::]
print(len(ans))
print(*map(lambda x: x + 1, ans))