#!/usr/bin/env python3
N, M = map(int, input().split())
G = [[] * N for _ in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1

    G[a].append([b, c])
    G[b].append([a, c])

ans = 0
seen = [False] * N
sum = 0


def dfs(v, c):
    global sum
    global ans
    seen[v] = True
    for nv in G[v]:
        next = nv[0]
        cost = nv[1]
        if not seen[next]:
            sum += cost
            ans = max(ans, sum)
            dfs(next, cost)
    seen[v] = False
    sum -= c


for i in range(N):
    dfs(i, 0)
    ans = max(ans, sum)
    sum = 0

print(ans)
