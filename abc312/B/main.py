#!/usr/bin/env python3
N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]
ans = []
for i in range(N):
    for j in range(M):
        if i + 8 < N and j + 8 < M:
            if (
                S[i][j] == "#"
                and S[i][j + 1] == "#"
                and S[i][j + 2] == "#"
                and S[i + 1][j] == "#"
                and S[i + 1][j + 1] == "#"
                and S[i + 1][j + 2] == "#"
                and S[i + 2][j] == "#"
                and S[i + 2][j + 1] == "#"
                and S[i + 2][j + 2] == "#"
                and S[i + 3][j] == "."
                and S[i + 3][j + 1] == "."
                and S[i + 3][j + 2] == "."
                and S[i + 3][j + 3] == "."
                and S[i][j + 3] == "."
                and S[i + 1][j + 3] == "."
                and S[i + 2][j + 3] == "."
            ):
                if (
                    S[i + 6][j + 6] == "#"
                    and S[i + 6][j + 7] == "#"
                    and S[i + 6][j + 8] == "#"
                    and S[i + 7][j + 6] == "#"
                    and S[i + 7][j + 7] == "#"
                    and S[i + 7][j + 8] == "#"
                    and S[i + 8][j + 6] == "#"
                    and S[i + 8][j + 7] == "#"
                    and S[i + 8][j + 8] == "#"
                    and S[i + 5][j + 5] == "."
                    and S[i + 5][j + 6] == "."
                    and S[i + 5][j + 7] == "."
                    and S[i + 5][j + 8] == "."
                    and S[i + 6][j + 5] == "."
                    and S[i + 7][j + 5] == "."
                    and S[i + 8][j + 5] == "."
                ):
                    ans.append([i + 1, j + 1])
for x in ans:
    print(*x)