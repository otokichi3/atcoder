#!/usr/bin/env python3

YES = "Yes"
NO = "No"

def main():
    N, Q = map(int, input().split())
    p = [0] * (N + 1)
    for _ in range(Q):
        e = list(map(int, input().split()))
        if e[0] == 1:
            p[e[1]] += 1
        if e[0] == 2:
            p[e[1]] += 2
        if e[0] == 3:
            if p[e[1]] >= 2:
                print('Yes')
            else:
                print('No')
                
    return

if __name__ == '__main__':
    main()
