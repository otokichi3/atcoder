H, W = map(int, input().split())
for i in range(H):
    temp = []
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if row[j] == 0:
            temp.append('.')
        else:
            temp.append(chr(row[j]+64))
    print(''.join(temp))