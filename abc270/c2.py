from collections import deque

N, X, Y = map(int, input().split())
N += 1
G = [[] for _ in range(N)]
for _ in range(N - 2):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

Q = deque()
Q.append(X)
dist = [-1] * N
dist[X] = 0
prev = [-1] * N 


def bfs():
    while Q:
        v = Q.popleft()
        for u in G[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                Q.append(u)
                prev[u] = v


bfs()

cur = Y
path = []
while cur != -1:
    path.append(cur)
    cur = prev[cur]

ans = []

for x in reversed(path):
    ans.append(str(x))

print(" ".join(ans))
