N = int(input())
S = input()

flag = False
for i in range(N-1):
    if S[i] == S[i+1]:
        flag = True

if flag == True:
    print('No')
else:
    print('Yes')

        
