N, D = map(int, input().split())
T = list(map(int, input().split()))
prev = T[0]
for i in range(1, N):
    if T[i] - prev <= D:
        print(T[i])
        break
    prev = T[i]
else:
    print('-1')