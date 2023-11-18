#!/usr/bin/env python3
# (i, j) がグリッド内部かを判定する

def inside(i, j):
    return 0 <= i and i < 4 and 0 <= j and j < 4


# p を (di, dj) を左上の位置として配置できるか？
def can_put(exist, p, di, dj):
    for i in range(4):
        for j in range(4):
            if p[i][j] == "#":
                ni = i + di
                nj = j + dj
                if not inside(ni, nj):
                    return False
                if exist[ni][nj] == 1:
                    return False
                exist[ni][nj] = 1
    return True


from copy import deepcopy


didj = []
for i in range(-3, 4):
    for j in range(-3, 4):
        didj.append((i, j))

# ポリオミノを再帰で置いていく関数
def dfs(i, exist, ps):
    # i == 3 means all polyomino are placed
    if i == 3:
        ok = 1
        # 全グリッドと1との論理積を取る
        for u in range(4):
            ok &= all(exist[u])
        if ok:
            print("Yes")
            exit()
        return

    for di, dj in didj:
        ex2 = deepcopy(exist)
        if can_put(ex2, ps[i], di, dj):
            dfs(i + 1, ex2, ps)


def rotate(m):
    return list(zip(*m[::-1]))


ps = [[input() for _ in range(4)] for _ in range(3)]
for _ in range(4):
    for _ in range(4):
        v = [[0] * 4 for _ in range(4)]
        dfs(0, v, ps)
        ps[2] = rotate(ps[2])
    ps[1] = rotate(ps[1])
print("No")
