#!/usr/bin/env python3
import sys


def solve(ABCD: str):
    op_cnt = len(ABCD) - 1
    for i in range(2**op_cnt):
        op = ["-"] * op_cnt
        for j in range(op_cnt):
            if i & (1 << j):
                # i=1, j=0 のとき初めて+になる
                # そのときはLSBが1。つまり一番右が+になる
                op[op_cnt - 1 - j] = "+"
        
        formula = ""
        for n, o in zip(ABCD, op + [""]):
            formula += (n + o)
        if eval(formula) == 7:
            print(formula + "=7")
            break
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
