#!/usr/bin/env python3
import sys

sys.setrecursionlimit(10**6)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]
seen = [[False] * W for _ in range(H)]
p = {">": None, "v": None, "<": None, "^": None}
for i in range(H):
    for j in range(W):
        if grid[i][j] == "S":
            s = [i, j]
        if grid[i][j] == "G":
            g = [i, j]
        if grid[i][j] == ">":
            for k in range(j, W):
                if k < W:
                    if j != k:
                        if grid[i][k] in p or grid[i][k] == "#":
                            break
                        grid[i][k] = "!"
                else:
                    break
        if grid[i][j] == "v":
            for k in range(i, H):
                if k < H:
                    if i != k:
                        if grid[k][j] in p or grid[k][j] == "#":
                            break
                        grid[k][j] = "!"
                else:
                    break
        if grid[i][j] == "<":
            for k in range(j + 1):
                l = j - k
                if l >= 0:
                    if j != l:
                        if grid[i][l] in p or grid[i][l] == "#":
                            break
                        grid[i][l] = "!"
        if grid[i][j] == "^":
            for k in range(i + 1):
                l = i - k
                if l >= 0:
                    if i != l:
                        if grid[l][j] in p or grid[l][j] == "#":
                            break
                        grid[l][j] = "!"

for i in range(H):
    for j in range(W):
        if grid[i][j] in p or grid[i][j] == "!":
            grid[i][j] = "#"

# for i in range(H):
#     print("".join(grid[i]))


cnt = 0
def dfs(h, w):
    global cnt

    seen[h][w] = True

    for dir in range(4):
        nh = h + dx[dir]
        nw = w + dy[dir]

        if nh < 0 or nh >= H or nw < 0 or nw >= W:
            continue
        if grid[nh][nw] == "#":
            continue
        if seen[nh][nw]:
            continue
        if nh == g[0] and nw == g[1]:
            print(cnt)
            exit()

        cnt += 1
        dfs(nh, nw)


dfs(s[0], s[1])
print(-1)
