N, X = list(map(int, input().split()))
A = [int(x) for x in input().split()]
flag = False

ans = []
for i in range(N):
    ans.append(X + A[i])

if (len(set(A) & set(ans))) > 0:
    flag = True

if flag == True:
    print('Yes')
else:
    print('No')

