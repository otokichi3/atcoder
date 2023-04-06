N, Y = map(int, input().split())
for i in range(0, N + 1):
    for j in range(0, N + 1 - i):
        if i * 10000 + j * 5000 + (N - i - j) * 1000 == Y:
            print(i, j, N - i - j)
            exit()
print("-1 -1 -1")
