#!/usr/bin/env python3
N = int(input())
S = list(input())
for i in range(N):
    if i + 3 <= N:
        if S[i] == "A" and S[i + 1] == "B" and S[i + 2] == "C":
            print(i + 1)
            exit()
print(-1)
