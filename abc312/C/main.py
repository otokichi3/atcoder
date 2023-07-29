#!/usr/bin/env python3
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [[x, 0] for x in A] + [[x + 1, 1] for x in B]
C.sort()
na, nb = 0, M
for x in C:
    if x[1] == 0:  # Aから来た
        na += 1
    else:  # Bから来た
        nb -= 1
    if na >= nb:
        print(x[0])
        break
