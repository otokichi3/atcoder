#!/usr/bin/env python3
K = int(input())


def is321(N):
    for i in range(len(N) - 1):
        if N[i] <= N[i + 1]:
            return False
    return True


from itertools import permutations

cnt = 0
for i in range(1, 11):
    for p in permutations(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], i):
        if p[0] == "0":
            continue
        if int(p[0]) < len(p) - 1:
            continue
        s = "".join(p)
        if is321(s):
            cnt += 1
            if cnt == K:
                print(s)
                exit()
