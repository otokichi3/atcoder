N = int(input())
K = int(input())
x = list(map(int, input().split()))
ans = 0
for i in range(N):
    if x[i] < K - x[i]:
        ans += x[i] * 2
    else:
        ans += (K - x[i]) * 2
print(ans)