#!/usr/bin/env python3
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(lambda x: int(x) + 1, input().split()))
C = sorted(A + B)
print(C[m-1])