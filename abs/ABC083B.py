N, A, B = map(int, input().split())
ans = 0
for i in range(1, N+1):
    strnum = str(i)
    strsum = 0
    for j in range(len(strnum)):
        strsum += int(strnum[j])
    if strsum >= A and strsum <= B:
        ans += int(strnum)
print(ans)