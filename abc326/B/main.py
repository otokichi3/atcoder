#!/usr/bin/env python3
N = int(input())


def check(N):
    if int(N[0]) * int(N[1]) == int(N[2]):
        return True
    else:
        return False


for i in range(N, 920):
    if check(str(i)):
        print(i)
        exit()
