N = int(input())
ans = {}
for _ in range(N):
    s, a = input().split()
    ans[int(a)] = s
young = min(ans)
former = []
latter = []

for k,v  in ans.items():
    if k == young:
        latter.append(v)
    else:
        if len(latter) > 0:
            latter.append(v)
        else:
            former.append(v)
ans = latter + former
print(*ans, sep="\n")
