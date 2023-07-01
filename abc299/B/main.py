#!/usr/bin/env python3
import sys


def solve(N: int, T: int, C: "List[int]", R: "List[int]"):
    p1c = C[0]
    max = 0
    p = 0
    if T in C:
        for i in range(N):
            if C[i] == T and R[i] > max:
                max = R[i]
                p = i
    else:
        for i in range(N):
            if C[i] == p1c and R[i] > max:
                max = R[i]
                p = i
    print(p + 1)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    C = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    R = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, T, C, R)


if __name__ == "__main__":
    main()
