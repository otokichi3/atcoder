#!/usr/bin/env python3
def check(s, t):
    if len(s) > len(t):
        return check(t, s)
    if len(s) < len(t) - 1:
        return False
    i, j, miss = 0, 0, 0
    while i < len(s):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            miss += 1
            if miss > 1:
                return False
            if len(s) == len(t):
                i += 1
            j += 1
    return True

N, T = input().split()
N = int(N)
ans = []
for i in range(N):
    S = input()
    if check(S, T):
        ans.append(i + 1)
print(len(ans))
print(" ".join(map(str, ans)))
