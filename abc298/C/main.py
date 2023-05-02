#!/usr/bin/env python3
from collections import defaultdict


def solve(N: int, Q: int):
    box = defaultdict(list)
    card = defaultdict(set)

    for _ in range(Q):
        q = list(map(int, input().split()))
        i = int(q[1])
        if q[0] == 1:
            j = int(q[2])
            box[j].append(i)
            card[i].add(j)
        elif q[0] == 2:
            print(*sorted(box[i]))
        else:
            print(*sorted(list(card[i])))


def main():
    N = int(input())
    Q = int(input())

    solve(N, Q)


if __name__ == "__main__":
    main()
