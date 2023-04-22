#!/usr/bin/env python3
import sys
import re


def solve(N: int, S: str):
    res = re.findall(r'(o+)-', S)
    len_list = list(map(len, res))
    if len(len_list) >= 1:
        print(max(len_list))
    else:
        print(-1)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)

if __name__ == '__main__':
    main()
