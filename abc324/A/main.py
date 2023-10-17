#!/usr/bin/env python3

N = int(input())
A = input().split()
for i in range(N):
    if i + 1 < N:
        if A[i] == A[i+1]:
            continue
        else:
            print("No")
            exit()
print("Yes")