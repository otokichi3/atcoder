from bisect import bisect

N, M, D = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.sort()
ans = -1
for a in A:
    i = bisect(B, a + D) - 1
    if i >= 0 and abs(a - B[i]) <= D:
        ans = max(ans, B[i] + a)
print(ans)
