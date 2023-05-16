N, M, C = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
for _ in range(N):
    A = list(map(int, input().split()))
    if 0 < (sum([a * B[i] for i, a in enumerate(A)]) + C):
        ans += 1
print(ans)