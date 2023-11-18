#!/usr/bin/env python3
N, M = map(int, input().split())
S = input()
T = input()
pre = False
post = False
l = len(S)
if T[0:l] == S:
    pre = True
if T[-l:] == S:
    post = True

ans = 0
if pre and post:
    ans = 0
elif pre and not post:
    ans = 1
elif not pre and post:
    ans = 2
else:
    ans = 3
print(ans)
