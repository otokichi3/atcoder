H, W = map(int, input().split())
table = []
row = ''
skip = False
for i in range(H):
    S = input()
    row = list(S)
    for j in range(W-1):
        if row[j] == 'T' and row[j+1] == 'T':
            row[j] = 'P'
            row[j+1] = 'C'
            skip = True
        elif skip == True:
            skip = False
            continue
        else:
            continue
    table.append(row)

for i in range(H):
    print(''.join(table[i]))