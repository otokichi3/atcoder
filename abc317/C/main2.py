#!/usr/bin/env python3
N, M = map(int, input().split())
G = [[0] * N for _ in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    G[a][b] = G[b][a] = c


from itertools import permutations

ans = 0
for p in permutations(range(N)):
    ansi = 0
    for i in range(N - 1):
        a = p[i]
        b = p[i + 1]
        d = G[a][b]
        if d == 0:
            break
        ansi += d
    ans = max(ans, ansi)
print(ans)
