from collections import deque

N, X, Y = map(int, input().split())
X -= 1
Y -= 1
G = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

Q = deque()
Q.append(X)
dist = [-1] * N
dist[X] = 0


def bfs():
    while Q:
        v = Q.popleft()
        for u in G[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                Q.append(u)


# BFSの結果から最短経路を復元する
# 素朴なやり方
# ゴールから1ずつ遠ざかっていく経路をメモする
def get_path():
    path = [Y + 1]
    while Q:
        v = Q.popleft()
        for u in G[v]:
            if dist[u] == 0:
                path.append(u + 1)
                return path
            if dist[v] - dist[u] == 1:
                path.append(u + 1)
                Q.append(u)


bfs()

Q = deque()
Q.append(Y)
res = get_path()
ans = []
for x in reversed(res):
    ans.append(x)
ans = list(map(str, ans))
print(" ".join(ans))
