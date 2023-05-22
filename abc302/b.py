H, W = list(map(int, input().split()))
s = []
for _ in range(H):
    s.append(list(input()))


def f(i, j):
    # 上下左右
    # ↑
    if i - 4 >= 0:
        if (
            s[i - 1][j] == "n"
            and s[i - 2][j] == "u"
            and s[i - 3][j] == "k"
            and s[i - 4][j] == "e"
        ):
            return [[i, j], [i - 1, j], [i - 2, j], [i - 3, j], [i - 4, j]]
    # ↓
    if H > i + 4:
        if (
            s[i + 1][j] == "n"
            and s[i + 2][j] == "u"
            and s[i + 3][j] == "k"
            and s[i + 4][j] == "e"
        ):
            return [[i, j], [i + 1, j], [i + 2, j], [i + 3, j], [i + 4, j]]
    if j - 4 >= 0:
        # ←
        if (
            s[i][j - 1] == "n"
            and s[i][j - 2] == "u"
            and s[i][j - 3] == "k"
            and s[i][j - 4] == "e"
        ):
            return [[i, j], [i, j - 1], [i, j - 2], [i, j - 3], [i, j - 4]]
    # →
    if j + 4 < W:
        if (
            s[i][j + 1] == "n"
            and s[i][j + 2] == "u"
            and s[i][j + 3] == "k"
            and s[i][j + 4] == "e"
        ):
            return [[i, j], [i, j + 1], [i, j + 2], [i, j + 3], [i, j + 4]]
    if i - 4 >= 0 and j + 4 < W:
        # 斜め
        # ↑→
        if (
            s[i - 1][j + 1] == "n"
            and s[i - 2][j + 2] == "u"
            and s[i - 3][j + 3] == "k"
            and s[i - 4][j + 4] == "e"
        ):
            return [
                [i, j],
                [i - 1, j + 1],
                [i - 2, j + 2],
                [i - 3, j + 3],
                [i - 4, j + 4],
            ]
    # →↓
    if i + 4 < H and j + 4 < W:
        if (
            s[i + 1][j + 1] == "n"
            and s[i + 2][j + 2] == "u"
            and s[i + 3][j + 3] == "k"
            and s[i + 4][j + 4] == "e"
        ):
            return [
                [i, j],
                [i + 1, j + 1],
                [i + 2, j + 2],
                [i + 3, j + 3],
                [i + 4, j + 4],
            ]
    # ←↓
    if i + 4 < H and j - 4 >= 0:
        if (
            s[i + 1][j - 1] == "n"
            and s[i + 2][j - 2] == "u"
            and s[i + 3][j - 3] == "k"
            and s[i + 4][j - 4] == "e"
        ):
            return [
                [i, j],
                [i + 1, j - 1],
                [i + 2, j - 2],
                [i + 3, j - 3],
                [i + 4, j - 4],
            ]
    # ←↑
    if i - 4 >= 0 and j - 4 >= 0:
        if (
            s[i - 1][j - 1] == "n"
            and s[i - 2][j - 2] == "u"
            and s[i - 3][j - 3] == "k"
            and s[i - 4][j - 4] == "e"
        ):
            return [
                [i, j],
                [i - 1, j - 1],
                [i - 2, j - 2],
                [i - 3, j - 3],
                [i - 4, j - 4],
            ]


for i in range(H):
    for j in range(W):
        if s[i][j] == "s":
            res = f(i, j)
            if res != None:
                res = [[x[0] + 1, x[1] + 1] for x in res]
                for x in res:
                    print(*x)
