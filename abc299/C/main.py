#!/usr/bin/env python3
import sys
import re


def s(N, S):
    res = -1
    n = 0
    for i in range(N):
        if S[i] == "o":
            n += 1
            if n > res:
                res = n
        else:
            n = 0
    return res


def solve(N: int, S: str):
    rmax = s(N, S)
    lmax = s(N, S[::-1])
    if rmax > lmax:
        print(rmax)
    else:
        print(lmax)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)


if __name__ == "__main__":
    main()
