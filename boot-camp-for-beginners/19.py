N, M, X = list(map(int, input().split()))
A = list(map(int, input().split()))
a1 = 0
a2 = 0
# from 0 to X
for i in range(X):
    if i in A:
        a1 += 1
# from X to N
for i in range(X, N):
    if i in A:
        a2 += 1
print(min(a1, a2))