#!/usr/bin/env python3
import sys

sys.setrecursionlimit(10**6)
H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]
seen = [[False] * W for _ in range(H)]


def dfs(h, w):
    global grid
    seen[h][w] = True
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)):
        nh = h + dy
        nw = w + dx
        if nh < 0 or nh >= H or nw < 0 or nw >= W:
            continue
        if seen[nh][nw]:
            continue
        if grid[nh][nw] == "#":
            grid[nh][nw] = "."
            dfs(nh, nw)


ans = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == "#":
            ans += 1
            dfs(i, j)
print(ans)