#!/usr/bin/env python3
N, M = map(int, input().split())
A = list(map(int, input().split()))
from collections import deque
q = deque(A)

cnt = 1
while q:
    x = q.popleft()
    for i in range(cnt, x + 1):
        print(x - i)
        cnt += 1
