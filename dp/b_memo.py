# メモ化再帰
import sys
sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
h = list(map(int, input().split()))
INF = float("inf")
memo = [INF] * N


def f(i):
    if i <= 0:
        return 0
    if memo[i] != INF:
        return memo[i]
    res = INF
    for j in range(1, K + 1):
        if i - j >= 0:
            res = min(res, f(i - j) + abs(h[i] - h[i - j]))
    memo[i] = res
    return res


print(f(N - 1))
