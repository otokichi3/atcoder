#!/usr/bin/env python3
import sys


def solve(N: int, M: int, A: "List[int]", B: "List[str]", C: "List[int]", D: "List[str]"):
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [str()] * (M)  # type: "List[str]"
    C = [int()] * (M)  # type: "List[int]"
    D = [str()] * (M)  # type: "List[str]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = next(tokens)
        C[i] = int(next(tokens))
        D[i] = next(tokens)
    solve(N, M, A, B, C, D)

if __name__ == '__main__':
    main()