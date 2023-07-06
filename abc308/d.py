import sys
from collections import deque

sys.setrecursionlimit(10**6)
H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]
seen = [[False] * W for _ in range(H)]
next = {"s": "n", "n": "u", "u": "k", "k": "e", "e": "s"}
q = deque()
q.append((0, 0))


def bfs(q):
    h, w = q.popleft()
    seen[h][w] = True
    c = grid[h][w]
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        nh = h + dy
        nw = w + dx
        if nh < 0 or nh >= H or nw < 0 or nw >= W:
            continue
        # snuke判定
        if c not in next or grid[nh][nw] != next[c]:
            continue

        if seen[nh][nw]:
            continue
        q.append((nh,nw))
        bfs(q)

bfs(q)
# print(seen)
if seen[H-1][W-1]:
    print('Yes')
else:
    print('No')

