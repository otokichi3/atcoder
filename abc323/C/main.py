#!/usr/bin/env python3
def mysum(a):
    res = 0
    for x in a:
        if x >= 0:
            res += x
    return res

N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]
T = [[0] * M for _ in range(N)]
P = [0 for _ in range(N)]
for i in range(N):
    for j in range(M):
        if S[i][j] == "o":
            T[i][j] = A[j]
        else:
            T[i][j] = -A[j]
l = []
for i in range(N):
    l.append(mysum(T[i]) + i + 1)
m = max(l)
for i in range(N):
    if l[i] >= m:
        # すでに総合得点以上
        print(0)
    else:
        # 1問以上解く必要あり
        T[i].sort()
        cnt = 0
        for j in range(M):
            l[i] += -T[i][j]
            cnt += 1
            if l[i] >= m:
                print(cnt)
                break