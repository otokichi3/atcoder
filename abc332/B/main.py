#!/usr/bin/env python3
k, g, m = map(int, input().split())
G, M = 0, 0
for _ in range(k):
    if G == g:
        G = 0
    elif M == 0:
        M = m
    else:
        while True:
            if M == 0 or G == g:
                break
            M -= 1
            G += 1
print(G, M)
