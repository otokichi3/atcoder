N, M = list(map(int, input().split()))
a = [list(map(int, input().split())) for i in range(M)]
l1 = []
# 考えられる全組み合わせを作成
for i in range(N):
    for j in range(i + 1, N):
        l1.append([i + 1, j + 1])


def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]


# 実際の並び順から全組み合わせを作成
l2 = []
for i in range(M):
    for j in range(0, N - 1):
        l2.append([a[i][j], a[i][j + 1]])
l2 = get_unique_list(l2)

ans = []

for p in l1:
    if p in l2 or [p[1], p[0]] in l2:
        pass
    else:
        ans.append(p)
print(len(ans))
