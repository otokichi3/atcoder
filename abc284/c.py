from collections import deque

N, M = map(int, input().split())
if M == 0:
    print(N)
    exit()

visited = [False] * N
G = [[] * N for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

Q = deque()
ans = 0


def bfs():
    while Q:
        v = Q.popleft()
        u = G[v]
        for x in u:
            if not visited[x]:
                visited[x] = True
                Q.append(x)


for i in range(N):
    if not visited[i]:
        ans += 1
        Q.append(i)
        bfs()

print(ans)
