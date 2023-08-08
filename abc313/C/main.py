#!/usr/bin/env python3
N = int(input())
A = list(map(int, input().split()))
s = sum(A)
B = [s // N] * N
for i in range(s % N):
    B[i] += 1
A.sort()
B.sort()
ans = 0
for a, b in zip(A, B):
    ans += abs(a - b)
print(ans // 2)
