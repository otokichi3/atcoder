#!/usr/bin/env python3

# 1.Input
h, w = map(int, input().split())
g = [list(input()) for _ in range(h)]


while True:
    # 2.転置前行列の削除対象行を洗い出す
    kesu_line = []
    for i in range(len(g)):
        # 長さが2以上かつ重複排除後に1種類のみなら削除対象
        if len(g[i]) >= 2 and len(set(g[i])) == 1:
            kesu_line.append(i)


    # 3.転置後行列の削除対象行を洗い出す
    kesu_row = []
    t = list(zip(*g))
    for i in range(len(t)):
        # 長さが2以上かつ重複排除後に1種類のみなら削除対象
        if len(t[i]) >= 2 and len(set(t[i])) == 1:
            kesu_row.append(i)

    # 削除対象がなければ終了
    if len(kesu_line) + len(kesu_row) == 0:
        break

    # 行の削除(前から削除すると削除するインデックスがずれるためreversd)
    for i in kesu_row[::-1]:
        if len(t) <= i:
            break
        _ = t.pop(i)

    # 列の削除(転置して削除対象の列を行として削除)
    g = list(zip(*t)) # 転置行列を転置して元の行列に戻す
    for i in kesu_line[::-1]:
        if len(g) <= i:
            break
        _ = g.pop(i)

ans = 0
for i in range(len(g)):
    ans += len(g[i])
        
print(ans)