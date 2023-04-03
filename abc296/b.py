S = []
for i in range(8):
    S.append(input())

for i in range(8):
    for j in range(8):
        if S[i][j] == '*':
            if j == 0:
                print('a', 8-i, sep='')
            if j == 1:     
                print('b', 8-i, sep='')
            if j == 2:     
                print('c', 8-i, sep='')
            if j == 3:     
                print('d', 8-i, sep='')
            if j == 4:     
                print('e', 8-i, sep='')
            if j == 5:     
                print('f', 8-i, sep='')
            if j == 6:     
                print('g', 8-i, sep='')
            if j == 7:     
                print('h', 8-i, sep='')
