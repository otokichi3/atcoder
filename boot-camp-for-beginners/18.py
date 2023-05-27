S = list(input())
ans = 0
cnt = 0
for i in S:
    if i in 'ACGT':
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0
print(ans)