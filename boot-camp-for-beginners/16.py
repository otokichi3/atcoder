N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict
d = defaultdict(int)
for i,a in enumerate(A):
    d[a] = i+1
d = sorted(d.items(), key=lambda x: x[0])
ans = []
for x in d:
    ans.append(x[1])
print(*ans)
    