#!/usr/bin/env python3
X, Y = map(int, input().split())
# 下り
flag = False
if X - Y > 0:
    if abs(X - Y) <= 3:
        flag = True
    else:
        flag = False
else:
    if abs(X - Y) <= 2:
        flag = True
    else:
        flag = False
if flag:
    print("Yes")
else:
    print("No")
