N = int(input())
d = list(map(int, input().split()))
d.sort()
l = len(d)
a = d[: l // 2]
b = d[l // 2 :]
if a[-1] == b[0]:
    print(0)
else:
    print(b[0] - a[-1])
