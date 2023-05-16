N, A, B = list(map(int, input().split()))
S = input()
passed = A + B
fr = 0
for i, x in enumerate(list(S)):
    if passed > 0:
        if x == 'a':
            print('Yes')
            passed -= 1
        elif x == 'b' and fr < B:
            print('Yes')
            fr += 1
            passed -= 1
        else:
            print('No')
    else:
        print('No')
exit()