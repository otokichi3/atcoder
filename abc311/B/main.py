#!/usr/bin/env python3
N, D = map(int, input().split())
S = [list(input()) for _ in range(N)]
ans = 0
s = 0
for i in range(D):
    for j in range(N):
        if S[j][i] == "x":
            ans = max(ans, s)
            s = 0
            break
    else:
        s += 1
print(max(ans,s))