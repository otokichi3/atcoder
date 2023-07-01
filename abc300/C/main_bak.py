#!/usr/bin/env python3

def solve(H, W, C):
    ans = [0] * min(H, W)
    cnt = 0
    for i in range(H):
        for j in range(W):
            if C[i][j] == '#':
                C[i][j] = '.'
                n = 1
                while(C[i+n][j+n] == '#'):
                    C[i+n][j+n] = '.'
                    n += 1
                    

        
    ans = [str(n) for n in ans]
    print(' '.join(ans))
    return

def main():
    H, W = map(int, input().split())
    C = ['.'] * H
    for i in range(H):
        C[i] = list(input())
    solve(H, W, C)

if __name__ == '__main__':
    main()
