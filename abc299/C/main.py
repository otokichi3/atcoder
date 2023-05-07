#!/usr/bin/env python3
import sys
import re


def solve(N: int, S: str):
    ans = max(map(len, S.split('-'))) if 'o' in S and '-' in S else -1
    print(ans)


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
