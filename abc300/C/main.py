#!/usr/bin/env python3


def solve(H, W, C):
    ans = [0] * min(H, W)
    for i in range(H - 1):
        for j in range(W - 1):
            # minmimum batsu
            if (
                C[i][j] == "#"
                and C[i - 1][j - 1] == "#"
                and C[i - 1][j + 1] == "#"
                and C[i + 1][j - 1] == "#"
                and C[i + 1][j + 1] == "#"
            ):
                n = 1
                while (
                    i + n + 1 < H and j + n + 1 < W and C[i + n + 1][j + n + 1] == "#"
                ):
                    n += 1
                ans[n - 1] += 1

    ans = [str(n) for n in ans]
    print(" ".join(ans))
    return


def main():
    H, W = map(int, input().split())
    C = ["."] * H
    for i in range(H):
        C[i] = list(input())
    solve(H, W, C)


if __name__ == "__main__":
    main()
