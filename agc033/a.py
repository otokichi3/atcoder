from collections import deque

H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]
dist = [[-1] * W for _ in range(H)]
blacks = deque()
for h in range(H):
    for w in range(W):
        if grid[h][w] == "#":  # blacks
            blacks.append((h, w))
            dist[h][w] = 0


def bfs(blacks, dist):
    while blacks:
        h, w = blacks.popleft()
        d = dist[h][w]
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nh = h + dy
            nw = w + dx
            if nh < 0 or H <= nh or nw < 0 or W <= nw:
                continue
            if dist[nh][nw] == -1:
                dist[nh][nw] = d + 1
                blacks.append((nh, nw))
    return d


d = bfs(blacks, dist)
print(d)
