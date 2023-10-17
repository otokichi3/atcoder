#!/usr/bin/env python3
N, T2 = input().split()
N = int(N)


def check(T, T2):
    A = 0
    B = 0
    if abs(len(T) - len(T2)) >= 2:
        return False
    for j in range(len(T)):
        if len(T2) > j and T2[j] == T[j]:
            A += 1
        else:
            break
    rT = "".join(list(reversed(T)))
    rT2 = "".join(list(reversed(T2)))
    for j in range(len(rT)):
        if len(rT2) > j and rT2[j] == rT[j]:
            B += 1
        else:
            break
    flag = False
    if A == len(T) and len(T) == len(T2):
        flag = True
    if A + B >= len(T) and len(T) + 1 == len(T2):
        flag = True
    if A + B >= len(T) - 1 and len(T) - 1 == len(T2):
        flag = True
    if A + B == len(T) - 1 and len(T) == len(T2):
        flag = True
    return flag


ans = []
for i in range(N):
    T = input()
    if check(T, T2):
        ans.append(i + 1)
print(len(ans))
print(*ans)
