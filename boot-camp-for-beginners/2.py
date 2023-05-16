N = int(input())
X = list(map(int, input().split()))
min = 2**32
for p in range(1, max(X)+1):
    res = sum([(xi-p)**2 for xi in X])
    if res < min:
        min = res
print(min)
    