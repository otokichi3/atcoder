#!/usr/bin/env python3
import sys
from collections import defaultdict

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(S: str, T: str):
    scnt = defaultdict(int)
    tcnt = defaultdict(int)
    for c in S: scnt[c] += 1
    for c in T: tcnt[c] += 1
    for c in "atcoder":
        m = max(scnt[c], tcnt[c])
        if scnt["@"] < m - scnt[c] or tcnt["@"] < m - tcnt[c]:
            print(NO)
            return
        scnt["@"] -= m - scnt[c]
        scnt[c] = m
        tcnt["@"] -= m - tcnt[c]
        tcnt[c] = m
    print(YES if scnt == tcnt else NO)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    solve(S, T)

if __name__ == '__main__':
    main()