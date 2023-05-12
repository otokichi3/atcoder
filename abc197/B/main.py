#!/usr/bin/env python3


def main():
    H, W, X, Y = list(map(int, input().split()))
    S = []
    for _ in range(H):
        S.append(list(input()))

    ans = 1
    # 以下、マス(X, Y)自体は参照しない
    # 上
    for i in range(X - 2, -1, -1):
        # print('up: ' + S[i][Y-1])
        if S[i][Y - 1] == ".":
            ans += 1
        else:
            break
    # 下
    for i in range(X, H, 1):
        # print('down: ' + S[i][Y-1])
        if S[i][Y - 1] == ".":
            ans += 1
        else:
            break
    # 左
    for i in range(Y - 2, -1, -1):
        # print('left: ' + S[X-1][i])
        if S[X - 1][i] == ".":
            ans += 1
        else:
            break
    # 右
    for i in range(Y, W, 1):
        # print('right: ' + S[X-1][i])
        if S[X - 1][i] == ".":
            ans += 1
        else:
            break
    print(ans)
    return


if __name__ == "__main__":
    main()
