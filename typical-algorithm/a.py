from bisect import bisect

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
i = bisect(A, K)
if i >= 0 and i != N:
    print(i)
else:
    print(-1)
