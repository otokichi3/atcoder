import sys
sys.setrecursionlimit(10**6)

N, INF = int(input()), float('inf')
h = list(map(int, input().split()))
dp = [INF] * N

def memrec(i):
    if dp[i] != INF:
        return dp[i]
    res = INF
    if i == 0:
        return 0
    res = min(res, memrec(i - 1) + abs(h[i] - h[i - 1]))
    if i > 1:
        res = min(res, memrec(i - 2) + abs(h[i] - h[i - 2]))
    dp[i] = res
    return res

print(memrec(N-1))