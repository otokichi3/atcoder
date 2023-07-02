S = list(map(int,input().split()))
before = S[0]
for i in range(1, len(S)):
    if before <= S[i] and (100 <= S[i] <= 675) and (S[i] % 25 == 0):
        before = S[i]
        continue
    else:
        print('No')
        exit()
print('Yes')