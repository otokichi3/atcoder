import collections
N = int(input())
A = list(map(int, input().split()))
ans = 0
c = collections.Counter(A)
for k in c.keys():
    ans += c[k] // 2
print(ans)