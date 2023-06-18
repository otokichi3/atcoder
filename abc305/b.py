d = [0, 3, 1, 4, 1, 5, 9]
a = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
ans = 0

p, q = input().split()
if a[p] < a[q]:
    for i in range(a[p]+1, a[q]+1):
        ans += d[i]
else:
    for i in range(a[q]+1, a[p]+1):
        ans += d[i]
print(ans)