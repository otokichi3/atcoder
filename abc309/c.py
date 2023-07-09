N, K = map(int, input().split())
med = []
total = 0
for i in range(N):
    a, b = map(int, input().split())
    med.append((a, b))
    total += b
med = sorted(med, key=lambda x: x[0])
if total <= K:
    print(1)
else:
    for i in range(len(med)):
        if total <= K:
            print(med[i - 1][0] + 1)
            exit()
        total -= med[i][1]
    print(med[len(med) - 1][0] + 1)
