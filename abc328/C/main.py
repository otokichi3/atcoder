#!/usr/bin/env python3
N, Q = map(int, input().split())
S = input()
t = [0] * N
cnt = 0
for i in range(1, N):
    if S[i-1] == S[i]:
        cnt += 1
    t[i] = cnt

for _ in range(Q):
    l, r = map(int, input().split())
    l, r = l-1, r-1
    print(t[r] - t[l])
