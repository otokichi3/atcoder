N, Y = map(int, input().split())
for i in range(0, N+1):
    for j in range(0, N+1-i):
        for k in range(0, N+1-i-j):
            if i*1000 + j*5000 + k*10000 == Y:
                print(k, j, i)
                exit()
print('-1 -1 -1')