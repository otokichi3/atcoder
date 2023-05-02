#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def rotate(N: int, A: "List[List[int]]"):
    res = [0] * N
    for i in range(N):
        res[i] = [0] * N
        for j in range(N):
            res[i][j] = A[N-j-1][i]
    return res

def solve(N: int, A: "List[List[int]]", B: "List[List[int]]"):
    for _ in range(4):
        ok = True
        for j in range(N):
            for k in range(N):
                if (A[j][k] == 1 and B[j][k] == 0):
                    ok = False
        if ok == True:
            print(YES)
            return
        else:
            A = rotate(N, A)
    print(NO)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(N)] for _ in range(N)]  # type: "List[List[int]]"
    B = [[int(next(tokens)) for _ in range(N)] for _ in range(N)]  # type: "List[List[int]]"
    solve(N, A, B)

if __name__ == '__main__':
    main()
