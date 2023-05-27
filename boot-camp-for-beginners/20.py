s = int(input())
l = [s]
for i in range(1, 1000000):
    n = l[i - 1]
    res = n // 2 if n % 2 == 0 else 3 * n + 1
    if res in l:
        print(i+1)
        exit()
    else:
        l.append(res)
