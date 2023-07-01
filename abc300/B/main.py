#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str


# 縦シフト
def vshift(A):
    a = A.pop(len(A) - 1)
    A.insert(0, a)
    return A


# 横シフト
def hshift(A):
    for i in range(len(A)):
        a = A[i].pop(len(A[i]) - 1)
        A[i].insert(0, a)
    return A


def solve(H, W, A, B):
    for _ in range(H):
        for _ in range(W):
            ok = True
            for i in range(H):
                if A[i] != B[i]:
                    ok = False
                    break
            if ok == True:
                print(YES)
                return
            hshift(A)
        vshift(A)
    print(NO)
    return


def main():
    H, W = map(int, input().split())
    A = ["."] * H
    B = ["."] * H
    for i in range(H):
        A[i] = list(input())
    for i in range(H):
        B[i] = list(input())
    solve(H, W, A, B)


if __name__ == "__main__":
    main()
