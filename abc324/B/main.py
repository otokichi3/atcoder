#!/usr/bin/env python3
N = int(input())
for i in range(100):
    for j in range(100):
        if N == (2 ** i) * (3 ** j):
            print("Yes")
            exit()
print("No")
