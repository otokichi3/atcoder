N, M = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    pi = items[i][0]
    ci = items[i][1]
    fi = set(items[i][2:])
    for j in range(N):
        if i == j:
            continue
        pj = items[j][0]
        cj = items[j][1]
        fj = set(items[j][2:])
        if pi >= pj and fi <= fj and (pi > pj or cj > ci):
            print("Yes")
            exit()
print("No")
