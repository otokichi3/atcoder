N = int(input())
S = input()
cond1 = False
cond2 = True
for i in range(N):
    if S[i] == "o":
        cond1 = True
    elif S[i] == "x":
        cond2 = False
if cond1 and cond2:
    print('Yes')
else:
    print('No')