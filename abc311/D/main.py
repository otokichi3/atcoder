#!/usr/bin/env python3
from collections import deque

N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
visited[1][1] = True
q = deque()
start = (1, 1)  # 始点(2,2)
q.append(start)
end = set()
end.add(start)

while q:
    x, y = q.popleft()
    for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        for i in range(1, 200): # 壁でbreakするのでout of indexにはならない
            nx = x + dx * i # +でなく*なのは上もしくは左方向のとき負の値のため
            ny = y + dy * i
            if S[nx][ny] == ".":
                visited[nx][ny] = True
            else:
                nx -= dx
                ny -= dy
                if (nx, ny) not in end:
                    end.add((nx, ny))
                    q.append((nx, ny)) # 壁の直前の座標
                break

ans = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            ans += 1
print(ans)
