from collections import deque

N1, N2, M = map(int, input().split())
N = N1 + N2
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)


# sは探索の開始地点
def bfs(s):
    dist = [-1] * len(G)
    dist[s] = 0
    q = deque()
    q.append(s)

    while q:
        v = q.popleft()
        for nv in G[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                q.append(nv)
    return max(dist)


print(bfs(0) + bfs(N - 1) + 1)
