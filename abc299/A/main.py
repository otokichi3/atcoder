#!/usr/bin/env python3
import sys, re


def solve(N: int, S: str):
    # 文字列Sの中の*が|に挟まれていればYes
    p = "(.*\|.*\*.*\|)"
    pc = re.compile(p)
    res = re.search(pc, S)
    if res == None:
        print("out")
    else:
        print("in")


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
