#!/usr/bin/env python3
import sys

def eratosthenes(N: int):
    isprime = [True] * (N + 1)
    for i in range(2, N + 1):
        if not isprime[i]:
            continue
        x = i * 2
        while x <= N:
            isprime[x] = False
            x += i
    return [i for i, x in enumerate(isprime) if i > 1 and x == True]

def solve(N: int):
    primes = eratosthenes(N)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
