#!/usr/bin/env python3
# ac*30,wa*8,re*4

h, w = map(int, input().split())
ga1 = [[0 for _ in range(w)] for _ in range(h)]
gb1 = [[0 for _ in range(w)] for _ in range(h)]
ga2 = [[0 for _ in range(h)] for _ in range(w)]
gb2 = [[0 for _ in range(h)] for _ in range(w)]

# 1. グリッドA
for i in range(h):
    s = list(map(int, input().split()))
    for j in range(w):
        ga1[i][j] = s[j]
        ga2[j][i] = s[j]

# 2. グリッドB
for i in range(h):
    s = list(map(int, input().split()))
    for j in range(w):
        gb1[i][j] = s[j]
        gb2[j][i] = s[j]

# 3. 一致しない場合は-1を出力して終了
gbs = list(map(set, gb1))
for i in range(h):
    gas = set(ga1[i])
    if gas in gbs:
        gbs.remove(gas)
    else:
        print(-1)
        exit()


# バブルソート
def bsort(l):
    cnt = 0
    for i in range(len(l)):
        for j in range(len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                cnt += 1
    return cnt


# 行方向
sga = [sorted(g) for g in ga1]
sgb = [sorted(g) for g in gb1]
li = []
for i in range(h):
    li.append(sgb.index(sga[i]))
lc = bsort(li)

# 列方向
sga = [sorted(g) for g in ga2]
sgb = [sorted(g) for g in gb2]
ri = []
for i in range(w):
    ri.append(sgb.index(sga[i]))
rc = bsort(ri)

print(lc + rc)
