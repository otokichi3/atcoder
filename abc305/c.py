H, W = map(int, input().split())
S = [input() for _ in range(H)]
for i in range(H):
    for j in range(W):
        # 自身除く上下左右に2マス以上クッキーがあればそこが食われたマス
        cnt = 0
        if S[i][j] == ".":
            if i - 1 >= 0 and S[i - 1][j] == "#":
                cnt += 1
            if i + 1 < H and S[i + 1][j] == "#":
                cnt += 1
            if j - 1 >= 0 and S[i][j - 1] == "#":
                cnt += 1
            if j + 1 < W and S[i][j + 1] == "#":
                cnt += 1
        if cnt >= 2:
            print(i + 1, j + 1)
            exit()
