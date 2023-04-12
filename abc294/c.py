# 汚い
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = A + B
C.sort()
md = {}
ans1 = []
ans2 = []
for i in range(N+M):
    md[C[i]] = i

for i in range(N+M):
    md[C[i]] = i

# A
for i in range(N):
    ans1.append(str(md[A[i]]+1))
for i in range(M):
    ans2.append(str(md[B[i]]+1))
print(' '.join(ans1))
print(' '.join(ans2))