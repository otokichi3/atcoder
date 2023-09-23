#!/usr/bin/env python3
N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(101):
    A.append(i)
    A.sort()
    res = sum(A[1 : N - 1])
    if res >= X:
        print(i)
        exit()
    idx = A.index(i)
    A = A[:idx] + A[idx + 1 :]
print(-1)
