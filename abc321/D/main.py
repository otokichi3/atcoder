#!/usr/bin/env python3
N, M, P = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.sort()

from itertools import accumulate
from bisect import bisect

B_sum = [0] + list(accumulate(B))
ans = 0
for i in A:
    lb = bisect(B, P - i)
    ans += i * lb
    ans += B_sum[lb]
    ans += P * (M - lb)
print(ans)
