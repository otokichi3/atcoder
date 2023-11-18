#!/usr/bin/env python3
S = input()
t = []
for x in S:
    t.append(x)
    if len(t) > 2 and t[-1] == "C" and t[-2] == "B" and t[-3] == "A":
        t.pop()
        t.pop()
        t.pop()
print("".join(t))