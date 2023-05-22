K, N = list(map(int, input().split()))
A = list(map(int, input().split()))
A.append(K+A[0])
d = 0

for i in range(N):
    d = max(d, A[i+1] - A[i])

print(K-d)