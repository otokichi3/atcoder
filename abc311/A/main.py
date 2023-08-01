#!/usr/bin/env python3
N = int(input())
S = list(input())
a, b, c = False, False, False
for i in range(N):
    s = S[i]
    if s == "A":
        a = True
    if s == "B":
        b = True
    if s == "C":
        c = True
    if a and b and c:
        print(i + 1)
        exit()