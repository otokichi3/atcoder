#!/usr/bin/env python3
import sys


def solve(N: int, A: int, B: int, C: "List[int]"):
    for i in range(N):
        if (A + B) == C[i]:
            print(i + 1)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B, C)


if __name__ == "__main__":
    main()
