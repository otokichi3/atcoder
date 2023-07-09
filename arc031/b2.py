# BFS
import sys

sys.setrecursionlimit(10**6)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
seen = [[-1] * 10 for _ in range(10)]


def dfs(h, w):
    global cnt

    seen[h][w] = True

    for dir in range(4):
        nh = h + dx[dir]
        nw = w + dy[dir]

        if nh < 0 or nh >= H or nw < 0 or nw >= W:
            continue
        if field[nh][nw] == "x":
            continue
        if seen[nh][nw]:
            continue

        cnt += 1
        dfs(nh, nw)


H, W = 10, 10
field = [list(input()) for _ in range(H)]
start = []
islands_count = 0
for h in range(H):
    for w in range(W):
        if field[h][w] == "x":
            start.append((h, w))
        else:
            islands_count += 1
for s in start:
    cnt = 0
    dfs(s[0], s[1])
    if cnt == islands_count:
        print("YES")
        exit()
    cnt = 0
    seen = [[False] * 10 for _ in range(10)]
print("NO")
