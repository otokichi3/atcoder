import sys

sys.setrecursionlimit(10**6)
# 縦読みすると、
# dx[0],dy[0]:→
# dx[1],dy[1]:↓
# dx[2],dy[2]:←
# dx[3],dy[3]:↑
# となる。
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
seen = [[False] * 510 for _ in range(510)]


def dfs(h, w):
    seen[h][w] = True

    for dir in range(4):
        nh = h + dx[dir]
        nw = w + dy[dir]

        if nh < 0 or nh >= H or nw < 0 or nw >= W:
            continue
        if field[nh][nw] == "#":
            continue

        if seen[nh][nw]:
            continue

        dfs(nh, nw)


H, W = map(int, input().split())
field = [list(input()) for _ in range(H)]
sh, sw, gh, gw = 0, 0, 0, 0
for h in range(H):
    for w in range(W):
        if field[h][w] == "s":
            sh, sw = h, w
        if field[h][w] == "g":
            gh, gw = h, w
dfs(sh, sw)

if seen[gh][gw]:
    print("Yes")
else:
    print("No")
