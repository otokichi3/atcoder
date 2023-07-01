#!/usr/bin/env python3
import sys
from itertools import product


def solve(ABCD: str):
    op_cnt = len(ABCD) - 1
    for op in product((' -', ' +'), repeat=op_cnt):
        f = [None] * (len(ABCD) + op_cnt)
        f[0::2] = list(ABCD)
        f[1::2] = list(op)
        f = ''.join(f).split()
        res = sum(map(int, f))
        if res == 7:
            print(''.join(f) + '=7')
            return
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    ABCD = next(tokens)  # type: str
    solve(ABCD)


if __name__ == "__main__":
    main()
