N, M = map(int, input().split())
C = input().split()
D = input().split()
d = {}
P = list(map(int, input().split()))
other = P[0]
for i in range(M):
    d[D[i]] = P[i + 1]
ans = 0
for c in C:
    if c in d:
        ans += d[c]
    else:
        ans += other
print(ans)
