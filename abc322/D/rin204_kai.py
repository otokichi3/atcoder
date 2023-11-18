#!/usr/bin/env python3
S = []
c = 0
for _ in range(3):
    T = [list(input()) for _ in range(4)]
    S.append(T)
    for row in T:
        c += row.count("#")

if c != 16:
    print("No")
    exit()

didj = []
for i in range(-3, 4):
    for j in range(-3, 4):
        didj.append((i, j))


def rot(x):
    return list(zip(*x[::-1]))


def f(S):
    res = []
    for _ in range(4):
        for di, dj in didj:
            ok = True
            nex = [["."] * 4 for _ in range(4)]
            for i in range(4):
                for j in range(4):
                    if S[i][j] == "#":
                        ni = i + di
                        nj = j + dj
                        if ni < 0 or 4 <= ni or nj < 0 or 4 <= nj:
                            ok = False
                            break
                        nex[ni][nj] = "#"
                if not ok:
                    break
            if ok:
                res.append(nex)
        S = rot(S)
    return res


A = f(S[0])
B = f(S[1])
C = f(S[2])

for a in A:
    for b in B:
        for c in C:
            ok = True
            for i in range(4):
                for j in range(4):
                    if a[i][j] == "." and b[i][j] == "." and c[i][j] == ".":
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                print("Yes")
                exit()
print("No")
