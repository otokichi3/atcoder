N = int(input())
A = list(map(int, input().split()))
ans = []
for i in range(N):
    if A[i] % 2 == 0:
        ans.append(str(A[i]))
print(' '.join(ans))