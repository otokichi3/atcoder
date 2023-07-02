from functools import cmp_to_key


def cmp(a, b):
    l = a[0] * (b[0] + b[1])
    r = b[0] * (a[0] + a[1])
    if l == r:
        return 1 if a[2] < b[2] else -1
    elif l > r:
        return 1
    else:
        return -1

    return 0


N = int(input())
res = []
for i in range(N):
    A, B = map(int, input().split())
    res.append((A, B, i + 1))
l = sorted(res, key=cmp_to_key(cmp), reverse=True)
ans = []
for v in l:
    ans.append(v[2])
print(*ans)
