from math import sqrt

N, D = map(int, input().split())
d = []
for _ in range(2001):
    l = []
    for _ in range(2001):
        l.append(0)
    d.append(l)


p = []
for i in range(N):
    x, y = map(int, input().split())
    # マイナスは面倒なので+1000
    p.append([x + 1000, y + 1000])

for x in p:
    for i in range(d+1):
        for j in range(d+1):
            s = sqrt( (x[0] - i) ** 2 + (x[1] - j) ** 2)
            if euc <= D and (x[0] != i and x[1] != j):
                print(i, j)
                d[i][j] = -1
for x in p:
    if d[x[0]][x[1]] == -1:
        print("Yes")
    else:
        print("No")