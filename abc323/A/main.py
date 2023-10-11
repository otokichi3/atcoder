#!/usr/bin/env python3
S = input()
for i in range(17):
    if i % 2 == 1:
        if S[i] == "1":
            print("No")
            exit()
print("Yes")