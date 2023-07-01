#!/usr/bin/env python3
def main():
    N = int(input())
    l = 1
    r = N
    cnt = 20
    while (cnt > 0):
        mid = (l + r) // 2
        print(f'? {mid}')
        i = int(input())
        if l + 1 == r:
            print(f'! {l}')
            return
        if i == 0:
            l = mid
        else:
            r = mid


main()