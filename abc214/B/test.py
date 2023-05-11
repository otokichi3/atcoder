from itertools import product

N = 5
for p in product([0,1], repeat=N):
    print(p)