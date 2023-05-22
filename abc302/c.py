N, M = list(map(int, input().split()))
S = [list(input()) for _ in range(N)]

from itertools import permutations

for p in permutations(S):
    diff = 0
    for i in range(N - 1):
        for j in range(M):
            if p[i][j] != p[i + 1][j]:
                diff += 1
    if diff == (N - 1):
        print("Yes")
        exit()
print("No")
