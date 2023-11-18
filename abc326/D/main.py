#!/usr/bin/env python3
N = int(input())
R = input()
C = input()
# マス目作成
t = [["."] * N for _ in range(N)]

flag = False
ans = []


def check(tt):
    # 各行にちょうど1個ずつ
    # 各列にちょうど1個ずつ
    # R一致
    # C一致
    return True


l = ["A", "B", "C", ".", "."]
from itertools import permutations
pl = []
for i, p in enumerate(permutations(l, N)):
    pl.append(p)
ql = []
for tt in permutations(pl, N):
    if check(tt):
        flag = True
        ans = tt
        break
if flag:
    print("Yes")
    for i in range(N):
        print("".join(tt[i]))
else:
    print("No")
