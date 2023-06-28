N = int(input())
ans = [0] * (N * 7)
A = list(map(int, input().split()))
for i in range(N * 7):
    idx = i // 7
    ans[idx] += A[i]

print(*ans[0:N])
