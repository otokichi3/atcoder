N, P, Q = map(int, input().split())
D = list(map(int, input().split()))
p1 = P
p2 = Q + min(D)
if p1 > p2:
    print(p2)
else:
    print(p1)
