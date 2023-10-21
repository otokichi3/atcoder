#!/usr/bin/env python3
# けんちょんさんのコードを Python 化したまま
N = int(input())
num = [0] * (N + 1)
for x in range(1, N):
    for y in range(1, N):
        if x * y > N:
            break
        num[x * y] += 1
res = 0
for v in range(N):
    ab = num[v]
    cd = num[N - v]
    res += ab * cd
print(res)