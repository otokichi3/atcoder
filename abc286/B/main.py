#!/usr/bin/env python3
N = int(input())
S = input()
ans = []
cnt = 0
for i in range(N):
    if i < cnt:
        continue
    cnt += 1
    if i + 1 < N and S[i] == "n" and S[i+1] == "a":
        ans.append("nya")
        cnt += 1
    else:
        ans.append(S[i])
print("".join(ans))