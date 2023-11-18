#!/usr/bin/env python3
N = int(input())
D = list(map(int, input().split()))


def check(m, d):
    s = str(m) + str(d)
    for i in range(len(s) - 1):
        if s[i] != s[i+1]:
            return False
    return True


ans = 0
for i in range(len(D)):
    for j in range(1, D[i]+1):
        if check(i+1, j):
            ans += 1
print(ans)
