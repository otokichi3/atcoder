#!/usr/bin/env python3
import sys


def solve(S: int, T: int):
    ans = 0
    for a in range(S + 1):
        for b in range(S + 1):
            for c in range(S + 1):
                if a + b + c <= S and a * b * c <= T:
                    ans += 1
    print(ans)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    solve(S, T)


if __name__ == "__main__":
    main()
