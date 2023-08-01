from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
sy -= 1
sx -= 1
gy -= 1
gx -= 1
dist = [[-1] * C for _ in range(R)]
dist[sy][sx] = 0
G = []
for _ in range(R):
    G.append(list(input()))
Q = deque()
Q.append((sy, sx))
while Q:
    x, y = Q.popleft()
    d = dist[x][y]
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if G[nx][ny] == "#":
            continue
        if dist[nx][ny] == -1:
            dist[nx][ny] = d + 1
            Q.append((nx, ny))
print(dist[gy][gx])
