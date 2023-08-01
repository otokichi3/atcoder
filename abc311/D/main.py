#!/usr/bin/env python3
from collections import deque
N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]
print(N, M, S)

visited = [[False] * M for _ in range(N)]
q = deque()
q.append((1, 1)) # 始点(2,2)
d = [(-1, 0), (0, -1), (1, 0), (0, 1)]

while q: # queueが空になるまで
    x, y = q.popleft()
    visited[x][y] = True

    # 上下左右に突き当たりまで進む
    # ただし突き当りまでの道がすべて訪問済みなら進まない
    go = False
    end = None
    for i in range(x, N-x): # 下方向
        nx = x + i
        if S[nx][y] == ".":
            if not visited[nx][y]:
                visited[nx][y] = True
                go = True
            if go:
                end = (nx, y)
        else:
            break
    if go:
        q.append(end)
        go = False

    for i in range(x): # 上方向
        nx = x - i
        if S[nx][y] == ".":
            if not visited[nx][y]:
                visited[nx][y] = True
                go = True
            if go:
                end = (nx, y)
        else:
            break
    if go:
        q.append(end)
        go = False

    for i in range(y, M-y): # 右方向
        ny = y + i
        if S[x][ny] == ".":
            if not visited[x][ny]:
                visited[x][ny] = True
                go = True
            if go:
                end = (x, ny)
        else:
            break
    if go:
        q.append(end)
        go = False

    for i in range(y): # 左方向
        ny = y - i
        if S[x][ny] == ".":
            if not visited[x][ny]:
                visited[x][ny] = True
                go = True
            if go:
                end = (x, ny)
        else:
            break
    if go:
        q.append(end)
        go = False
    print(q)

ans = 0
for i in range(N):
    for j in range(M):
        if S[i][j] == "#":
            S[i][j] = "■"

        if visited[i][j]:
            S[i][j] = "x"
            ans += 1
for i in range(N):
    print(*S[i])
print(ans)