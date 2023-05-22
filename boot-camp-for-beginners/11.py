N = int(input())
ans = 0
mcnt = -1
for x in range(1, N + 1):
    cnt = 0
    tmp = x
    while tmp % 2 == 0:
        tmp /= 2
        cnt += 1
    if cnt > mcnt:
        mcnt = cnt
        ans = x
print(ans)
