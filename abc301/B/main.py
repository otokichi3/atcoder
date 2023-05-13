#!/usr/bin/env python3
import sys


#  数列 A のどの隣接する 2 項の差の絶対値も 1 であるとき、Falseを返す
def f(A):
    for i in range(len(A)-1):
        if abs(A[i] - A[i + 1]) != 1:
            return True
    return False


def solve(N: int, A: "List[int]"):
    while f(A):
        for i in range(len(A) - 1):
            l = []
            if abs(A[i] - A[i + 1]) != 1:
                if A[i] < A[i + 1]:
                    for j in range(A[i] + 1, A[i + 1]):
                        l.append(j)
                    A = A[:i+1] + l + A[i+1:]
                    continue
                if A[i] > A[i + 1]:
                    for j in range(A[i] - 1, A[i+1], -1):
                        l.append(j)
                    A = A[:i+1] + l + A[i+1:]
                    break
    A = list(map(str, A))
    print(" ".join(A))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)


if __name__ == "__main__":
    main()
