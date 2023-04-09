S = input()
flag1 = False
flag2 = False
b1 = -1
b2 = -1
r1 = -1
r2 = -1
k = -1
for i in range(len(S)):
    if S[i] == 'B' and b1 == -1:
        b1 = i
    elif S[i] == 'B' and b1 != -1:
        b2 = i

    if S[i] == 'R' and r1 == -1:
        r1 = i
    elif S[i] == 'R' and r1 != -1:
        r2 = i
    
    if S[i] == 'K':
        k = i

if b1 % 2 == 0 and b2 % 2 != 0:
    flag1 = True
if b1 % 2 != 0 and b2 % 2 == 0:
    flag1 = True

if r1 < k and k < r2:
    flag2 = True

if flag1 == True and flag2 == True:
    print('Yes')
else:
    print('No')